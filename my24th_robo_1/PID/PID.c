#include "PID.h"

void PID_Init(pid_t *pid, float kp, float ki, float kd, float max_out, float integral_limit, float deadband)
{
    pid->Kp = kp;
    pid->Ki = ki;
    pid->Kd = kd;
    pid->MaxOut = max_out;
    pid->IntegralLimit = integral_limit;
    pid->Deadband = deadband;

    pid->Err = 0;
    pid->Last_Err = 0;
    pid->Iout = 0;
    pid->Output = 0;
    pid->DWT_CNT = 0;
    pid->dt = 0;
}

//速度环PID计算
float PID_Calculate(pid_t *pid, float measure, float ref)
{
    pid->dt = DWT_GetDeltaT((void *)&pid->DWT_CNT) * 1000.0f;   // 毫秒

    pid->Err = ref - measure;

    //死区
    if (fabsf(pid->Err) < pid->Deadband)
        pid->Err = 0;

    //积分（累加 + 限幅）
    pid->Iout += pid->Ki * pid->Err * pid->dt;
    if (pid->Iout >  pid->IntegralLimit) pid->Iout =  pid->IntegralLimit;
    if (pid->Iout < -pid->IntegralLimit) pid->Iout = -pid->IntegralLimit;

    //微分（普通差分）
    float dout = pid->Kd * (pid->Err - pid->Last_Err) / pid->dt;

    //合成 + 输出限幅
    pid->Output = pid->Kp * pid->Err + pid->Iout + dout;
    if (pid->Output >  pid->MaxOut) pid->Output =  pid->MaxOut;
    if (pid->Output < -pid->MaxOut) pid->Output = -pid->MaxOut;

    pid->Last_Err = pid->Err;
    return pid->Output;
}

//过零PID（6020 角度环用，编码器 0~8191 会过零）
float PID_Calculate_ECD(pid_t *pid, float measure, float ref, float ecd_range)
{
    pid->dt = DWT_GetDeltaT((void *)&pid->DWT_CNT) * 1000.0f;

    pid->Err = ecd_zero(ref, measure, ecd_range);   //关键区别：过零误差

    if (fabsf(pid->Err) < pid->Deadband)
        pid->Err = 0;

    pid->Iout += pid->Ki * pid->Err * pid->dt;
    if (pid->Iout >  pid->IntegralLimit) pid->Iout =  pid->IntegralLimit;
    if (pid->Iout < -pid->IntegralLimit) pid->Iout = -pid->IntegralLimit;

    float dout = pid->Kd * (pid->Err - pid->Last_Err) / pid->dt;

    pid->Output = pid->Kp * pid->Err + pid->Iout + dout;
    if (pid->Output >  pid->MaxOut) pid->Output =  pid->MaxOut;
    if (pid->Output < -pid->MaxOut) pid->Output = -pid->MaxOut;

    pid->Last_Err = pid->Err;
    return pid->Output;
}
