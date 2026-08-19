#include "Gimbal_task.h"

//遥控器结构体
extern RC_ctrl_t rc_ctrl;
extern Remove_data remove_gimbal_data;

//pid结构体
PID_t pid_speed_PTZ;	//云台电机速度环
PID_t pid_angle_PTZ;		//云台电机位置环

extern MOTOR_send cmd;
extern MOTOR_recv data;

float PTZ_angle_ecd;	//编码器数值
gimbal_data_t gimbal_data;//云台数据

extern imu_t imu;

static void pid_gimbal_init(void){
	//速度环
	PID_Init(&pid_speed_PTZ,PTZ_SPEED_MAX,PTZ_SPEED_I_LIMIT,0.0f,PTZ_SPEED_KP,PTZ_SPEED_KI,PTZ_SPEED_KD,256.0f,512.0f,0.0000001f,0.0000001f,2,Integral_Limit);
	
	//位置环
	PID_Init(&pid_angle_PTZ,PTZ_ANGLE_MAX,PTZ_ANGLE_I_LIMIT,1.0f,PTZ_ANGLE_KP,PTZ_ANGLE_KI,PTZ_ANGLE_KD,256.0f,512.0f,0.0000001f,0.0000001f,2,Integral_Limit);
	
}

void Gimbal_task(void const * argument){
	can_filter_init();
	remote_control_init();
	pid_gimbal_init();
	
	for(;;){
		GO_pos_mode(&cmd,&data,0,0,0.2);
		osDelay(1);
	}
}













