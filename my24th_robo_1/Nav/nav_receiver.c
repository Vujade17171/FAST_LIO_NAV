#include "nav_receiver.h"
#include "crc_ccitt.h"
#include "Chassis_task.h"
#include <string.h>

extern Speedcmd speed_cmd;  

static uint8_t  rx_byte;
static uint8_t  buf[NAV_FRAME_LEN];
static uint8_t  rx_state = 0;              /* 状态机: 0等帧头1  1等帧头2  2..收数据 */
static volatile uint32_t last_valid_tick = 0;
static uint8_t  nav_mode = 0;

/* 启动 USART1 单字节中断接收 */
void Nav_Receiver_Init(void)
{
    rx_state = 0;
    nav_mode = 0;
    HAL_UART_Receive_IT(&huart1, &rx_byte, 1);
}

/* 校验并应用一帧速度指令 */
static void Nav_ParseFrame(uint8_t *f)
{
    uint16_t crc_calc, crc_recv;
    float vx, vy, wz;

    if (f[0] != NAV_HEAD0 || f[1] != NAV_HEAD1) return;
    if (f[16] != NAV_TAIL0 || f[17] != NAV_TAIL1) return;

    crc_calc = crc_ccitt(0, f, 14);
    crc_recv = (uint16_t)(f[14] | (f[15] << 8));
    if (crc_calc != crc_recv) return;

    memcpy(&vx, &f[2], 4);
    memcpy(&vy, &f[6], 4);
    memcpy(&wz, &f[10], 4);

    /* 限幅,防异常指令 */
    if (vx >  NAV_VX_MAX) vx =  NAV_VX_MAX;
    if (vx < -NAV_VX_MAX) vx = -NAV_VX_MAX;
    if (vy >  NAV_VY_MAX) vy =  NAV_VY_MAX;
    if (vy < -NAV_VY_MAX) vy = -NAV_VY_MAX;
    if (wz >  NAV_WZ_MAX) wz =  NAV_WZ_MAX;
    if (wz < -NAV_WZ_MAX) wz = -NAV_WZ_MAX;

    speed_cmd.vx = vx;
    speed_cmd.vy = vy;
    speed_cmd.wz = wz;
    last_valid_tick = HAL_GetTick();
    nav_mode = 1;
}

/* USART1 每收到 1 字节,该回调被 HAL 调用 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if (huart->Instance != USART1)
        return;

    switch (rx_state)
    {
    case 0:
        if (rx_byte == NAV_HEAD0) { buf[0] = rx_byte; rx_state = 1; }
        break;
    case 1:
        if (rx_byte == NAV_HEAD1) { buf[1] = rx_byte; rx_state = 2; }
        else                       rx_state = 0;
        break;
    default:                      /* 2..17: 收剩余数据 */
        buf[rx_state] = rx_byte;
        rx_state++;
        if (rx_state >= NAV_FRAME_LEN)
        {
            Nav_ParseFrame(buf);
            rx_state = 0;
        }
        break;
    }

    HAL_UART_Receive_IT(&huart1, &rx_byte, 1);
}

/* 通信超时看门狗:在 Chassis_task 每 1ms 调用 */
void Nav_Receiver_Check(void)
{
    if (nav_mode && (HAL_GetTick() - last_valid_tick) > NAV_CMD_TIMEOUT_MS)
    {
        speed_cmd.vx = 0.0f;
        speed_cmd.vy = 0.0f;
        speed_cmd.wz = 0.0f;
        nav_mode = 0;
    }
}

uint8_t Nav_GetMode(void)
{
    return nav_mode;
}
