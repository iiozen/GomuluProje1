#ifndef __I2C_LED_DEF__
#define __I2C_LED_DEF__


#define PCF8575_DEV_ADDR 0x20<<1


/*
 * SEÇİM
 */
#define L1 "01"
#define L2 "02"
#define L3 "03"
#define L4 "04"
#define L5 "05"
#define L6 "06"
#define L7 "07"
#define L8 "08"
#define L9 "09"
#define L10 "10"
#define L11 "11"
#define L12 "12"
#define L13 "13"
#define L14 "14"
#define L15 "15"
#define L16 "16"
#define LHEPSI "00"
#define LSIRALI "22"


#define LEDH_HEX 0xFFFF
#define LED1_HEX 0x0001
#define LED2_HEX 0x0002
#define LED3_HEX 0x0004
#define LED4_HEX 0x0008
#define LED5_HEX 0x0010
#define LED6_HEX 0x0020
#define LED7_HEX 0x0040
#define LED8_HEX 0x0080
#define LED9_HEX 0x0100
#define LED10_HEX 0x0200
#define LED11_HEX 0x0400
#define LED12_HEX 0x0800
#define LED13_HEX 0x1000
#define LED14_HEX 0x2000
#define LED15_HEX 0x4000
#define LED16_HEX 0x8000




extern int I2C_LED_OTOMATIK_ARTIR;
extern int I2C_LED_DELAY_MS;

void I2C_LED_YAK(int led);
void I2C_LED_SONDUR(int led);
void I2C_LED_OTOMATIK_ARTIR_F(int artir);
void I2C_LED_DELAY_F(char* uart1);
void I2C_LED_SIRALI(void);
void LedYak(char* uart1);
void LedSondur(char* uart1);



#endif
