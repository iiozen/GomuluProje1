from base64 import encode
import serial
import io
import sys
if sys.version_info[0]>=3:
    unicode = str

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
        print(yazi)
        self.uart.write(yazi)
        
        # yazi = yazi.encode("ascii")
        # print(yazi)
        # self.uart.write(yazi)
        
        # sio = io.TextIOWrapper(io.BufferedRWPair(self.uart,self.uart))
        # sio.write(unicode(yazi))
        # sio.flush()
        
        
    def Oku(self,adet=2):
        # sio = io.TextIOWrapper(io.BufferedRWPair(self.uart,self.uart))
        # sio.flush()
        # return sio.read(adet)
        return self.uart.read(adet)
    
    
    
def Komut(uart1,uart2,komut:str):
    uart1.Yaz(komut)
    print(uart2.Oku())
    
    # for i in komut:
    #     gelen = None
    #     while(gelen!=i):
    #         uart1.Yaz(yazi=i)
    #         gelen = uart2.Oku()
        