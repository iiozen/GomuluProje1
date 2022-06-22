#include "I2C_MOTOR.h"
#include "main.h"
#include "i2c.h"
#include "stdio.h"
#include "string.h"



volatile uint8_t i2c_motor_veri[5];
volatile int motor_hiz ;
uint8_t sag,sol;
uint8_t* secicim[4];


void I2C_MOTOR(int hiz);
void I2C_MOTOR_SUR(char* uart1)
{
	char k3 = uart1[2];
	char k4 = uart1[3];
	char k5 = uart1[4];
	char k6 = uart1[5];

	if(strcmp(k3,"0")==0)
	{
		if(strcmp(k4,"0")==0)
		{
			if(strcmp(k5,"0")==0)
			{
				if(strcmp(k6,"0")==0)
				{
					secicim[0] = "0";
				}
				else
				{
					sprintf(secicim,"%c",k6);
				}
			}
			else
			{
				sprintf(secicim,"%c%c",k5,k6);
			}

		}

		else
		{
			sprintf(secicim,"%c%c%c",k4,k5,k6);
		}

	}
	else
	{
		sprintf(secicim,"%c%c%c%c",k3,k4,k5,k6);
	}


	motor_hiz =(uint16_t)(atoi(secicim) & 0x0fff);

	I2C_MOTOR(motor_hiz);
	Yapildi();
}

void I2C_MOTOR(int hiz)
{

	HAL_GPIO_WritePin(GPIOB, I2C_MOTOR_Pin, GPIO_PIN_RESET);

	i2c_motor_veri[0] =  MCP47FEB21A3_MEMORY_ADDR;

	i2c_motor_veri[1] = (hiz >> 8);
	i2c_motor_veri[2] = hiz;

	HAL_I2C_Master_Transmit(&hi2c1, MCP47FEB21A3_DEV_ADDR, &i2c_motor_veri, 3, HAL_MAX_DELAY);

	HAL_GPIO_WritePin(GPIOB, I2C_MOTOR_Pin, GPIO_PIN_SET);

}
