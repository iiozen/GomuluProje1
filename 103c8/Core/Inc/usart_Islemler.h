#ifndef __USARTISLEMLERH__
#define __USARTISLEMLERH__

#include "main.h"
#include "stdio.h"
#include "string.h"
#include "LEDDEF.h"

#define BAGLANTI "BGL"

#define UART1_RECIEVE_ADET 3
#define UART1_TRANSMIT_ADET 1
#define UART1_TRANSMIT_ONAY "1"


char* Yap(char* uart1,char* son_komut);
void LedYak(char* secim);
void LedSondur(char* secim);

#endif
