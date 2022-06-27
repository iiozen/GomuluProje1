from PyQt6.QtCore import QObject,QRunnable, pyqtSignal,pyqtSlot
from uart import Komut
from degiskenler import KOMUTLARD

class SinyalSinif2(QObject):
    finished = pyqtSignal(bool)




class UART1BAGLANTI(QRunnable):
    def __init__(self,komut:Komut):
        super().__init__()
        self.komut = komut
        
        self.signals = SinyalSinif2()
        
        
    @pyqtSlot()
    def run(self):
        cevap = self.komut.Haberles(KOMUTLARD["BAGLANTI"])
        self.signals.finished.emit(cevap)
