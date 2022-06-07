from uart import UART

uart1 = UART(port="COM2",baudrate = 115200,timeout=0.01)
uart2 = UART(port = "COM3",baudrate =115200,timeout=0.01)


uart1.Yaz("1")



uart1.close()
uart2.close()

