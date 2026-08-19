// robot_base_node: 订阅 /cmd_vel (Twist: vx=linear.x, vy=linear.y, wz=angular.z)
// 打包成 18 字节帧发往下位机 USART1:
//   AA 55 | vx(float LE) | vy(float LE) | wz(float LE) | crc16(LE) | 0D 0A
// CRC-CCITT 覆盖 [0..13],与下位机 crc_ccitt.h 一致。
//
// 串口用 POSIX termios 实现,无第三方依赖。

#include <cstring>
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#include <cerrno>
#include <cstdio>

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

namespace {

constexpr uint16_t crc_ccitt_table[256] = {
  0x0000, 0x1189, 0x2312, 0x329b, 0x4624, 0x57ad, 0x6536, 0x74bf,
  0x8c48, 0x9dc1, 0xaf5a, 0xbed3, 0xca6c, 0xdbe5, 0xe97e, 0xf8f7,
  0x1081, 0x0108, 0x3393, 0x221a, 0x56a5, 0x472c, 0x75b7, 0x643e,
  0x9cc9, 0x8d40, 0xbfdb, 0xae52, 0xdaed, 0xcb64, 0xf9ff, 0xe876,
  0x2102, 0x308b, 0x0210, 0x1399, 0x6726, 0x76af, 0x4434, 0x55bd,
  0xad4a, 0xbcc3, 0x8e58, 0x9fd1, 0xeb6e, 0xfae7, 0xc87c, 0xd9f5,
  0x3183, 0x200a, 0x1291, 0x0318, 0x77a7, 0x662e, 0x54b5, 0x453c,
  0xbdcb, 0xac42, 0x9ed9, 0x8f50, 0xfbef, 0xea66, 0xd8fd, 0xc974,
  0x4204, 0x538d, 0x6116, 0x709f, 0x0420, 0x15a9, 0x2732, 0x36b4,
  0xce4c, 0xdfc5, 0xed5e, 0xfcd7, 0x8868, 0x99e1, 0xab7a, 0xbaf3,
  0x5285, 0x430c, 0x7197, 0x601e, 0x14a1, 0x0528, 0x37b3, 0x263a,
  0xdecd, 0xcf44, 0xfddf, 0xec56, 0x98e9, 0x8960, 0xbbfb, 0xaa72,
  0x6306, 0x728f, 0x4014, 0x519d, 0x2522, 0x34ab, 0x0630, 0x17b9,
  0xef4e, 0xfec7, 0xcc5c, 0xddd5, 0xa96a, 0xb8e3, 0x8a78, 0x9bf1,
  0x7387, 0x620e, 0x5095, 0x411c, 0x35a3, 0x242a, 0x16b1, 0x0738,
  0xffcf, 0xee46, 0xdcdd, 0xcd54, 0xb9eb, 0xa862, 0x9af9, 0x8b70,
  0x8408, 0x9581, 0xa71a, 0xb693, 0xc22c, 0xd3a5, 0xe13e, 0xf0b7,
  0x0840, 0x19c9, 0x2b52, 0x3adb, 0x4e64, 0x5fed, 0x6d76, 0x7cff,
  0x9489, 0x8500, 0xb79b, 0xa612, 0xd2ad, 0xc324, 0xf1bf, 0xe036,
  0x18c1, 0x0948, 0x3bd3, 0x2a5a, 0x5ee5, 0x4f6c, 0x7df7, 0x6c7e,
  0xa50a, 0xb483, 0x8618, 0x9791, 0xe32e, 0xf2a7, 0xc03c, 0xd1b5,
  0x2942, 0x38cb, 0x0a50, 0x1bd9, 0x6f66, 0x7eef, 0x4c74, 0x5dfd,
  0xb58b, 0xa402, 0x9699, 0x8710, 0xf3af, 0xe226, 0xd0bd, 0xc134,
  0x39c3, 0x284a, 0x1ad1, 0x0b58, 0x7fe7, 0x6e6e, 0x5cf5, 0x4d7c,
  0xc60c, 0xd785, 0xe51e, 0xf497, 0x8028, 0x91a1, 0xa33a, 0xb2b3,
  0x4a44, 0x5bcd, 0x6956, 0x78df, 0x0c60, 0x1de9, 0x2f72, 0x3efb,
  0xd68d, 0xc704, 0xf59f, 0xe416, 0x90a9, 0x8120, 0xb3bb, 0xa232,
  0x5ac5, 0x4b4c, 0x79d7, 0x685e, 0x1ce1, 0x0d68, 0x3ff3, 0x2e7a,
  0xe70e, 0xf687, 0xc41c, 0xd595, 0xa12a, 0xb0a3, 0x8238, 0x93b1,
  0x6b46, 0x7acf, 0x4854, 0x59dd, 0x2d62, 0x3ceb, 0x0e70, 0x1ff9,
  0xf78f, 0xe606, 0xd49d, 0xc514, 0xb1ab, 0xa022, 0x92b9, 0x8330,
  0x7bc7, 0x6a4e, 0x58d5, 0x495c, 0x3de3, 0x2c6a, 0x1ef1, 0x0f78
};


// CRC-CCITT (0x1021 多项式, 初值 0), 与下位机 crc_ccitt.h 相同的算法
uint16_t crc_ccitt_calc(uint16_t crc, const uint8_t * buf, size_t len)
{
  while (len--) {
    crc = (crc >> 8) ^ crc_ccitt_table[(crc ^ *buf++) & 0xff];
  }
  return crc;
}







}  // namespace

class RobotBaseNode : public rclcpp::Node
{
public:
  RobotBaseNode() : Node("robot_base_node")
  {
    declare_parameter<std::string>("serial_port", "/dev/ttyUSB0");
    declare_parameter<int>("baudrate", 115200);
    declare_parameter<double>("send_rate", 50.0);
    declare_parameter<double>("max_vx", 2.0);
    declare_parameter<double>("max_vy", 2.0);
    declare_parameter<double>("max_wz", 3.0);

    serial_port_ = get_parameter("serial_port").as_string();
    baudrate_ = get_parameter("baudrate").as_int();
    send_rate_ = get_parameter("send_rate").as_double();
    max_vx_ = get_parameter("max_vx").as_double();
    max_vy_ = get_parameter("max_vy").as_double();
    max_wz_ = get_parameter("max_wz").as_double();

    if (!openSerial()) {
      RCLCPP_ERROR(get_logger(), "串口打开失败: %s (%s)", serial_port_.c_str(), strerror(errno));
    }

    sub_ = create_subscription<geometry_msgs::msg::Twist>(
      "/cmd_vel", 10,
      [this](const geometry_msgs::msg::Twist::SharedPtr msg) { last_twist_ = *msg; });

    // 定时发送:即使没新指令也持续发(下位机 200ms 超时急停,不能停发)
    auto period = std::chrono::milliseconds(static_cast<int64_t>(1000.0 / send_rate_));
    timer_ = create_wall_timer(period, [this]() { sendFrame(); });

    RCLCPP_INFO(get_logger(), "串口 %s @ %d baud, 发送频率 %.1f Hz",
                serial_port_.c_str(), baudrate_, send_rate_);
  }

  ~RobotBaseNode() override
  {
    if (fd_ >= 0) close(fd_);
  }

private:
  bool openSerial()
  {
    fd_ = ::open(serial_port_.c_str(), O_RDWR | O_NOCTTY | O_NDELAY);
    if (fd_ < 0) return false;

    termios tio{};
    tcgetattr(fd_, &tio);
    cfmakeraw(&tio);
    tio.c_cflag |= CLOCAL | CREAD;
    tio.c_cflag &= ~CRTSCTS;

    speed_t br;
    switch (baudrate_) {
      case 9600: br = B9600; break;
      case 19200: br = B19200; break;
      case 38400: br = B38400; break;
      case 57600: br = B57600; break;
      case 115200: br = B115200; break;
      case 230400: br = B230400; break;
      case 460800: br = B460800; break;
      case 921600: br = B921600; break;
      default: br = B115200; break;
    }
    cfsetispeed(&tio, br);
    cfsetospeed(&tio, br);
    tio.c_cc[VMIN] = 0;
    tio.c_cc[VTIME] = 1;
    tcsetattr(fd_, TCSANOW, &tio);

    tcflush(fd_, TCIOFLUSH);
    return true;
  }

  void sendFrame()
  {
    if (fd_ < 0) return;

    float vx = last_twist_.linear.x;
    float vy = last_twist_.linear.y;
    float wz = last_twist_.angular.z;

    // 限幅
    vx = clamp(vx, max_vx_);
    vy = clamp(vy, max_vy_);
    wz = clamp(wz, max_wz_);

    uint8_t frame[18];
    frame[0] = 0xAA;
    frame[1] = 0x55;
    std::memcpy(&frame[2], &vx, 4);
    std::memcpy(&frame[6], &vy, 4);
    std::memcpy(&frame[10], &wz, 4);
    uint16_t crc = crc_ccitt_calc(0, frame, 14);
    frame[14] = static_cast<uint8_t>(crc & 0xFF);
    frame[15] = static_cast<uint8_t>((crc >> 8) & 0xFF);
    frame[16] = 0x0D;
    frame[17] = 0x0A;

    ssize_t n = ::write(fd_, frame, sizeof(frame));
    if (n != static_cast<ssize_t>(sizeof(frame))) {
      RCLCPP_WARN_THROTTLE(get_logger(), *get_clock(), 2000,
                           "串口写入不完整: %zd/%zu", n, sizeof(frame));
    }
  }

  static float clamp(float v, double max_abs)
  {
    if (v > max_abs) return static_cast<float>(max_abs);
    if (v < -max_abs) return static_cast<float>(-max_abs);
    return v;
  }

  int fd_ = -1;
  std::string serial_port_;
  int baudrate_;
  double send_rate_;
  double max_vx_, max_vy_, max_wz_;
  geometry_msgs::msg::Twist last_twist_;
  rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<RobotBaseNode>());
  rclcpp::shutdown();
  return 0;
}
