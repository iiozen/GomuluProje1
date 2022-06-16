import serial
import time

from degiskenler import HABERLESD

class UART():
    def __init__(self,port:str,baudrate:int,timeout:int):
        self.baglandi = False
        try:
            self.uart = serial.Serial(port=port,baudrate=baudrate,timeout=timeout)
            self.baglandi = True
            self.is_open = self.acikmi()
        except:
            self.baglandi = False
            self.is_open = False
            
            
        

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



class Komut():
    def __init__(self,uart,zamanasimi:int):
        self.uart = uart
        self.zamanasimi = zamanasimi
    def Haberles(self,komut:str):
        yazi = self.GonderimHazirla(komut= komut)
        okuma = 0
        baslangic = time.time()
        while okuma!=HABERLESD["ONAY"]:
            okuma = self.GonderveOku(yazi= yazi)
            zaman = time.time()-baslangic
            if (zaman>self.zamanasimi):
                return False
        if okuma == HABERLESD["ONAY"]:
            return True            
    def GonderimHazirla(self,komut:str):
        yazi = "\x00".join(komut)
        return yazi
    
    def GonderveOku(self,yazi:str):
        self.uart.Yaz(yazi = yazi)
        okuma = self.uart.Oku(adet= HABERLESD["OKUMA_ADET"])
        return okuma

    def ZamanAsimi(self):
        print("Zaman Aşımı")
        
    def BasariliIslem(self):
        print("İşlem Başarılı")
