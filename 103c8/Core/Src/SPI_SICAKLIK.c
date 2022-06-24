#include "SPI_SICAKLIK.h"
#include "main.h"
#include "spi.h"
#include "stdio.h"
#include "string.h"
#include "usart.h"

char spi_sicaklik[5];
uint8_t verici[5];
uint8_t alici1[5];
uint8_t alici2[5];
uint8_t alici3[5];

void SPI_SICAKLIK_BASLAT(void)

{
	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);
/*
	HAL_SPI_Transmit(&hspi2,(uint8_t*) TC72_READ, 1, 100);
	HAL_SPI_Transmit(&hspi2,(uint8_t*) TC72_READ_ADRES, 1, 100);
	HAL_SPI_Receive(&hspi2, (uint8_t*)spi_sicaklik, 3, 100);
*/
	//verici[0]=TC72_WRITE_ADRES;

	verici[0]=0x80  ;

	HAL_SPI_Transmit(&hspi2,verici, 1, HAL_MAX_DELAY);

	/*
	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);
	*/

	verici[0]=0x00;
	HAL_SPI_Transmit(&hspi2,verici, 1, HAL_MAX_DELAY);



	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);
}

void SPI_SICAKLIK_ISLEMLER(void)
{

	HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);

		verici[0]=0x00;

		HAL_SPI_Transmit(&hspi2,verici, 1, 100);
/*

		verici[0]=0x00;
		HAL_SPI_Transmit(&hspi2,verici, 1, 100);

		verici[0]=0x00;
		HAL_SPI_Transmit(&hspi2,verici, 1, 100);
		*/
		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);




		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_RESET);
/*
		verici[0]=0x02;
		HAL_SPI_Transmit(&hspi2,verici, 1, HAL_MAX_DELAY);
*/
		HAL_SPI_Receive(&hspi2, alici1, 3, HAL_MAX_DELAY);
/*
		HAL_SPI_Receive(&hspi2, alici2, 1, HAL_MAX_DELAY);

		HAL_SPI_Receive(&hspi2, alici3, 1, HAL_MAX_DELAY);
*/
		HAL_GPIO_WritePin(GPIOB, SPI_SICAKLIK_Pin, GPIO_PIN_SET);

		Yapildi();

		char uart_buf[50];
		int uz;

		uz = sprintf(uart_buf,
				" 0x%02x 0x%02x 0x%02x\r\n",
				alici1[0],
				alici1[1],
				alici1[2]);

		HAL_UART_Transmit(&huart1, uart_buf,uz , 100);

}




