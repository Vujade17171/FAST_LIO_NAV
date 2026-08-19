#include "usart.h"
#include "Unitree.h"
#include "crc_ccitt.h"
#include "stdio.h"
#include "dma.h"
#define SATURATE(_IN, _MIN, _MAX) {\
 if (_IN < _MIN)\
 _IN = _MIN;\
 else if (_IN > _MAX)\
 _IN = _MAX;\
 } 

MOTOR_send cmd;   //以全局变量声明电机控制结构体和电机数据结构体，方便在故障时通过debug查看变量值
MOTOR_recv data;


// 减速比6.33
int modify_data(MOTOR_send *motor_s)
{
    motor_s->hex_len = 17;
    motor_s->motor_send_data.head[0] = 0xFE;
    motor_s->motor_send_data.head[1] = 0xEE;
	
//		SATURATE(motor_s->id,   0,    15);
//		SATURATE(motor_s->mode, 0,    7);
		SATURATE(motor_s->K_P,  0.0f,   25.599f);
		SATURATE(motor_s->K_W,  0.0f,   25.599f);
		SATURATE(motor_s->T,   -127.99f,  127.99f);
		SATURATE(motor_s->W,   -804.00f,  804.00f);
		SATURATE(motor_s->Pos, -411774.0f,  411774.0f);

    motor_s->motor_send_data.mode.id   = motor_s->id;
    motor_s->motor_send_data.mode.status  = motor_s->mode;
    motor_s->motor_send_data.comd.k_pos  = motor_s->K_P/25.6f*32768;//关节刚度系数
    motor_s->motor_send_data.comd.k_spd  = motor_s->K_W/25.6f*32768;//关节速度系数
    motor_s->motor_send_data.comd.pos_des  = motor_s->Pos/6.2832f*32768;//期望关节位置（rad）
    motor_s->motor_send_data.comd.spd_des  = motor_s->W/6.2832f*256; //期望关节速度（电机本身的速度）(rad/s)
    motor_s->motor_send_data.comd.tor_des  = motor_s->T*256;//期望关节的输出力矩（电机本身的力矩）（Nm）
    motor_s->motor_send_data.CRC16 = crc_ccitt(0, (uint8_t *)&motor_s->motor_send_data, 15);
    return 0;
                                                 
}

int extract_data(MOTOR_recv *motor_r)
{
    if(motor_r->motor_recv_data.CRC16 !=
        crc_ccitt(0, (uint8_t *)&motor_r->motor_recv_data, 14)){
        // printf("[WARNING] Receive data CRC error");
        motor_r->correct = 0;
        return motor_r->correct;
    }
    else
		{
        motor_r->motor_id = motor_r->motor_recv_data.mode.id;
        motor_r->mode = motor_r->motor_recv_data.mode.status;
        motor_r->Temp = motor_r->motor_recv_data.fbk.temp;
        motor_r->MError = motor_r->motor_recv_data.fbk.MError;
        motor_r->W = ((float)motor_r->motor_recv_data.fbk.speed/256)*6.2832f ;
        motor_r->T = ((float)motor_r->motor_recv_data.fbk.torque) / 256;
        motor_r->Pos = 6.2832f*((float)motor_r->motor_recv_data.fbk.pos) / 32768;
				motor_r->footForce = motor_r->motor_recv_data.fbk.force;
				motor_r->correct = 1;
        return motor_r->correct;
    }
}

HAL_StatusTypeDef SERVO_Send_recv(MOTOR_send *pData, MOTOR_recv *rData)
{
    uint16_t rxlen = 0;

    modify_data(pData);
    
//		SET_485_DE_UP();
//		SET_485_RE_UP();
	HAL_UART_Transmit(&huart6, (uint8_t *)pData, sizeof(pData->motor_send_data),1); 
//	HAL_UART_Transmit_DMA(&huart6,(uint8_t *)pData, sizeof(pData->motor_send_data));

//		SET_485_RE_DOWN();
//		SET_485_DE_DOWN();
//    HAL_UARTEx_ReceiveToIdle(&huart6, (uint8_t *)rData, sizeof(rData->motor_recv_data), &rxlen, 10);
//	HAL_UART_Receive(&huart6, (uint8_t *)rData, sizeof(rData->motor_recv_data),1);
	HAL_UART_Receive_DMA(&huart6,(uint8_t *)rData,sizeof(rData->motor_recv_data));
    if(rxlen == 0)

      return HAL_TIMEOUT;

    if(rxlen != sizeof(rData->motor_recv_data))
			return HAL_ERROR;

    uint8_t *rp = (uint8_t *)&rData->motor_recv_data;
    if(rp[0] == 0xFE && rp[1] == 0xEE)
    {
        rData->correct = 1;
        extract_data(rData);
        return HAL_OK;
    }
    
    return HAL_ERROR;
}
//一圈 32768  
//rad   rad/s
void GO_Control(MOTOR_send *pData, MOTOR_recv *rData,float speed,float pos,float Kp,float kw)
{
	cmd.id=0; 			//给电机控制指令结构体赋值
	cmd.mode=1;
	cmd.T=0;
	cmd.W=speed;
	cmd.Pos=pos;
	cmd.K_P=Kp;
	cmd.K_W=kw;
	SERVO_Send_recv(pData, rData);	//将控制指令发送给电机，同时接收返回值
}


void GO_pos_mode(MOTOR_send *pData, MOTOR_recv *rData,float pos,float Kp,float kw)
{
	cmd.id=0; 			//给电机控制指令结构体赋值
	cmd.mode=1;
	cmd.T=0.0;
	cmd.W=0.0;
	cmd.Pos=pos;
	cmd.K_P=Kp;
	cmd.K_W=kw;
	SERVO_Send_recv(pData, rData);	//将控制指令发送给电机，同时接收返回值
}

void GO_speed_mode(MOTOR_send *pData, MOTOR_recv *rData,float speed,float kw)
{
	cmd.id=0; 			//给电机控制指令结构体赋值
	cmd.mode=1;
	cmd.T=0.0;
	cmd.W=speed;
	cmd.Pos=0.0;
	cmd.K_P=0.0;
	cmd.K_W=kw;
	SERVO_Send_recv(pData, rData);	//将控制指令发送给电机，同时接收返回值
}

void GO_speed_modeid(MOTOR_send *pData, MOTOR_recv *rData,float speed,float kw,uint16_t id)
{
	cmd.id=id; 			//给电机控制指令结构体赋值
	cmd.mode=1;
	cmd.T=0.0;
	cmd.W=speed;
	cmd.Pos=0.0;
	cmd.K_P=0.0;
	cmd.K_W=kw;
	SERVO_Send_recv(pData, rData);	//将控制指令发送给电机，同时接收返回值
}

void GO_stop(void)
{
	GO_speed_mode(&cmd,&data,0.0f,0.0f);//输出轴单位为rad/s
}
