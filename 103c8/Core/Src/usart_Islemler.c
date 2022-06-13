#include "usart_islemler.h"

/*
 * UART1'DEN GELEN KOMUTA GÖRE YAPILACAK İŞLEMLERİ BELİRLEYEN
 * VE SON KOMUTUN STRİNG DEĞERİNİ DÖNDÜREN FONKSİYON
 */
char* Yap(UART_HandleTypeDef* huart3,char* uart1,char* son_komut)
{

	char* komut = uart1[0];
	char* islem = uart1[1];
	char* secilen= uart1[2];

	/*

	komut = uart1[0];
	islem = uart1[1];
	secilen = uart1[2];
	*/

	/*
	sprintf(komut,"%c",uart1[0]);
	sprintf(islem,"%c",uart1[1]);
	sprintf(islem2,"%c",uart1[1]);
	sprintf(secilen,"%c",uart1[2]);
	*/

	if(strcmp(uart1,son_komut)  != 0)
	{
		/*
		 * İŞLEM GELEN VERİNİN İLK HARFİNDEN OKUNUR
		 */

		if(strcmp(&komut,LED_KOMUT) == 0 )
		{
			if(strcmp(&islem,LED_SONDUR)==0)
			{
				LedSondur(&secilen);
			}
			else if(strcmp(&islem,LED_YAK) == 0)
			{
				LedYak(&secilen);
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
void LedYak(char* secim)
{
	if(strcmp(secim,LED_HEPSI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_SET);
		HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_SET);
		HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_SET);
		HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_SET);
	}
	else if(strcmp(secim,LED_MAVI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_SET);
	}
	else if(strcmp(secim,LED_YESIL)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_SET);
	}
	else if(strcmp(secim,LED_KIRMIZI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_SET);
	}
	else if(strcmp(secim,LED_SARI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_SET);
	}

	Yapildi();
}

/*
 * GELEN L0 KOMUTU DURUMUNDA ÇALIŞAN FONKSİYON
 */
void LedSondur(char* secim)
{
	if(strcmp(secim,LED_HEPSI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_RESET);
		HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_RESET);
	}
	else if(strcmp(secim,LED_MAVI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED1_Pin, GPIO_PIN_RESET);
	}
	else if(strcmp(secim,LED_YESIL)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED2_Pin, GPIO_PIN_RESET);
	}
	else if(strcmp(secim,LED_KIRMIZI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED3_Pin, GPIO_PIN_RESET);
	}
	else if(strcmp(secim,LED_SARI)==0)
	{
		HAL_GPIO_WritePin(GPIOA, LED4_Pin, GPIO_PIN_RESET);
	}
	Yapildi();
}


