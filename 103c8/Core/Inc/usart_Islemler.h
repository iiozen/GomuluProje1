#ifndef __USARTISLEMLERH__
#define __USARTISLEMLERH__

#include "main.h"
#include "stdio.h"
#include "string.h"

#define UART1_ADET 2
#define UART3_ADET 1


char* Yap(UART_HandleTypeDef* huart3,char* uart1,char* son_komut);
void LedYak(void);
void LedSondur(void);

#endif
