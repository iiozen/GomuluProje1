from PyQt6.QtWidgets import QFrame,QWidget
from PyQt6.QtCore import QRect

class FrameOlustur(QFrame):
    def __init__(self,parent:QWidget,id:str,konum,stiller:list):
        super().__init__(parent=parent)
        self.setObjectName(id)
        
        if konum!=None:
            self.setGeometry(konum)
        
        stilb = "#"+id+"{"
        stil= ";".join(stiller)
        stil = stilb+stil+"}"
        
        print(stil)
        self.setStyleSheet(stil)
        
        
        