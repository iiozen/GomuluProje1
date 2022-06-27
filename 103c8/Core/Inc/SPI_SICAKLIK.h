#ifndef __I2C_SICAKLIK_DEF__
#define __I2C_SICAKLIK_DEF__




#define TC72_READ_ADRES 0x00
#define TC72_OKUMA_ADET 2

#define SPI_SICAKLIK_OKUMA_DELAY 300


//extern float sicaklik;

extern int SPI_SICAKLIK_OKU;



void SPI_SICAKLIK_ISLEMLER(void);
void SPI_SICAKLIK_BASLAT(int baslat);




#endif
