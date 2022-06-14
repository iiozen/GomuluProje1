from PyQt6.QtWidgets import QMainWindow

class Pencere(QMainWindow):
    def __init__(self,pencere_ad:str,):
        super().__init__()
        
        self.setWindowTitle(pencere_ad)
        
        