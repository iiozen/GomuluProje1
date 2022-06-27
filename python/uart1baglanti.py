from PyQt6.QtCore import QObject, pyqtSignal
from uart import Komut
from degiskenler import KOMUTLARD
class UART1BAGLANTI(QObject):
    finished = pyqtSignal(bool)
    def __init__(self,komut:Komut):
        super().__init__()
        self.komut = komut
    def run(self):
        """Long-running task."""
        cevap = self.komut.Haberles(KOMUTLARD["BAGLANTI"])
        self.finished.emit(cevap)
