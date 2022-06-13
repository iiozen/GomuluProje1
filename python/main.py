import sys

from uart import UART
from degiskenler import UARTD

from gui_tarafi import MainWindow

from PyQt6.QtWidgets import QApplication

uart1= UART(uart= UARTD["UART1"])
uart2= UART(uart= UARTD["UART2"])

uygulama = QApplication(sys.argv)

pencere = MainWindow(uart1=uart1, uart2= uart2)
pencere.show()


uygulama.exec()

uart1.close()
uart2.close()
