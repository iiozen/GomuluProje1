from PyQt6.QtCore import QObject, pyqtSignal
from uart import UART
class UART3DEGEROKU(QObject):
    progress = pyqtSignal(bytes)
    finished = pyqtSignal()
    def __init__(self,uart:UART):
        super().__init__()
        self.uart = uart
        self.baslat = True
    def run(self):
        """Long-running task."""
        while self.baslat:
            sicaklik = self.uart.OkuSatir()
            self.progress.emit(sicaklik)
        if not self.baslat:
            self.finished.emit()
