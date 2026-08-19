#ifndef __NAV_RECEIVER_H
#define __NAV_RECEIVER_H

#include "usart.h"

/* 帧格式: AA 55 | vx(4B) | vy(4B) | wz(4B) | crc16(2B) | 0D 0A */
#define NAV_HEAD0          0xAA
#define NAV_HEAD1          0x55
#define NAV_TAIL0          0x0D
#define NAV_TAIL1          0x0A
#define NAV_FRAME_LEN      18

/* 超时急停:超过该时间没收到新指令,速度清零 */
#define NAV_CMD_TIMEOUT_MS 200

/* 速度限幅(单位: m/s, rad/s) */
#define NAV_VX_MAX         2.0f
#define NAV_VY_MAX         2.0f
#define NAV_WZ_MAX         3.0f

void  Nav_Receiver_Init(void);   /* 在 Chassis_task 开头调用,启动接收 */
void  Nav_Receiver_Check(void);  /* 在 Chassis_task 循环里调用,超时清零 */
uint8_t Nav_GetMode(void);       /* 1=导航模式, 0=手动/失联 */

#endif
