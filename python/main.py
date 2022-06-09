from uart import UART,Komut

uart1= UART(port= "COM2",baudrate= 115200,timeout=0.01)
uart2= UART(port= "COM3",baudrate= 115200,timeout=0.01)

Komut(uart1= uart1,uart2= uart2,komut= "L0")

uart1.close()
uart2.close()
