#ifndef bsp_can_h
#define bsp_can_h
#include "main.h"
#include "stdint.h"
void can_filter_init(void);

/* µç»úID */
typedef enum{
	// 0x200 201-203
	CAN1_3508_ID1  = 0x201,
	CAN1_3508_ID2  = 0x202,
	CAN1_3508_ID3  = 0x203,
	CAN1_3508_ID4  = 0x204,
}CAN_ID_3508;

typedef enum{
  //0x1FF 205-207
	
	CAN1_6020_ID1  = 0x205,
	CAN1_6020_ID2  = 0x206,
	CAN1_6020_ID3  = 0x207,
	CAN1_6020_ID4  = 0x208,
}CAN_ID_6020;

typedef struct 
{
    uint16_t ecd;
    int16_t speed_rpm;
    int16_t given_current;
    uint8_t temperate;
    int16_t last_ecd;
}motor_measure;

void can_filter_init(void);
void can_cmd_motor(CAN_HandleTypeDef *hcan,uint32_t StdId,int16_t motor1,int16_t motor2,int16_t motor3,int16_t motor4 );
//void Motor_measure_get(motor_measure *ptr,uint8_t* RX_buffer);
#endif
