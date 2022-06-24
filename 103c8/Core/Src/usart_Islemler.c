#include "usart_islemler.h"
#include "main.h"
#include "stdio.h"
#include "string.h"
#include "I2C_LED.h"
#include "I2C_MOTOR.h"
#include "SPI_SICAKLIK.h"
/*
 * UART1'DEN GELEN KOMUTA GÖRE YAPILACAK İŞLEMLERİ BELİRLEYEN
 * VE SON KOMUTUN STRİNG DEĞERİNİ DÖNDÜREN FONKSİYON
 */
//char* Yap(char* uart1,char* son_komut)
void Yap(char* uart1)
{

	char* komut = uart1[0];
	char* islem = uart1[1];

	//if(strcmp(uart1,son_komut)  != 0)
	//{
		/*
		 * İŞLEM GELEN VERİNİN İLK HARFİNDEN OKUNUR
		 */
		if(strcmp(uart1,BAGLANTI)==0)
		{
			Yapildi();
		}
		else if(strcmp(&komut,LED_KOMUT) == 0 )
		{
			if(strcmp(&islem,LED_SONDUR)==0)
			{
				LedSondur(uart1);
			}
			else if(strcmp(&islem,LED_YAK) == 0)
			{
				LedYak(uart1);
			}
			else if(strcmp(&islem,LED_DELAY) == 0)
			{
				I2C_LED_DELAY_F(uart1);
			}
		}
		else if(strcmp(&komut,MS_KOMUT) == 0 )
		{
			if(strcmp(&islem,MS_SURME)==0)
			{
				I2C_MOTOR_SUR(uart1);
			}
		}
		else if(strcmp(&komut,SCKLK_KMT) == 0 )
		{
			if(strcmp(&islem,SCKLK_OKU)==0)
			{
				SPI_SICAKLIK_ISLEMLER();
			}
		}
		else
		{
			Yapilamadi();
		}
		//strcpy(son_komut,uart1);
}

