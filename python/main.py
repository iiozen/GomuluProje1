import sys
from gui_tarafi import AnaPencere

from PyQt6.QtWidgets import QApplication

uygulama = QApplication(sys.argv)

anapencere = AnaPencere()
anapencere.show()


uygulama.exec()

