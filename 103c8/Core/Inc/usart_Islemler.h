#ifndef __USARTISLEMLERH__
#define __USARTISLEMLERH__


/*
 * KOMUT
 */
#define LED_KOMUT "L"

#define MS_KOMUT "M"

#define SCKLK_KMT "S"

/*
 * İŞLEM
 */
#define LED_YAK "Y"
#define LED_SONDUR "S"
#define LED_DELAY "D"

#define MS_SURME "S"

#define SCKLK_OKU "O"




#define BAGLANTI "BGL000"

#define UART1_RECIEVE_ADET 6
#define UART1_TRANSMIT_ADET 1
#define UART1_TRANSMIT_ONAY "1"
#define UART1_RESET_TIME 2000


void Yap(char* uart1);


#endif
