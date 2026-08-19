#ifndef __PID_H
#define __PID_H

#include "stdint.h"
#include "math.h"
#include "bsp_dwt.h"     // DWT_GetDeltaT
#include "user_lib.h"    // ecd_zero

typedef struct {
    float Kp;              // 比例系数
    float Ki;              // 积分系数
    float Kd;              // 微分系数
    float MaxOut;          // 输出限幅
    float IntegralLimit;   // 积分限幅
    float Deadband;        // 死区

    float Err;             // 当前误差
    float Last_Err;        // 上次误差
    float Iout;            // 积分累加
    float Output;          // 输出

    uint32_t DWT_CNT;      // DWT 计时基准
    float dt;              // 时间间隔（毫秒）
} pid_t;

void  PID_Init(pid_t *pid, float kp, float ki, float kd, float max_out, float integral_limit, float deadband);
float PID_Calculate(pid_t *pid, float measure, float ref);                        // 普通 PID（速度环用）
float PID_Calculate_ECD(pid_t *pid, float measure, float ref, float ecd_range);   // 过零 PID（角度环用）

#endif

