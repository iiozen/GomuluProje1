from uart import UART,Komut
from degiskenler import HABERLESD,UARTD

uart1= UART(uart= UARTD["uart1"])
uart2= UART(uart= UARTD["uart2"])

komut = Komut(uart1= uart1,uart2= uart2,zamanasimi=HABERLESD["zamanasimi"])
komut.Haberles(komut= "L1")

uart1.close()
uart2.close()
