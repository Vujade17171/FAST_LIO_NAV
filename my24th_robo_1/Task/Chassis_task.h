#ifndef __CHASSIS_TASK_H
#define __CHASSIS_TASK_H

#include "FreeRTOS.h"
#include "cmsis_os.h"
#include "can.h"
#include "dma.h"
#include "usart.h"
#include "gpio.h"
#include "bsp_can.h"
#include "remote_control.h"
#include "bsp_rc.h"
#include "PID.h"
#include "math.h"
#include "user_lib.h"

//周长，单位是米
#define WHEEL_PERIMETER			0.29202f
//减速比
#define M3508_RATIO					101.0f/17.0f
//线速度m/s = 电机转速(rpm)*轮子周长 / (60*减速比) 
#define wheel_rpm_ratio			60.0f * (1+M3508_RATIO) / WHEEL_PERIMETER
//中心到舵的距离
#define Radius		0.29f

//舵轮偏置点====
#define M6020_HE_ANGLE 4181.0f
#define M6020_BL_ANGLE 2048.0f
#define M6020_BR_ANGLE 3515.0f

//底盘电机速度环
#define M3508_SPEED_PID_KP        12.0f 
#define M3508_SPEED_PID_KI        0.2f     
#define M3508_SPEED_PID_KD        0.0f//5.5f
#define M3508_SPEED_PID_MAX_OUT		16384.0f
#define M3508_SPEED_PID_MAX_IOUT  4000.0f

//转向电机 速度环 
#define GIMBAL_SPEED_KP 8.0f
#define GIMBAL_SPEED_KI 0.1f
#define GIMBAL_SPEED_KD 0.0f
#define GIMBAL_SPEED_I_LIMIT 4000.f
#define GIMBAL_SPEED_MAX 25000.f

//转向电机 角度环 
#define GIMBAL_ANGLE_KP 4.0f
#define GIMBAL_ANGLE_KI 0.0f
#define GIMBAL_ANGLE_KD 3.0f
#define GIMBAL_ANGLE_I_LIMIT 3000.f
#define GIMBAL_ANGLE_MAX 8192.f

//右轮舵向电机单独角度环
#define GIMBAL_ANGLE_R_KP 2.0f
#define GIMBAL_ANGLE_R_KI 0.0f
#define GIMBAL_ANGLE_R_KD 0.0f



//电机数组数据宏定义
#define AGV_3508_data_head		Motor_measure[0]
#define AGV_3508_data_left    Motor_measure[1]
#define AGV_3508_data_right   Motor_measure[2]
#define AGV_6020_data_head    Motor_measure[5]
#define AGV_6020_data_left   Motor_measure[7]
#define AGV_6020_data_right    Motor_measure[4]

#define CHASSIS_MODE rc_ctrl.rc.s[1]

typedef struct{
	float vx;
	float	vy;
	float wz;
	
	
}Speedcmd;

extern Speedcmd speed_cmd;   /* 导航/遥控写入底盘速度指令 */






typedef struct{
	float Vx;
	float Vy;
	float Wz;
	float Last_Vx;
	float Last_Vy;
	float Last_Wz;
}Remove_data;


void filter_remote(float *value);
void Chassis_control(Remove_data *data);
void Chassis_manual_control(Remove_data *data);
void chassis_pid_init(void);
void chassis_calc_cmd(float Vx,float Vy,float Wz);
void chassis_vector_to_M3508_wheel_speed(float vx_set, float vy_set, float wz_set, float wheel_speed[3]);
void chassis_vector_to_M6020_wheel_angle(float vx_set, float vy_set, float wz_set, float wheel_angle[3]);


#endif
