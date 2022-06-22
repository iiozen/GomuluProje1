from PyQt6.QtWidgets import QFrame,QWidget
from PyQt6.QtCore import QRect
from stil import Stil

class FrameOlustur(QFrame):
    def __init__(self,parent:QWidget,widget_d:dict):
        super().__init__(parent=parent)
        id = widget_d["id"]
        konum = widget_d["konum"]
        stiller = widget_d["stiller"]
        self.setObjectName(id)
        
        if konum!=None:
            self.setGeometry(konum)
        if stiller!=None:
                
            stil = Stil(id=id,stiller=stiller)
            
            self.setStyleSheet(stil)
            
        
        