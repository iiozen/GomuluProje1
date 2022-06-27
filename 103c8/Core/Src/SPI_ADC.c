#include <SPI_ADC.h>
#include "main.h"
#include "spi.h"
#include "stdio.h"
#include "string.h"
#include "usart.h"

int SPI_ADC_OKU = 0;
uint8_t alici2[5];
char* uart_adc[50];
float adc_deger=0;


void SPI_ADC_BASLAT(int baslat)

{
	SPI_ADC_OKU = baslat;
}


void SPI_ADC_ISLEMLER(void)
{

		HAL_GPIO_WritePin(GPIOB, SPI_ADC_Pin, GPIO_PIN_RESET);


		HAL_SPI_Receive(&hspi2, alici2, 2, HAL_MAX_DELAY);

		HAL_GPIO_WritePin(GPIOB, SPI_ADC_Pin, GPIO_PIN_SET);

		adc_deger = ((alici2[0]<<8) + alici2[1]) / 2;
		adc_deger *= 3.3;
		adc_deger /= 4095;




		char* uart_buf1[50];
		int uz1;


		uz1 = sprintf(uart_buf1,
				"AO%.3f\n",
					adc_deger);


		HAL_UART_Transmit(&huart3, uart_buf1 ,uz1 , HAL_MAX_DELAY);

}
