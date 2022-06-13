# from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import  QMainWindow, QPushButton, QVBoxLayout, QWidget , QRadioButton
from uart import Komut

from degiskenler import HABERLESD, KOMUTLARD,  GUI_LABELD

class MainWindow(QMainWindow):
    def __init__(self,uart1,uart2):
        super().__init__()
        self.uart1= uart1
        self.uart2= uart2
        self.komut = Komut(uart1= self.uart1,uart2= self.uart2,zamanasimi=HABERLESD["ZAMAN_ASIMI"])
        
        # BAŞLANGIÇ DEĞERİ
        self.led_secim = KOMUTLARD["LED"]["ISLEM"]["LD_SONDUR"]
        
        self.setWindowTitle("Gömülü yazılım")
        
        layout = QVBoxLayout()
        
        # LED SÖNDÜR RADİO BUTONUNU BAŞLANGIÇ OLARAK İŞARETLEDİM
        LED_SECIM_SONDUR = QRadioButton(GUI_LABELD["LED"]["ISLEM"]["SONDUR"])
        LED_SECIM_SONDUR.clicked.connect(lambda x: self.Led_Secim(KOMUTLARD["LED"]["ISLEM"]["LD_SONDUR"]))
        LED_SECIM_SONDUR.setChecked(True)
        layout.addWidget(LED_SECIM_SONDUR)
        
        LED_SECIM_YAK = QRadioButton(GUI_LABELD["LED"]["ISLEM"]["YAK"])
        LED_SECIM_YAK.clicked.connect(lambda x: self.Led_Secim(KOMUTLARD["LED"]["ISLEM"]["LD_YAK"]))
        layout.addWidget(LED_SECIM_YAK)
        
        LY0 = QPushButton(GUI_LABELD["LED"]["SECIM"]["HEPSI"])
        LY0.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_HEPSI"]))
        layout.addWidget(LY0)
        
        LY1 = QPushButton(GUI_LABELD["LED"]["SECIM"]["MAVI"])
        LY1.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_MAVI"]))
        layout.addWidget(LY1)
        
        LY2 = QPushButton(GUI_LABELD["LED"]["SECIM"]["YESIL"])
        LY2.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_YESIL"]))
        layout.addWidget(LY2)
        
        LY3 = QPushButton(GUI_LABELD["LED"]["SECIM"]["KIRMIZI"])
        LY3.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_KIRMIZI"]))
        layout.addWidget(LY3)
          
        LY4 = QPushButton(GUI_LABELD["LED"]["SECIM"]["SARI"])
        LY4.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_SARI"]))
        layout.addWidget(LY4)
        
        widget = QWidget()
        
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
        
        # LY2 = QPushButton("Yeşil Ledi Yak")
        # LY3 = QPushButton("Kırmızı Ledi Yak")
        # LY4 = QPushButton("Sarı Ledi Yak")
        
        # LS0 = QPushButton("Tüm Ledleri Söndür")
        # LS1 = QPushButton("Mavi Ledi Söndür")
        # LS2 = QPushButton("Yeşil Ledi Söndür")
        # LS3 = QPushButton("Kırmızı Ledi Söndür")
        # LS4 = QPushButton("Sarı Ledi Söndür")
        
        
        # self.setCentralWidget(LY0)
        # self.setCentralWidget(LY1)
        # self.setCentralWidget(LY2)
        # self.setCentralWidget(LY3)
        # self.setCentralWidget(LY4)
        
        # self.setCentralWidget(LS0)
        # self.setCentralWidget(LS1)
        # self.setCentralWidget(LS2)
        # self.setCentralWidget(LS3)
        # self.setCentralWidget(LS4)
        
    def KomutGonder(self,komut:str):
        komut = self.led_secim+komut
        self.komut.Haberles(komut= komut)
        
        
    def Led_Secim(self,secim:str):
        self.led_secim = secim
        
    def IslemPencere(self):
        pass