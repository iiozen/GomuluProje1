import serial
import time

class UART():
    def __init__(self,uart:dict):
        port = uart["port"]
        baudrate = uart["baudrate"]
        timeout = uart["timeout"]
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



class Komut():
    def __init__(self,uart1,uart2,zamanasimi:int):
        self.uart1 = uart1
        self.uart2 = uart2
        self.zamanasimi = zamanasimi
    def Haberles(self,komut:str):
        yazi = self.GonderimHazirla(komut= komut)
        okuma = 0
        baslangic = time.time()
        while okuma!=b'1':
            okuma = self.GonderveOku(yazi= yazi)
            zaman = time.time()-baslangic
            if (zaman>self.zamanasimi):
                self.ZamanAsimi()
                break
        if okuma == b'1':
            self.BasariliIslem()
            
    def GonderimHazirla(self,komut:str):
        yazi = "\x00".join(komut)
        return yazi
    
    def GonderveOku(self,yazi:str):
        self.uart1.Yaz(yazi = yazi)
        okuma = self.uart2.Oku()
        print(okuma)
        return okuma

    def ZamanAsimi(self):
        print("Zaman Aşımı")
        
    def BasariliIslem(self):
        print("İşlem Başarılı")
