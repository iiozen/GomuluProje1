from tkinter import Frame
from PyQt6.QtWidgets import (
                            QMainWindow, QPushButton, QVBoxLayout,
                            QWidget , QRadioButton,QFormLayout,
                            QHBoxLayout, QLineEdit, QLabel, QFrame,
                            QLayout, QGridLayout
                            )

from PyQt6.QtCore import Qt

from uart import Komut

from qframe import FrameOlustur

from degiskenler import HABERLESD, KOMUTLARD,  GUI_LABELD, QFRAMELERD

class AnaPencere(QMainWindow):
    def __init__(self,uart):
        super().__init__()
        self.uart= uart
        self.komut = Komut(uart= self.uart,zamanasimi=HABERLESD["ZAMAN_ASIMI"])

        # TÜM WİDGETLERİN PARENTİ OLACAK WİDGET
        ustwidget = QWidget()

        ## WİDGET SATIR  1
        # widget_satir_1 = QWidget(parent=ustwidget)
        # widget_satir_1.setGeometry(0,0,960,140)

        ## WİDGET SATIR 1 QFRAME VERSİYONU
        # widget_satir_1 = QFrame(parent=ustwidget)
        # widget_satir_1.setObjectName("widget_satir_1")
        # widget_satir_1.setGeometry(0,0,960,140)
        # widget_satir_1.setStyleSheet("#widget_satir_1{border:3px solid white}")
        widget_satir_1d = QFRAMELERD["widget_satir"]["widget_satir_1"]
        widget_satir_1 = FrameOlustur(parent=ustwidget,id=widget_satir_1d["id"],konum=widget_satir_1d["konum"],stiller=widget_satir_1d["stiller"])

        # WİDGET SÜTUN 1
        # widget_sutun_1 = QWidget(parent=widget_satir_1)
        # widget_sutun_1.setGeometry(0,0,320,140)
        
        # WİDGET SÜTUN 1 QFRAME VERSİYONU
        widget_sutun_1 = QFrame(parent=widget_satir_1)
        widget_sutun_1.setGeometry(0,0,320,140)
        widget_sutun_1.setObjectName("widget_sutun_1")
        widget_sutun_1.setStyleSheet("#widget_sutun_1{border:3px solid white}")
        
        # WİDGET UART BİLGİLERİ
        widget_uart_bilgiler = QWidget(parent=widget_sutun_1)
        
        layout_sutun_1 = QGridLayout()
        
        layout_uart_baslik = QGridLayout()
        
        uart_label = QLabel(text="UART İLETİŞİM BİLGİLERİ")
        uart_label.setStyleSheet("font-weight:bold;font-size:10pt")
        layout_uart_baslik.addWidget(uart_label)

        uartlayout = QFormLayout()
        uartlayout.setVerticalSpacing(5)
        portinput = QLineEdit()
        portinput.setText("COM2")

        baudinput = QLineEdit()
        baudinput.setText("115200")
        toinput = QLineEdit()
        toinput.setText("0.1")

        uartlayout.addRow("Port:",portinput)
        uartlayout.addRow("Baudrate: ",baudinput)
        uartlayout.addRow("Timeout: ",toinput)
        
        layout_sutun_1.addLayout(layout_uart_baslik,1,1,1,1,Qt.AlignmentFlag.AlignTop)
        layout_sutun_1.addLayout(uartlayout,2,1,1,1,Qt.AlignmentFlag.AlignBottom)
        widget_uart_bilgiler.setLayout(layout_sutun_1)

        self.Ortala(eleman = widget_uart_bilgiler,layout=layout_sutun_1)
        

        # WİDGET SÜTUN 2
        # widget_sutun_2 = QWidget(parent=widget_satir_1)
        # widget_sutun_2.setGeometry(320,0,320,140)

        # WİDGET SÜTUN 2 QFRAME VERSİYONU
        widget_sutun_2 = QFrame(parent=widget_satir_1)
        widget_sutun_2.setGeometry(320,0,320,140)
        widget_sutun_2.setObjectName("widget_sutun_2")
        widget_sutun_2.setStyleSheet("#widget_sutun_2{border:3px solid white}")
        
        # WİDGET BAĞLANTI BİLGİLERİ
        widget_baglanti_bilgiler = QWidget(parent=widget_sutun_2)
        
        layout_sutun_2 = QGridLayout()
        
        layout_baglanti_durumu = QFormLayout()
        
        self.baglanti_durumu = QLabel("Bekliyor")
        self.baglanti_durumu.setStyleSheet("font-size:14pt;font-weight:bold;color:gray")
        baglanti_durumu_label = QLabel("Bağlantı Durumu: ")
        baglanti_durumu_label.setStyleSheet("font-size:12pt")
        layout_baglanti_durumu.addRow(baglanti_durumu_label,self.baglanti_durumu)
        # layout_sutun_2.addWidget(baglanti_durumu_label)
        
        layout_baglanti_buton = QGridLayout()
        self.baglan_buton_label = "BAĞLAN"
        baglan_buton = QPushButton("%s"%self.baglan_buton_label)
        baglan_buton.setStyleSheet("font-size:11pt")
        baglan_buton.setCheckable(False)
        layout_baglanti_buton.addWidget(baglan_buton)

        
        layout_sutun_2.addLayout(layout_baglanti_durumu,1,1,1,1,Qt.AlignmentFlag.AlignTop)
        layout_sutun_2.addLayout(layout_baglanti_buton,2,1,1,1,Qt.AlignmentFlag.AlignBottom) 
        
         
        widget_baglanti_bilgiler.setLayout(layout_sutun_2)
        self.Ortala(eleman=widget_baglanti_bilgiler,layout=layout_sutun_2)



        # WİDGET SÜTUN 3
        widget_sutun_3 = QWidget(parent=widget_satir_1)
        widget_sutun_3.setGeometry(640,0,320,140)
        
        # WİDGET İSİM SOYİSİM
        widget_isim_soyisim = QWidget(parent=widget_sutun_3)
        
        layout_isim_soyisim = QVBoxLayout()
        
        isim_soyisim = QLabel("IŞINER İSMAİL ÖZEN")
        isim_soyisim.setStyleSheet("font-size:16pt;font-weight:bold")
        layout_isim_soyisim.addWidget(isim_soyisim)
        kullanilan_mcu = QLabel("STM32F103C8")
        kullanilan_mcu.setStyleSheet("font-size:12pt;font-style:italic")
        kullanilan_mcu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_isim_soyisim.addWidget(kullanilan_mcu)
        
        widget_isim_soyisim.setLayout(layout_isim_soyisim)
        self.Ortala(eleman=widget_isim_soyisim,layout=layout_isim_soyisim)


        # Ana Widget Ayarları
        self.setCentralWidget(ustwidget)
        self.setGeometry(500,300,960,540)






        ## Buton Sınıfından Çekilerek Yapılacak

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

        LY4 = QPushButton(text= GUI_LABELD["LED"]["SECIM"]["SARI"])
        LY4.clicked.connect(lambda x:self.KomutGonder(KOMUTLARD["LED"]["SECIM"]["LD_SARI"]))
        layout.addWidget(LY4)


    def KomutGonder(self,komut:str):
        komut = self.led_secim+komut
        self.komut.Haberles(komut= komut)


    def Led_Secim(self,secim:str):
        self.led_secim = secim

    def IslemPencere(self):
        pass
    
    def Ortala(self,eleman:QWidget,layout:QLayout):
        parent =eleman.parentWidget()
        a1,b1 = parent.width()/2,parent.height()/2
        layoutsize = layout.sizeHint()
        a,b = layoutsize.width()/2,layoutsize.height()/2
        eleman.move(a1-a,b1-b)
        