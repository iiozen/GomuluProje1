import serial

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
        yazi = bytes(yazi,"ascii")
        self.uart.write(yazi)
        
    def Oku(self,adet=2):
        self.uart.read(adet)
        
        

        