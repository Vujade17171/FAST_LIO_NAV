#include "Chassis_task.h"
#include "nav_receiver.h"
#include "stdio.h"

#define COS30		0.866025f
#define SIN30		0.5f

extern motor_measure Motor_measure[8];
extern RC_ctrl_t rc_ctrl;
Remove_data remove_chassis_data;


//小电脑结构体
Speedcmd speed_cmd;

////遥控器控制，加了死去
//void Chassis_control(Remove_data *data,float Vx,float Vy,float Wz){
//	double ch0 = rc_ctrl.rc.ch[0];
//	double ch2 = rc_ctrl.rc.ch[2];
//	double ch3 = rc_ctrl.rc.ch[3];

//	//通道死区：±10以内当0（滤掉摇杆中位抖动）
//	if (ch0 > -10 && ch0 < 10) ch0 = 0;
//	if (ch2 > -10 && ch2 < 10) ch2 = 0;
//	if (ch3 > -10 && ch3 < 10) ch3 = 0;

//	data->Vx = ch3 / 660.0 * Vx;
//	data->Vy = ch2 / 660.0 * Vy;
//	data->Wz = ch0 / 660.0 * Wz;

//}

//小电脑给的速度
void Chassis_control(Remove_data *data){
	data->Vx = speed_cmd.vx;
	data->Vy = speed_cmd.vy;
	data->Wz = speed_cmd.wz;
	
	
	
}




//pid结构体
pid_t	pid_wheel_angle[3];	//6020角度环
pid_t pid_wheel_speed[3];	//6020速度环
pid_t pid_wheel_rpm[3];		//底盘3508速度环

void chassis_pid_init(void){
	//前轮舵向电机角度环
	PID_Init(&pid_wheel_angle[0],GIMBAL_ANGLE_KP,GIMBAL_ANGLE_KI,GIMBAL_ANGLE_KD,GIMBAL_ANGLE_MAX,GIMBAL_ANGLE_I_LIMIT,2.0f);
	//前轮舵向电机速度环
	PID_Init(&pid_wheel_speed[0], GIMBAL_SPEED_KP, GIMBAL_SPEED_KI, GIMBAL_SPEED_KD, GIMBAL_SPEED_MAX, GIMBAL_SPEED_I_LIMIT, 0.0f);
	//前轮轮向电机速度环
	PID_Init(&pid_wheel_rpm[0], M3508_SPEED_PID_KP, M3508_SPEED_PID_KI, M3508_SPEED_PID_KD, M3508_SPEED_PID_MAX_OUT, M3508_SPEED_PID_MAX_IOUT, 0.0f);
	
	//左轮舵向电机角度环
	PID_Init(&pid_wheel_angle[1], GIMBAL_ANGLE_KP, GIMBAL_ANGLE_KI, GIMBAL_ANGLE_KD, GIMBAL_ANGLE_MAX, GIMBAL_ANGLE_I_LIMIT, 2.0f);
	//左轮舵向电机速度环
	PID_Init(&pid_wheel_speed[1], GIMBAL_SPEED_KP, GIMBAL_SPEED_KI, GIMBAL_SPEED_KD, GIMBAL_SPEED_MAX, GIMBAL_SPEED_I_LIMIT, 0.0f);
	//左轮轮向电机速度环
	PID_Init(&pid_wheel_rpm[1], M3508_SPEED_PID_KP, M3508_SPEED_PID_KI, M3508_SPEED_PID_KD, M3508_SPEED_PID_MAX_OUT, M3508_SPEED_PID_MAX_IOUT, 0.0f);

	//右轮舵向电机角度环
	PID_Init(&pid_wheel_angle[2], GIMBAL_ANGLE_KP, GIMBAL_ANGLE_KI, GIMBAL_ANGLE_KD, GIMBAL_ANGLE_MAX, GIMBAL_ANGLE_I_LIMIT, 2.0f);
	//右轮舵向电机速度环
	PID_Init(&pid_wheel_speed[2], GIMBAL_SPEED_KP, GIMBAL_SPEED_KI, GIMBAL_SPEED_KD, GIMBAL_SPEED_MAX, GIMBAL_SPEED_I_LIMIT, 0.0f);
	//右轮轮向电机速度环
	PID_Init(&pid_wheel_rpm[2], M3508_SPEED_PID_KP, M3508_SPEED_PID_KI, M3508_SPEED_PID_KD, M3508_SPEED_PID_MAX_OUT, M3508_SPEED_PID_MAX_IOUT, 0.0f);
	
}


////手动控制
//float pre_vx[2];
//float pre_vy[2];
void Chassis_manual_control(Remove_data *data){
	Chassis_control(data);
	
//	//遥控器滤波
//	filter_remote(&data->Vx);
//  filter_remote(&data->Vy);
//  filter_remote(&data->Wz);
//	
//	pre_vx[1]=fabs(data->Last_Vx);
//	pre_vx[0]=fabs(data->Vx);
//	
//	pre_vy[1]=fabs(data->Last_Vy);
//	pre_vy[0]=fabs(data->Vy);
//	
//	//判断是否减速，减速就开始平滑
//	if(Deceleration_judgment(pre_vx[0],pre_vx[1])==1 || Deceleration_judgment(pre_vy[0],pre_vy[1])==1){
//		//这里调整遥控器平滑系数，越大停的越快
//		data->Vx = RAMP_float(data->Vx, data->Last_Vx, 0.002f);
//		data->Vy = RAMP_float(data->Vy, data->Last_Vy, 0.002f);
//	}
//	data->Last_Vx = data->Vx;
//	data->Last_Vy = data->Vy;
	
	chassis_calc_cmd(data->Vx,data->Vy,data->Wz);
}

int8_t dirt[3] = {1,1,1};
//3508电机速度解算
void chassis_vector_to_M3508_wheel_speed(float vx_set, float vy_set, float wz_set, float wheel_speed[3]){
	//前电机
	wheel_speed[0] = dirt[0] * sqrt(pow(vx_set,2) + pow(vy_set + wz_set*Radius,2)) * wheel_rpm_ratio;
	//左电机
	wheel_speed[1] = dirt[1] * sqrt(pow(vx_set + wz_set * Radius * COS30,2) + pow(vy_set - wz_set * Radius * SIN30,2) ) * wheel_rpm_ratio;
	//右电机
	wheel_speed[2] = dirt[2] * sqrt(pow(vx_set - wz_set * Radius * COS30,2) + pow(vy_set - wz_set * Radius * SIN30,2)) * wheel_rpm_ratio;
}

//舵轮的角度
double atan_angle[3];
float Wheel_angle[3];

void chassis_vector_to_M6020_wheel_angle(float vx_set,float vy_set,float wz_set,float wheel_angle[3]){
	//根据给定速度算出需要旋转的角度
	if(!(vx_set == 0 && vy_set == 0 && wz_set == 0)){
		//将弧度制转换为角度制
		atan_angle[0] = -atan2((vy_set + wz_set * Radius),vx_set) * 180.0f / PI;
		atan_angle[1] = -atan2((vy_set - wz_set * Radius * SIN30),(vx_set + wz_set * Radius * COS30)) * 180.0f / PI;
		atan_angle[2] = -atan2((vy_set - wz_set * Radius * SIN30),(vx_set - wz_set * Radius * COS30)) * 180.0f / PI;
		
		//范围归一化
		//0-8192
		wheel_angle[0] = Angle_Limit( ( M6020_HE_ANGLE - (float)(atan_angle[0] * 22.75f) ) ,8192.0f );
		wheel_angle[1] = Angle_Limit( ( M6020_BL_ANGLE - (float)(atan_angle[1] * 22.75f) ) ,8192.0f );
		wheel_angle[2] = Angle_Limit( ( M6020_BR_ANGLE - (float)(atan_angle[2] * 22.75f) ), 8192.0f );
		
		Wheel_angle[0] = wheel_angle[0];
		Wheel_angle[1] = wheel_angle[1];
		Wheel_angle[2] = wheel_angle[2];
		//判断最短路径和方向
		//前轮
		if(wheel_angle[0] - (float)AGV_6020_data_head.ecd > 2048 ){
			dirt[0] = 1; //轮方向
			wheel_angle[0] = Angle_Limit(wheel_angle[0] - 4096, 8192.0f);
		}
		else if(wheel_angle[0] - (float)AGV_6020_data_head.ecd < -2048 ){
			dirt[0] = 1;
			wheel_angle[0] = Angle_Limit(wheel_angle[0] + 4096, 8192.0f);
		}
		else{
			dirt[0] = -1;
		}
		//左轮
		if(  wheel_angle[1]-  (float)AGV_6020_data_left.ecd  > 2048 )
	 {
		dirt[1] = 1;
		wheel_angle[1] = Angle_Limit( wheel_angle[1] - 4096, 8192.f );
	 }
	 else if(  wheel_angle[1] - (float)AGV_6020_data_left.ecd < -2048)
	 {
		dirt[1] = 1;
		wheel_angle[1] = Angle_Limit( wheel_angle[1] + 4096, 8192.f );
	 }
	 else{
		 dirt[1] = -1;
	 }
	 //右轮
	 if(  wheel_angle[2]-  (float)AGV_6020_data_right.ecd  > 2048 )
	 {
		dirt[2] = 1;
		wheel_angle[2] = Angle_Limit( wheel_angle[2] - 4096, 8192.f );
	 }
	 else if(  wheel_angle[2] - (float)AGV_6020_data_right.ecd < -2048)
	 {
		dirt[2] = 1;
		wheel_angle[2] = Angle_Limit( wheel_angle[2] + 4096, 8192.f );
	 }
	 else{
		 dirt[2] = -1;
	 }
	 
	 wheel_angle[0] = (int)wheel_angle[0];
	 wheel_angle[1] = (int)wheel_angle[1];
	 wheel_angle[2] = (int)wheel_angle[2];
	}
}


//计算三个舵轮的转向角度和轮向电机转速
float M3508_SPEED[3],M6020_ANGLE[3];
void chassis_calc_cmd(float Vx,float Vy,float Wz){
	chassis_vector_to_M3508_wheel_speed(Vx,Vy,Wz,M3508_SPEED);
	chassis_vector_to_M6020_wheel_angle(Vx,Vy,Wz,M6020_ANGLE);
	
	//舵向角度环
	PID_Calculate_ECD(&pid_wheel_angle[0],Motor_measure[5].ecd,M6020_ANGLE[0],8192);
	PID_Calculate_ECD(&pid_wheel_angle[1],Motor_measure[7].ecd,M6020_ANGLE[1],8192);
	PID_Calculate_ECD(&pid_wheel_angle[2],Motor_measure[4].ecd,M6020_ANGLE[2],8192);
	//舵向速度环
	PID_Calculate(&pid_wheel_speed[0],Motor_measure[5].speed_rpm,pid_wheel_angle[0].Output);
	PID_Calculate(&pid_wheel_speed[1],Motor_measure[7].speed_rpm,pid_wheel_angle[1].Output);
	PID_Calculate(&pid_wheel_speed[2],Motor_measure[4].speed_rpm,pid_wheel_angle[2].Output);
	//轮向速度环
	PID_Calculate(&pid_wheel_rpm[0],Motor_measure[0].speed_rpm,M3508_SPEED[0]);
	PID_Calculate(&pid_wheel_rpm[1],Motor_measure[1].speed_rpm,M3508_SPEED[1]);
	PID_Calculate(&pid_wheel_rpm[2],Motor_measure[2].speed_rpm,M3508_SPEED[2]);
	
	
	//发送数据
	can_cmd_motor(&hcan1,0x200,pid_wheel_rpm[0].Output,pid_wheel_rpm[1].Output,pid_wheel_rpm[2].Output,0);
	can_cmd_motor(&hcan1,0x1FF,pid_wheel_speed[2].Output,pid_wheel_speed[0].Output,0,pid_wheel_speed[1].Output);
	
}

//底盘任务
void Chassis_task(void const * argument){
	//can初始化
	can_filter_init();
//	//遥控器初始化
//	remote_control_init();
	//设置pid参数
	chassis_pid_init();
	Nav_Receiver_Init();   //启动串口1
	for(;;){
		Nav_Receiver_Check();   //看门狗
		
		Chassis_manual_control(&remove_chassis_data);
		
		osDelay(1);
		
	}
}


////==========调试代码3508=========
//void Chassis_task(void const * argument){
//	//can初始化
//	can_filter_init();
//	//遥控器初始化
//	remote_control_init();
//	//设置pid参数
//	chassis_pid_init();
//	for(;;){
//		Chassis_manual_control(&remove_chassis_data,2,2,2);
//		osDelay(1);
//		
////		//调试3508速度环
////		//每10ms打印一次
////		static uint32_t cnt = 0;
////		if(++cnt >= 10){
////			cnt = 0;
////			printf("%.1f, %.1f\r\n",M3508_SPEED[0],(float)Motor_measure[0].speed_rpm);
////		}
//		
//	}
//}


////=========调试代码6020速度环========
// //6020 速度环单独测试
//void test_6020_speed(void)
//{
//    // 只调右轮（Motor_measure[5]）速度环
//    PID_Calculate(&pid_wheel_speed[2],
//                  Motor_measure[4].speed_rpm,   // 实际转速（反馈）
//                  100.0f);                      // 目标转速 100 RPM（先给个小的）

//    // 把速度环输出发给前轮 6020
//    can_cmd_motor(&hcan1, 0x1FF,
//                  pid_wheel_speed[2].Output,   // 0x205 右
//                  pid_wheel_speed[0].Output,   // 0x206 前
//                  0,                           // 0x207 空
//                  pid_wheel_speed[1].Output);  // 0x208 左
//}

//void Chassis_task(void const * argument){
//	can_filter_init();
//	remote_control_init();
//	chassis_pid_init();
//	for(;;){
//		test_6020_speed();  


//		static uint32_t cnt = 0;
//		if (++cnt >= 10){
//			cnt = 0;
//			printf("target:100 actual:%.1f \r\n",
//						 (float)Motor_measure[4].speed_rpm);
//		}

//		osDelay(1);
//	}
//}


////=========调试代码6020角度环========
//// 6020 角度环测试（含速度环）
//void test_6020_angle(void)
//{
//    //给前轮一个固定目标角度
//    float target_angle = 4096.0f;

//    //角度环
//    PID_Calculate_ECD(&pid_wheel_angle[2],
//                      Motor_measure[4].ecd,   // 实际编码器角
//                      target_angle,           // 目标角
//                      8192);                  // 编码器范围

//    //速度环角度环输出作为目标转速）
//    PID_Calculate(&pid_wheel_speed[2],
//                  Motor_measure[4].speed_rpm,
//                  pid_wheel_angle[2].Output);

//    //发送
//    can_cmd_motor(&hcan1, 0x1FF,
//                  pid_wheel_speed[2].Output,
//                  pid_wheel_speed[0].Output,
//                  0,
//                  pid_wheel_speed[1].Output);
//}

//void Chassis_task(void const * argument){
//	can_filter_init();
//	remote_control_init();
//	chassis_pid_init();
//	for(;;){
//		test_6020_angle();

//    static uint32_t cnt = 0;
//		if(++cnt >= 10){
//			cnt=0;
//			printf("target:%.1f actual:%.1f\r\n",
//				 (float)4096,
//				 (float)Motor_measure[4].ecd);
//		 }

//		osDelay(1);
//	}
//}


////测量舵轮偏置点
//void Chassis_task(void const * argument){
//	can_filter_init();          //只初始化 CAN（收编码器反馈）
//	remote_control_init();
//	// chassis_pid_init(); 

//	for(;;){
//		// 周期性发 0 控制帧，让 3508 和 6020 保持"无力"，可以手动转
//		can_cmd_motor(&hcan1, 0x200, 0, 0, 0, 0);   // 3508 给 0 电流 = 无力
//		can_cmd_motor(&hcan1, 0x1FF, 0, 0, 0, 0);   // 6020 给 0 电压 = 无力

//		// 打印三个 6020 编码器值（每 10ms 一次）
//		static uint32_t cnt = 0;
//		if(++cnt >= 10){
//			cnt = 0;
//			printf("head_ecd=%d left_ecd=%d right_ecd=%d\r\n",
//		+	       Motor_measure[5].ecd,   // 前轮 6020
//			       Motor_measure[7].ecd,   // 左轮 6020
//			       Motor_measure[4].ecd);  // 右轮 6020
//		}
//		osDelay(1);
//	}
//}



