#include "I2C_LED.h"
#include "main.h"
#include "i2c.h"
#include "stdio.h"
#include "string.h"


uint8_t i2c_led_veri[3];
uint16_t yanan_led = 0;
int I2C_LED_DELAY_MS = 500;
int I2C_LED_OTOMATIK_ARTIR = 0;


/*
 * GELEN L1 KOMUTU DURUMUNDA ÇALIŞAN FONKSİYON
 */
void LedYak(char* uart1)
{
	char* k3 = uart1[2];
	char* k4 = uart1[3];
	char* secim = "";
	sprintf(secim,"%c%c",k3,k4);
	if(strcmp(secim,LHEPSI)==0)
	{
		I2C_LED_YAK(LEDH_HEX);
	}
	else if(strcmp(secim,L1)==0)
	{
		I2C_LED_YAK(LED1_HEX);
	}
	else if(strcmp(secim,L2)==0)
	{
		I2C_LED_YAK(LED2_HEX);
	}
	else if(strcmp(secim,L3)==0)
	{
		I2C_LED_YAK(LED3_HEX);
	}
	else if(strcmp(secim,L4)==0)
	{
		I2C_LED_YAK(LED4_HEX);
	}
	else if(strcmp(secim,L5)==0)
	{
		I2C_LED_YAK(LED5_HEX);
	}
	else if(strcmp(secim,L6)==0)
	{
		I2C_LED_YAK(LED6_HEX);
	}
	else if(strcmp(secim,L7)==0)
	{
		I2C_LED_YAK(LED7_HEX);
	}
	else if(strcmp(secim,L8)==0)
	{
		I2C_LED_YAK(LED8_HEX);
	}
	else if(strcmp(secim,L9)==0)
	{
		I2C_LED_YAK(LED9_HEX);
	}
	else if(strcmp(secim,L10)==0)
	{
		I2C_LED_YAK(LED10_HEX);
	}
	else if(strcmp(secim,L11)==0)
	{
		I2C_LED_YAK(LED11_HEX);
	}
	else if(strcmp(secim,L12)==0)
	{
		I2C_LED_YAK(LED12_HEX);
	}
	else if(strcmp(secim,L13)==0)
	{
		I2C_LED_YAK(LED13_HEX);
	}
	else if(strcmp(secim,L14)==0)
	{
		I2C_LED_YAK(LED14_HEX);
	}
	else if(strcmp(secim,L15)==0)
	{
		I2C_LED_YAK(LED15_HEX);
	}
	else if(strcmp(secim,L16)==0)
	{
		I2C_LED_YAK(LED16_HEX);
	}
	else if(strcmp(secim,LSIRALI)==0)
	{
		I2C_LED_OTOMATIK_ARTIR_F(1);
	}
	//Yapildi();
}

/*
 * GELEN L0 KOMUTU DURUMUNDA ÇALIŞAN FONKSİYON
 */
void LedSondur(char* uart1)
{
	char* k3 = uart1[2];
	char* k4 = uart1[3];
	char* secim = "";
	sprintf(secim,"%c%c",k3,k4);
	if(strcmp(secim,LHEPSI)==0)
	{
		I2C_LED_SONDUR(LEDH_HEX);
	}
	else if(strcmp(secim,L1)==0)
	{
		I2C_LED_SONDUR(LED1_HEX);
	}
	else if(strcmp(secim,L2)==0)
	{
		I2C_LED_SONDUR(LED2_HEX);
	}
	else if(strcmp(secim,L3)==0)
	{
		I2C_LED_SONDUR(LED3_HEX);
	}
	else if(strcmp(secim,L4)==0)
	{
		I2C_LED_SONDUR(LED4_HEX);
	}
	else if(strcmp(secim,L5)==0)
	{
		I2C_LED_SONDUR(LED5_HEX);
	}
	else if(strcmp(secim,L6)==0)
	{
		I2C_LED_SONDUR(LED6_HEX);
	}
	else if(strcmp(secim,L7)==0)
	{
		I2C_LED_SONDUR(LED7_HEX);
	}
	else if(strcmp(secim,L8)==0)
	{
		I2C_LED_SONDUR(LED8_HEX);
	}
	else if(strcmp(secim,L9)==0)
	{
		I2C_LED_SONDUR(LED9_HEX);
	}
	else if(strcmp(secim,L10)==0)
	{
		I2C_LED_SONDUR(LED10_HEX);
	}
	else if(strcmp(secim,L11)==0)
	{
		I2C_LED_SONDUR(LED11_HEX);
	}
	else if(strcmp(secim,L12)==0)
	{
		I2C_LED_SONDUR(LED12_HEX);
	}
	else if(strcmp(secim,L13)==0)
	{
		I2C_LED_SONDUR(LED13_HEX);
	}
	else if(strcmp(secim,L14)==0)
	{
		I2C_LED_SONDUR(LED14_HEX);
	}
	else if(strcmp(secim,L15)==0)
	{
		I2C_LED_SONDUR(LED15_HEX);
	}
	else if(strcmp(secim,L16)==0)
	{
		I2C_LED_SONDUR(LED16_HEX);
	}
	else if(strcmp(secim,LSIRALI)==0)
	{
		I2C_LED_OTOMATIK_ARTIR_F(0);
	}

	//Yapildi();

}






void I2C_LED_YAK(int led)
{
	yanan_led |= led;
	i2c_led_veri[0] = yanan_led;
	i2c_led_veri[1] = yanan_led>>8 ;

	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_RESET);


	HAL_I2C_Master_Transmit(&hi2c1, PCF8575_DEV_ADDR, i2c_led_veri, 2, HAL_MAX_DELAY);

	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_SET);


}
void I2C_LED_SONDUR(int led)
{
	led = ~led;
	yanan_led &= led;
	i2c_led_veri[0] = yanan_led;
	i2c_led_veri[1] = yanan_led>>8 ;

	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_RESET);


	HAL_I2C_Master_Transmit(&hi2c1, PCF8575_DEV_ADDR, i2c_led_veri, 2, HAL_MAX_DELAY);

	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_SET);


}


void I2C_LED_SIRALI(void)
{
	if (yanan_led == 0)
	{
	yanan_led = 1;
	}



	i2c_led_veri[0] = yanan_led;
	i2c_led_veri[1] = yanan_led>>8 ;


	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_RESET);


	HAL_I2C_Master_Transmit(&hi2c1, PCF8575_DEV_ADDR, i2c_led_veri, 2, HAL_MAX_DELAY);

	HAL_GPIO_WritePin(GPIOB, I2C_LED_Pin, GPIO_PIN_SET);
	if(yanan_led>0x8000)
	{
		yanan_led <<=1;
		yanan_led = yanan_led | 0x0001;
	}
	else
	{
		yanan_led <<= 1;
	}



}


void I2C_LED_OTOMATIK_ARTIR_F(int artir)
{
	I2C_LED_OTOMATIK_ARTIR = artir;
}


void I2C_LED_DELAY_F(char* uart1)
{
	char* k3 = uart1[2];
	char* k4 = uart1[3];
	char* k5 = uart1[4];
	char* k6 = uart1[5];
	uint8_t* secim[4];
	if(strcmp(k3,"0")==0)
	{
		sprintf(secim,"%c%c%c",k4,k5,k6);
	}
	else
	{
		sprintf(secim,"%c%c%c%c",k3,k4,k5,k6);
	}
	I2C_LED_DELAY_MS = atoi(secim);
	//Yapildi();

}
