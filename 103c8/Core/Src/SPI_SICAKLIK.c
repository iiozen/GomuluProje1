#include "SPI_SICAKLIK.h"
#include "main.h"
#include "spi.h"
#include "stdio.h"
#include "string.h"
#include "usart.h"

char spi_sicaklik[5];
uint8_t verici[5];
uint8_t alici1[5];
int SPI_SICAKLIK_OKU = 0;

void SPI_SICAKLIK_BASLAT(int baslat)

{
	SPI_SICAKLIK_OKU = baslat;
}

void SPI_SICAKLIK_ISLEMLER(void)
{

	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);

		verici[0]=TC72_READ_ADRES;

		HAL_SPI_Transmit(&hspi2,verici, 1, 100);

		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);




		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);


		HAL_SPI_Receive(&hspi2, alici1, TC72_OKUMA_ADET, HAL_MAX_DELAY);

		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);

		//Yapildi();


		float virgul_deger=0;
		float s_d;
		for(int i=3;i<7;i++)
		{
			s_d = 0;
			uint8_t s_bit = 1<<i;
			if((alici1[1]&s_bit)==s_bit)
			{
				s_d = 1;
				for (int j = 0;j<(7-i);j++)
				{
					s_d /=2;
				}
			}
			virgul_deger += s_d;
		}

		int eksi = 0;
		float sicaklik;
		if (alici1[0]>=0x80)
		{
			eksi = 1;
		}

		//alici1[0] &=0x0fff;
		alici1[0] = alici1[0] & ~(1<<7);
		sicaklik = (alici1[0]<<1) | (alici1[1]>>7);

		sicaklik +=virgul_deger;

		if (eksi)
		{
			sicaklik = sicaklik - 256;
		}

		char uart_buf[50];
		int uz;

		uz = sprintf(uart_buf,
				"SO%.4f\n",
					sicaklik);

		HAL_UART_Transmit(&huart3, uart_buf,uz , HAL_MAX_DELAY);

}




