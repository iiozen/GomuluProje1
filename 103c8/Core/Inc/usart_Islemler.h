#ifndef __USARTISLEMLERH__
#define __USARTISLEMLERH__

#include "main.h"
#include "stdio.h"
#include "string.h"
#include "LEDDEF.h"

#define UART1_ADET 3
#define UART3_ADET 1
#define UART3_ONAY "1"


char* Yap(UART_HandleTypeDef* huart3,char* uart1,char* son_komut);
void LedYak(char* secim);
void LedSondur(char* secim);

#endif
