/**
  ******************************************************************************
  * @file	 user_lib.c
  * @author  Wang Hongxi
  * @version V1.0.0
  * @date    2021/2/18
  * @brief   
  ******************************************************************************
  * @attention
  *
  ******************************************************************************
  */
#include "stdlib.h"
#include "string.h"
#include "user_lib.h"
#include "math.h"
#include "arm_math.h"
#include "main.h"

#ifdef _CMSIS_OS_H
#define user_malloc pvPortMalloc
#else
#define user_malloc malloc
#endif

void mat_trans(float src[3][3],float dis[3][3])
{
	char i,j;
	for(i = 0;i < 3;i++)
	{
		for(j = 0; j < 3 ; j++)
		{
			dis[i][j] = src[j][i];
		}
	}
}

float cosd(float in)
{
	return arm_cos_f32(in*0.0173f);
}

float sind(float in)
{
	return arm_sin_f32(in*0.0173f);
}
/*
	雅可比求逆
*/
void cal_inv_jacobi(float *J_data,float *J_inv_data)
{
	float det;
  //arm加速
	char i=0;
	arm_status sta;  
	/****浮点数数组****/
	float32_t pDataB[4];
	float32_t pDataA[4] = { 1.0f,   0.0f,   
							0.0f,   1.0f};
				
	arm_matrix_instance_f32 pSrcA;
	arm_matrix_instance_f32 pSrcB; 
	pDataA[0] = J_data[0];
	pDataA[1] = J_data[1];
	pDataA[2] = J_data[2];
	pDataA[3] = J_data[3];							
	/****浮点数****/
	pSrcA.numCols = 2;
	pSrcA.numRows = 2;
	pSrcA.pData = pDataA;
	
	pSrcB.numCols = 2;
	pSrcB.numRows = 2;
	pSrcB.pData = pDataB;
	
	sta = arm_mat_inverse_f32(&pSrcA, &pSrcB);
	
	J_inv_data[0] = pDataB[0];
	J_inv_data[1] = pDataB[1];
	J_inv_data[2] = pDataB[2];
	J_inv_data[3] = pDataB[3];
}
/*
	低通滤波
	输入 输出 截止频率 时间
*/

float Low_Fass_Filter(float in, float out, float fc, float dt) 
{
    if (fc <= 0.0f || dt <= 0.0f) 
	{
        return out;
    }
    float rc = 1.0f/( 2 * PI * fc);
    float alpha = dt/(dt + rc);
    out += (in - out) * alpha;
	return out;
}
/*快速平方根倒数函数 计算 1/根号x的近似值*/
float invSqrt(float x)
{
    float halfx = 0.5f * x;
    float y = x;
    long i = *(long *)&y;
    i = 0x5f375a86 - (i >> 1);
    y = *(float *)&i;
    y = y * (1.5f - (halfx * y * y));
    return y;
}

float Angle_Limit (float angle ,float max)
{
	 	
		if(angle > max)
			angle -= max;
		if(angle < 0)
			angle += max;
		return angle;
		
}

float ecd_zero(float ecd, float offset_ecd, float ecd_range)
{
		float relative_ecd = ecd - offset_ecd;
		float half_ecd_range = ecd_range / 2;
	
		if(relative_ecd > half_ecd_range)
		{
					relative_ecd -= (ecd_range-1);
		}
		if(relative_ecd < - half_ecd_range)
		{
					relative_ecd += (ecd_range-1);
		}
		return relative_ecd;
}

int Angle_on(float angle ,float angle_target,float allow_angle)
{
	float err1 = angle - angle_target;
	float err2 = angle_target - angle;	
	float real_error;
	if(err1 > 0)
	{
		real_error = err1;
	}
	if(err2 > 0)
	{
		real_error = err2;		
	}
	if(real_error > 180)
	{
		real_error = 360 - real_error;
	}
	if(real_error < allow_angle)
	{ 
		return 1;		
	}
	else
	{
		return 0;		
	}
}

//快速开方
float Sqrt(float x)
{
    float y;
    float delta;
    float maxError;

    if (x <= 0)
    {
        return 0;
    }

    // initial guess
    y = x / 2;

    // refine
    maxError = x * 0.001f;

    do
    {
        delta = (y * y) - x;
        y -= delta / (2 * y);
    } while (delta > maxError || delta < -maxError);

    return y;
}

//快速求平方根倒数
/*
float invSqrt(float num)
{
    float halfnum = 0.5f * num;
    float y = num;
    long i = *(long *)&y;
    i = 0x5f375a86- (i >> 1);
    y = *(float *)&i;
    y = y * (1.5f - (halfnum * y * y));
    return y;
}*/

/**
  * @brief          斜波函数初始化
  * @author         RM
  * @param[in]      斜波函数结构体
  * @param[in]      间隔的时间，单位 s
  * @param[in]      最大值
  * @param[in]      最小值
  * @retval         返回空
  */
void ramp_init(ramp_function_source_t *ramp_source_type, float frame_period, float max, float min)
{
    ramp_source_type->frame_period = frame_period;
    ramp_source_type->max_value = max;
    ramp_source_type->min_value = min;
    ramp_source_type->input = 0.0f;
    ramp_source_type->out = 0.0f;
}

/**
  * @brief          斜波函数计算，根据输入的值进行叠加， 输入单位为 /s 即一秒后增加输入的值
  * @author         RM
  * @param[in]      斜波函数结构体
  * @param[in]      输入值
  * @retval         返回空
  */
float ramp_calc(ramp_function_source_t *ramp_source_type, float input)
{
    ramp_source_type->input = input;
    ramp_source_type->out += ramp_source_type->input * ramp_source_type->frame_period;
    if (ramp_source_type->out > ramp_source_type->max_value)
    {
        ramp_source_type->out = ramp_source_type->max_value;
    }
    else if (ramp_source_type->out < ramp_source_type->min_value)
    {
        ramp_source_type->out = ramp_source_type->min_value;
    }
    return ramp_source_type->out;
}
	float buffer = 0;
float RAMP_float(float final, float now, float ramp)
{
	buffer = final - now;

	if (buffer > 0)
	{
		if (buffer > ramp)
		{
			now += ramp;
		}
		else
		{
			now += buffer;
		}
	}
	else
	{
		if (buffer < -ramp)
		{
			now += -ramp;
		}
		else
		{
			now += buffer;
		}
	}

	return now;
}
int Deceleration_judgment(float now_value,float last_value)
{
	if(now_value < last_value)
	{
		return 1;
	}else
	{
		return 0;
	}
}
//绝对值限制
float abs_limit(float num, float Limit)
{
    if (num > Limit)
    {
        num = Limit;
    }
    else if (num < -Limit)
    {
        num = -Limit;
    }
    return num;
}

//判断符号位
float sign(float value)
{
    if (value >= 0.0f)
    {
        return 1.0f;
    }
    else
    {
        return -1.0f;
    }
}

//浮点死区
float float_deadband(float Value, float minValue, float maxValue)
{
    if (Value < maxValue && Value > minValue)
    {
        Value = 0.0f;
    }
    return Value;
}

//int26死区
int16_t int16_deadline(int16_t Value, int16_t minValue, int16_t maxValue)
{
    if (Value < maxValue && Value > minValue)
    {
        Value = 0;
    }
    return Value;
}

//限幅函数
float float_constrain(float Value, float minValue, float maxValue)
{
    if (Value < minValue)
        return minValue;
    else if (Value > maxValue)
        return maxValue;
    else
        return Value;
}

//限幅函数
int16_t int16_constrain(int16_t Value, int16_t minValue, int16_t maxValue)
{
    if (Value < minValue)
        return minValue;
    else if (Value > maxValue)
        return maxValue;
    else
        return Value;
}

//循环限幅函数
float loop_float_constrain(float Input, float minValue, float maxValue)
{
    if (maxValue < minValue)
    {
        return Input;
    }

    if (Input > maxValue)
    {
        float len = maxValue - minValue;
        while (Input > maxValue)
        {
            Input -= len;
        }
    }
    else if (Input < minValue)
    {
        float len = maxValue - minValue;
        while (Input < minValue)
        {
            Input += len;
        }
    }
    return Input;
}

//弧度格式化为-PI~PI

//角度格式化为-180~180
float theta_format(float Ang)
{
    return loop_float_constrain(Ang, -180.0f, 180.0f);
}

int float_rounding(float raw)
{
    static int integer;
    static float decimal;
    integer = (int)raw;
    decimal = raw - integer;
    if (decimal > 0.5f)
        integer++;
    return integer;
}

/**
  * @brief          最小二乘法初始化
  * @param[in]      最小二乘法结构体
  * @param[in]      样本数
  * @retval         返回空
  */
void OLS_Init(Ordinary_Least_Squares_t *OLS, uint16_t order)
{
    OLS->Order = order;
    OLS->Count = 0;
    OLS->x = (float *)user_malloc(sizeof(float) * order);//申请空间
    OLS->y = (float *)user_malloc(sizeof(float) * order);
    OLS->k = 0;
    OLS->b = 0;
    memset((void *)OLS->x, 0, sizeof(float) * order);//对空间清零
    memset((void *)OLS->y, 0, sizeof(float) * order);
    memset((void *)OLS->t, 0, sizeof(float) * 4);
}

/**
  * @brief          最小二乘法拟合
  * @param[in]      最小二乘法结构体
  * @param[in]      信号新样本距上一个样本时间间隔
  * @param[in]      信号值
  */
void OLS_Update(Ordinary_Least_Squares_t *OLS, float deltax, float y)
{
    static float temp = 0;
    temp = OLS->x[1];
    for (uint16_t i = 0; i < OLS->Order - 1; ++i)//将X时间向前推，保证初始的时间都为零，y的数值向前推
    {
        OLS->x[i] = OLS->x[i + 1] - temp;
        OLS->y[i] = OLS->y[i + 1];//
    }
    OLS->x[OLS->Order - 1] = OLS->x[OLS->Order - 2] + deltax;//最大的时间为上次的最大时间加上增加的时间
    OLS->y[OLS->Order - 1] = y;//更新最新的y

    if (OLS->Count < OLS->Order)
    {
        OLS->Count++;
    }
    memset((void *)OLS->t, 0, sizeof(float) * 4);//清空t
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)//更新t
    {
        OLS->t[0] += OLS->x[i] * OLS->x[i];
        OLS->t[1] += OLS->x[i];
        OLS->t[2] += OLS->x[i] * OLS->y[i];
        OLS->t[3] += OLS->y[i];
    }

    OLS->k = (OLS->t[2] * OLS->Order - OLS->t[1] * OLS->t[3]) / (OLS->t[0] * OLS->Order - OLS->t[1] * OLS->t[1]);//计算斜率k y=kx+b
    OLS->b = (OLS->t[0] * OLS->t[3] - OLS->t[1] * OLS->t[2]) / (OLS->t[0] * OLS->Order - OLS->t[1] * OLS->t[1]);//计算b

    OLS->StandardDeviation = 0;//计算标准差
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)
    {
        OLS->StandardDeviation += fabsf(OLS->k * OLS->x[i] + OLS->b - OLS->y[i]);
    }
    OLS->StandardDeviation /= OLS->Order;
}

/**
  * @brief          最小二乘法提取信号微分
  * @param[in]      最小二乘法结构体
  * @param[in]      信号新样本距上一个样本时间间隔
  * @param[in]      信号值
  * @retval         返回斜率k
  */
float OLS_Derivative(Ordinary_Least_Squares_t *OLS, float deltax, float y)
{
    static float temp = 0;
    temp = OLS->x[1];
    for (uint16_t i = 0; i < OLS->Order - 1; ++i)
    {
        OLS->x[i] = OLS->x[i + 1] - temp;
        OLS->y[i] = OLS->y[i + 1];
    }
    OLS->x[OLS->Order - 1] = OLS->x[OLS->Order - 2] + deltax;
    OLS->y[OLS->Order - 1] = y;

    if (OLS->Count < OLS->Order)
    {
        OLS->Count++;
    }

    memset((void *)OLS->t, 0, sizeof(float) * 4);
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)
    {
        OLS->t[0] += OLS->x[i] * OLS->x[i];
        OLS->t[1] += OLS->x[i];
        OLS->t[2] += OLS->x[i] * OLS->y[i];
        OLS->t[3] += OLS->y[i];
    }

    OLS->k = (OLS->t[2] * OLS->Order - OLS->t[1] * OLS->t[3]) / (OLS->t[0] * OLS->Order - OLS->t[1] * OLS->t[1]);

    OLS->StandardDeviation = 0;
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)
    {
        OLS->StandardDeviation += fabsf(OLS->k * OLS->x[i] + OLS->b - OLS->y[i]);
    }
    OLS->StandardDeviation /= OLS->Order;

    return OLS->k;
}

/**
  * @brief          获取最小二乘法提取信号微分
  * @param[in]      最小二乘法结构体
  * @retval         返回斜率k
  */
float Get_OLS_Derivative(Ordinary_Least_Squares_t *OLS)
{
    return OLS->k;
}

/**
  * @brief          最小二乘法平滑信号
  * @param[in]      最小二乘法结构体
  * @param[in]      信号新样本距上一个样本时间间隔
  * @param[in]      信号值
  * @retval         返回平滑输出
  */
float OLS_Smooth(Ordinary_Least_Squares_t *OLS, float deltax, float y)
{
    static float temp = 0;
    temp = OLS->x[1];
    for (uint16_t i = 0; i < OLS->Order - 1; ++i)
    {
        OLS->x[i] = OLS->x[i + 1] - temp;
        OLS->y[i] = OLS->y[i + 1];
    }
    OLS->x[OLS->Order - 1] = OLS->x[OLS->Order - 2] + deltax;
    OLS->y[OLS->Order - 1] = y;

    if (OLS->Count < OLS->Order)
    {
        OLS->Count++;
    }

    memset((void *)OLS->t, 0, sizeof(float) * 4);
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)
    {
        OLS->t[0] += OLS->x[i] * OLS->x[i];
        OLS->t[1] += OLS->x[i];
        OLS->t[2] += OLS->x[i] * OLS->y[i];
        OLS->t[3] += OLS->y[i];
    }

    OLS->k = (OLS->t[2] * OLS->Order - OLS->t[1] * OLS->t[3]) / (OLS->t[0] * OLS->Order - OLS->t[1] * OLS->t[1]);
    OLS->b = (OLS->t[0] * OLS->t[3] - OLS->t[1] * OLS->t[2]) / (OLS->t[0] * OLS->Order - OLS->t[1] * OLS->t[1]);

    OLS->StandardDeviation = 0;
    for (uint16_t i = OLS->Order - OLS->Count; i < OLS->Order; ++i)
    {
        OLS->StandardDeviation += fabsf(OLS->k * OLS->x[i] + OLS->b - OLS->y[i]);
    }
    OLS->StandardDeviation /= OLS->Order;

    return OLS->k * OLS->x[OLS->Order - 1] + OLS->b;
}

/**
  * @brief          获取最小二乘法平滑信号
  * @param[in]      最小二乘法结构体
  * @retval         返回平滑输出
  */
float Get_OLS_Smooth(Ordinary_Least_Squares_t *OLS)
{
    return OLS->k * OLS->x[OLS->Order - 1] + OLS->b;
}
/**
 * 将RPM转换为线速度（m/s）
 * @param rpm    转速（转/分钟）
 * @param radius 旋转半径（米）
 * @return 线速度（m/s)
 */
float rpm_to_ms(float rpm, float radius) {
    // RPM转角速度（弧度/秒）
    float angular_velocity = rpm * (2.0f*PI/60.0f);
    
    // 计算线速度（v = ω * r）
    return angular_velocity * radius;
}

/**
 * 将线速度（m/s）转为RPM
 * @param ms    转速（m/s）
 * @param radius 旋转半径（米）
 * @return rpm
 */
float ms_to_rpm(float ms, float radius) {
    float rpm = (ms / radius) / (2.0f*PI/60.0f);
    return rpm;
}
