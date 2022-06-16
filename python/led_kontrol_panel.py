from PyQt6.QtWidgets import QMainWindow,QWidget,QVBoxLayout,QRadioButton,QPushButton
from degiskenler import GUI_LABELD, KOMUTLARD,PENCERE_ADLARID

class Led_Kontrol_Panel(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["led_kontrol_panel"]
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        layout = QVBoxLayout()

        # LED SÖNDÜR RADİO BUTONUNU BAŞLANGIÇ OLARAK İŞARETLEDİM
        LED_SECIM_SONDUR = QRadioButton(GUI_LABELD["LED"]["ISLEM"]["SONDUR"])
        LED_SECIM_SONDUR.clicked.connect(lambda x: self.parent.Led_Secim(KOMUTLARD["LED"]["ISLEM"]["LD_SONDUR"]))
        LED_SECIM_SONDUR.setChecked(True)
        layout.addWidget(LED_SECIM_SONDUR)

        LED_SECIM_YAK = QRadioButton(GUI_LABELD["LED"]["ISLEM"]["YAK"])
        LED_SECIM_YAK.clicked.connect(lambda x: self.parent.Led_Secim(KOMUTLARD["LED"]["ISLEM"]["LD_YAK"]))
        layout.addWidget(LED_SECIM_YAK)

        LY0 = QPushButton(GUI_LABELD["LED"]["SECIM"]["HEPSI"])
        LY0.clicked.connect(lambda x:self.parent.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_HEPSI"]))
        layout.addWidget(LY0)

        LY1 = QPushButton(GUI_LABELD["LED"]["SECIM"]["MAVI"])
        LY1.clicked.connect(lambda x:self.parent.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_MAVI"]))
        layout.addWidget(LY1)

        LY2 = QPushButton(GUI_LABELD["LED"]["SECIM"]["YESIL"])
        LY2.clicked.connect(lambda x:self.parent.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_YESIL"]))
        layout.addWidget(LY2)

        LY3 = QPushButton(GUI_LABELD["LED"]["SECIM"]["KIRMIZI"])
        LY3.clicked.connect(lambda x:self.parent.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_KIRMIZI"]))
        layout.addWidget(LY3)

        LY4 = QPushButton(text= GUI_LABELD["LED"]["SECIM"]["SARI"])
        LY4.clicked.connect(lambda x:self.parent.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_SARI"]))
        layout.addWidget(LY4)
        
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
        self.show()
        self.parent.led_kontrol_panel_acik = True
        
        
    def closeEvent(self,event):
        self.parent.led_kontrol_panel_acik = False
        