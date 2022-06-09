import serial
import time

class UART():
    def __init__(self,port:str,baudrate:int,timeout=float):
        self.uart = serial.Serial(port=port,baudrate=baudrate,timeout=timeout)
        self.is_open = self.acikmi()

    def close(self):
        self.uart.close()
        self.is_open = self.acikmi()
        
    def acikmi(self):
        return self.uart.is_open
        
    def Yaz(self,yazi:str):
        
        yazi = bytes(yazi,"utf-8")
        self.uart.write(yazi)
        
        
    def Oku(self,adet=1):
        return self.uart.read(adet)


   
def Komut(uart1,uart2,komut:str):
    yazi = ""
    okuma = 0
    baslangic = time.time()
    yazi = "\x00".join(komut)
    
    while not okuma:
        uart1.Yaz(yazi = yazi)
        try:
            okuma = int(uart2.Oku())
        except:
            pass
        zaman = time.time()-baslangic
        if (zaman>1):
            ZamanAsimi()
            break
    
    if okuma ==1:
        BasariliIslem()


def ZamanAsimi():
    print("Zaman Aşımı")
def BasariliIslem():
    print("İşlem Başarılı")
