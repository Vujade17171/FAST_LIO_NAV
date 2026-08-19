#include "bsp_dwt.h"

//存储当前系统时间
DWT_Time_t SysTime;

//							cpu频率     每毫秒的cpu周期数 每微秒的cpu周期数
static uint32_t CPU_FREQ_Hz,CPU_FREQ_Hz_ms,CPU_FREQ_Hz_us;

//DWT计数器溢出次数
static uint32_t CYCCNT_RountCount;

//上一次的dwt->cyccnt的值
static uint32_t CYCCNT_LAST;

//拓展的64位周期计数器
uint64_t CYCCNT64;

static void DWT_CNT_Update(void);

//											cpu的主频率
void DWT_Init(uint32_t CPU_Freq_mHz){
	//使能dwt外设
	CoreDebug->DEMCR |= CoreDebug_DEMCR_TRCENA_Msk;
	
	//dwt cyccnt寄存器计数清0
	DWT->CYCCNT = (uint32_t)0u;
	
	//使能cortex-M DWT CYCCNT寄存器
	DWT->CTRL |= DWT_CTRL_CYCCNTENA_Msk;
	
	//计算cpu频率相关参数
	CPU_FREQ_Hz = CPU_Freq_mHz * 1000000; // 转换位Hz
	CPU_FREQ_Hz_ms = CPU_FREQ_Hz / 1000;	//每毫秒周期数
	CPU_FREQ_Hz_us = CPU_FREQ_Hz / 1000000;//每微秒周期数
	
	//初始化溢出计数
	CYCCNT_RountCount = 0;
}


//用于计算两次调用的时间之差float版本
float DWT_GetDeltaT(uint32_t *cnt_last){
	//获取当前周期值
	volatile uint32_t cnt_now = DWT->CYCCNT;
	//计算时间差
	float dt = ((uint32_t)(cnt_now - *cnt_last)) / ((float)(CPU_FREQ_Hz));
	//更新上一次的值
	*cnt_last = cnt_now;
	//处理计数器溢出
	DWT_CNT_Update();
	
	return dt;
}

//用于计算两次调用的时间之差 double 版本
double DWT_GetDeltaT64(uint32_t *cnt_last){
	volatile uint32_t cnt_now = DWT->CYCCNT;
	double dt = ((uint32_t)(cnt_now - *cnt_last)) / ((double)(CPU_FREQ_Hz));
	*cnt_last = cnt_now;
	
	DWT_CNT_Update();
	
	return dt;
}

//更新系统时间
void DWT_SysTimeUpdate(void){
	volatile uint32_t cnt_now = DWT->CYCCNT;
	static uint64_t CNT_TEMP1,CNT_TEMP2,CNT_TEMP3;
	
	//处理溢出
	DWT_CNT_Update();
	//计算位总周期数
	CYCCNT64 = (uint64_t)CYCCNT_RountCount * (uint64_t)UINT32_MAX + (uint64_t)cnt_now;
	//计算秒
	CNT_TEMP1 = CYCCNT64 / CPU_FREQ_Hz;
	SysTime.s = CNT_TEMP1;
	//计算毫秒
	CNT_TEMP2 = CYCCNT64 - CNT_TEMP1 * CPU_FREQ_Hz;
	SysTime.ms = CNT_TEMP2 / CPU_FREQ_Hz_ms;
	//计算微秒
	CNT_TEMP3 = CNT_TEMP2 - SysTime.ms * CPU_FREQ_Hz_ms;
	SysTime.us = CNT_TEMP3 / CPU_FREQ_Hz_us;
}

//获得当前时间（秒）
float DWT_GetTimeline_s(void){
	DWT_SysTimeUpdate();
	
	float DWT_Timelinef32 = SysTime.s + SysTime.ms * 0.001f + SysTime.us * 0.000001f;
	
	return DWT_Timelinef32;
}


//获取当前时间 (毫秒)
float DWT_GetTimeline_ms(void)
{
    DWT_SysTimeUpdate();

    float DWT_Timelinef32 = SysTime.s * 1000 + SysTime.ms + SysTime.us * 0.001f;

    return DWT_Timelinef32;
}

//获取当前时间 (微秒)
uint64_t DWT_GetTimeline_us(void)
{
    DWT_SysTimeUpdate();

    uint64_t DWT_Timelinef32 = SysTime.s * 1000000 + SysTime.ms * 1000 + SysTime.us;

    return DWT_Timelinef32;
}

//处理计数器溢出
//检测到dwt->cyccnt的溢出，32位计数器会从0xffffffff回到0
static void DWT_CNT_Update(void){
	volatile uint32_t cnt_now = DWT->CYCCNT;
	
	//如果当前值比上次小，说明发生溢出
	if(cnt_now < CYCCNT_LAST){
		CYCCNT_RountCount++; //溢出次数+1
	}
	
	CYCCNT_LAST = cnt_now;//更新上一次的值
}

//实现高精度延时
void DWT_Delay(float Delay){
	uint32_t tickstart = DWT->CYCCNT;
	float wait = Delay;
	
	//等待经过指定时间
	while((DWT->CYCCNT - tickstart) < wait * (float)CPU_FREQ_Hz){
		//空循环
	}
}


//计算从起始时间到当前时间的真实经过时间
float DWT_GET_true_time(DWT_TIME_TYPE* dwt){
	float now_t = DWT_GetTimeline_s();
	dwt->true_time = now_t - dwt->start_time;
	return dwt->true_time;
}

