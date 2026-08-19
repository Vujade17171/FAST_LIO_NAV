#include "bsp_can.h"
#include "main.h"
#include <stdlib.h>

/*can结构体*/
extern CAN_HandleTypeDef hcan;
extern CAN_HandleTypeDef hcan1;
extern CAN_HandleTypeDef hcan2;
CAN_TxHeaderTypeDef Can_Tx_message;
CAN_RxHeaderTypeDef Rx_header;
/*电机结构体*/
motor_measure Motor_measure[8];

uint8_t Send_data[8];
uint8_t RX_data[8];

#define Motor_measure_get(ptr, data)                                    \
    {                                                                   \
        (ptr)->last_ecd = (ptr)->ecd;                                   \
        (ptr)->ecd = (uint16_t)((data)[0] << 8 | (data)[1]);            \
        (ptr)->speed_rpm = (uint16_t)((data)[2] << 8 | (data)[3]);      \
        (ptr)->given_current = (uint16_t)((data)[4] << 8 | (data)[5]);  \
        (ptr)->temperate = (data)[6];                                   \
    }	

void can_filter_init(void)
{
	CAN_FilterTypeDef can_filter_st;																			  //定义过滤器结构体
    can_filter_st.FilterActivation = ENABLE;															//ENABLE使能过滤器
    can_filter_st.FilterMode = CAN_FILTERMODE_IDMASK;											//设置过滤器模式--标识符屏蔽位模式
    can_filter_st.FilterScale = CAN_FILTERSCALE_32BIT;										//过滤器的位宽 32 位
    can_filter_st.FilterIdHigh = 0x0000;																	//ID高位
    can_filter_st.FilterIdLow = 0x0000;																		//ID低位
    can_filter_st.FilterMaskIdHigh = 0x0000;															//过滤器掩码高位
    can_filter_st.FilterMaskIdLow = 0x0000;																//过滤器掩码低位
    can_filter_st.FilterBank = 0;																					//过滤器组-双CAN可指定0~27
    can_filter_st.FilterFIFOAssignment = CAN_RX_FIFO0;										//与过滤器组管理的 FIFO
    HAL_CAN_ConfigFilter(&hcan1, &can_filter_st);													//HAL库配置过滤器函数
    HAL_CAN_Start(&hcan1);																								//使能CAN控制器
    HAL_CAN_ActivateNotification(&hcan1, CAN_IT_RX_FIFO0_MSG_PENDING);		//使能CAN的各种中断


    can_filter_st.SlaveStartFilterBank = 14;															//双CAN模式下规定CAN的主从模式的过滤器分配，从过滤器为14
    can_filter_st.FilterBank = 14;																				//过滤器组-双CAN可指定0~27
    HAL_CAN_ConfigFilter(&hcan2, &can_filter_st);													//HAL库配置过滤器函数
    HAL_CAN_Start(&hcan2);																								//使能CAN控制器
    HAL_CAN_ActivateNotification(&hcan2, CAN_IT_RX_FIFO0_MSG_PENDING);		//使能CAN的各种中断
}


void can_cmd_motor(CAN_HandleTypeDef *hcan,uint32_t StdId,int16_t motor1,int16_t motor2,int16_t motor3,int16_t motor4 )
{
	uint32_t send_mail_box;                                                   //定义一个变量用于存储发送邮箱编号      
	Can_Tx_message.StdId = StdId;	                                            //标识符，形参数据存入发送的数据包
	Can_Tx_message.ExtId=0;
	Can_Tx_message.IDE = CAN_ID_STD;                                          //标识符选择位，STD-标准帧
	Can_Tx_message.RTR=CAN_RTR_DATA;	  																			//定义帧类型
	Can_Tx_message.DLC=0x08;                                                  //数据帧长度为8位
	Send_data[0]=motor1>>8;                                                        //依次将要发送的数据移入数据数组，下同
	Send_data[1]=motor1;
	Send_data[2]=motor2>>8;
	Send_data[3]=motor2;
	Send_data[4]=motor3>>8;
	Send_data[5]=motor3;
	Send_data[6]=motor4>>8;
	Send_data[7]=motor4;
	
	HAL_CAN_AddTxMessage(hcan,&Can_Tx_message,Send_data,&send_mail_box);            //hal库can发送函数：该函数用于向发送邮箱；添加发送报文，并激活发送请求
}
void HAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef *hcan)
{	
		if(HAL_CAN_GetRxMessage(&hcan1, CAN_RX_FIFO0, &Rx_header, RX_data) == HAL_OK)
		{
			if(hcan->Instance == CAN1)
			{
				int idx = -1;
				switch(Rx_header.StdId)
				{		
					case CAN1_3508_ID1: idx = 0; break;//[0]前轮
					case CAN1_3508_ID2:	idx = 1; break;//[1]  左轮 
					case CAN1_3508_ID3:	idx = 2; break;//[2]  右轮 
					case CAN1_6020_ID1:	idx = 4; break;//[4]  右轮
					case CAN1_6020_ID2:	idx = 5; break;//[5]  前轮 
					case CAN1_6020_ID4:	idx = 7; break;//[7]  左轮 
					default:return;
				}
				Motor_measure_get(&Motor_measure[idx], RX_data);
			}
		}
}
