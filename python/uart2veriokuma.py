from PyQt6.QtCore import QObject, pyqtSignal,QRunnable,pyqtSlot
from uart import UART


class SinyalSinif(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(bytes)


class UART3DEGEROKU(QRunnable):

    def __init__(self,uart:UART):
        super().__init__()
        self.uart = uart
        self.baslat = True
        
        self.signals = SinyalSinif()
        
    @pyqtSlot()
    def run(self):
        while self.baslat:
            sicaklik = self.uart.OkuSatir()
            try:
                self.signals.progress.emit(sicaklik)
            except:
                break
            
        if not self.baslat:
            try:
                self.signals.finished.emit()
            except:
                pass
