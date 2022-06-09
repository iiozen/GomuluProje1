#include "usart_islemler.h"


/*
 * UART1'DEN GELEN KOMUTA GÖRE YAPILACAK İŞLEMLERİ BELİRLEYEN
 * VE SON KOMUTUN STRİNG DEĞERİNİ DÖNDÜREN FONKSİYON
 */
char* Yap(UART_HandleTypeDef* huart3,char* uart1,char* son_komut)
{
	if(strcmp(uart1,son_komut)  != 0)
	{
		if(strncmp(uart1,"L",1) == 0 )
		{
			if(strcmp(&uart1[1],"0")==0)
			{
				LedSondur();
			}
			else if(strcmp(&uart1[1],"1") == 0)
			{
				LedYak();
			}
		}
		strcpy(son_komut,uart1);
	}
	else
	{
		Yapildi();
	}
	return son_komut;
}

/*
 * GELEN L1 KOMUTU DURUMUNDA ÇALIŞAN FONKSİYON
 */
void LedYak(void)
{

	HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_SET);
	Yapildi();
}

/*
 * GELEN L0 KOMUTU DURUMUNDA ÇALIŞAN FONKSİYON
 */
void LedSondur(void)
{
	HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_RESET);
	Yapildi();
}


