import sys

from uart import UART
from degiskenler import UARTD

from gui_tarafi import AnaPencere

from PyQt6.QtWidgets import QApplication

uart= UART(uart= UARTD["UART"])


uygulama = QApplication(sys.argv)

anapencere = AnaPencere(uart=uart)
anapencere.show()


uygulama.exec()

uart.close()
