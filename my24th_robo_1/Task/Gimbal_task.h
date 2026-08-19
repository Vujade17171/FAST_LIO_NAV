#ifndef __GIMBAL_TASK_H
#define __GIMBAL_TASK_H

#include "Chassis_task.h"
#include "dm_imu.h"
#include "Unitree.h"


/*零点*/
#define PTZ_ANGLE_offset 	(91.8521194f)
/*减速比*/
#define GO_RATIO 	 		(3.5f)			
/*云台一圈的编码值*/
#define PTZ_ONE_LOOP 	 	(GO_RATIO*360.f)	
/*多圈编码值*/
#define PTZ_ECD_MAX 		(99.0f*360.f)
/*编码器精度*/
#define ENCODER_RESOLUTION 	(32768.0f)
/*抬升齿轮半径*/
#define HEIGHT_RADIUS 		(20.295f)
/*伸展齿轮半径*/
#define DISTANCE_RADIUS 	(20.63f)


//云台电机 速度环 
#define PTZ_SPEED_KP 2.0f
#define PTZ_SPEED_KI 0.0f
#define PTZ_SPEED_KD 0.1f
#define PTZ_SPEED_I_LIMIT 3000.0f
#define PTZ_SPEED_MAX 2000.0f
//云台电机 角度环 
#define PTZ_ANGLE_KP 0.8f
#define PTZ_ANGLE_KI 0.0f
#define PTZ_ANGLE_KD 1.0f
#define PTZ_ANGLE_I_LIMIT 0.001f
#define PTZ_ANGLE_MAX  	(3.14f*6.33f*1.8f)//29.81f

typedef struct
{
	float distance;	 	//距离		毫米
	float height;		//高度		毫米
	float yaw; 			//偏航角 	360度
	float yaw_radian; 	//偏航角 	6.28
}gimbal_data_t; 		//云台数据


static void pid_gimbal_init(void);

#endif
