from PyQt6.QtWidgets import (
    QMainWindow,QWidget,QVBoxLayout,QRadioButton,QPushButton,
    QHBoxLayout,QGridLayout, QSlider, QLabel
                            )
from degiskenler import GUI_LABELD, KOMUTLARD,PENCERE_ADLARID
from PyQt6.QtCore import Qt

class SPI_SICAKLIK_KONTROL_PANEL(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["sicaklik_kontrol_panel"]
        self.sicaklik_oku = KOMUTLARD["SICAKLIK"]["ISLEM"]["OKU"]
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        layoutv = QVBoxLayout()
        
        layout_sirali = QHBoxLayout()
       
        self.artirmali_buton = QPushButton(text="SICAKLIK OKU")
        self.artirmali_buton.clicked.connect(lambda x:self.ButonBasildi(
            komut = "1111",
            ))
        self.artirmali_buton.setStyleSheet("background-color:rgb(195,195,195)")
        
        layout_sirali.addWidget(self.artirmali_buton)

 

        layoutv.addLayout(layout_sirali)
        
        widget.setLayout(layoutv)
        
        
        self.setCentralWidget(widget)
        
        self.show()
        self.parent.sicaklik_kontrol_panel_acik = True
        
    # def DelayYaz(self,):
    #     gelen = self.delay_hiz.value()
    #     gelen = str(gelen)
    #     self.delay_deger.setText("%d ms"%self.delay_hiz.value())
    #     # if self.artirmali_buton.isChecked():
    #     led_secim = self.led_delay
    #     if len(gelen)==3:
    #         gelen = "0"+gelen
    #     komut = led_secim+gelen
    #     self.parent.KomutGonder(komut)

      
    # def ButonOlustur(self,layout:QWidget,text:str,secim):
    #     if secim==None:
    #         secim = text
    #     buton = QPushButton(text=text)
    #     buton.setCheckable(True)
    #     buton.clicked.connect(lambda x:self.ButonBasildi(komut = KOMUTLARD["LED"]["SECIM"][secim],
    #                                                      buton=buton))
    #     buton.setStyleSheet("background-color:rgb(195,195,195)")
    #     layout.addWidget(buton)
        
        
        
    def ButonBasildi(self,komut:str):   
        komut = self.sicaklik_oku+komut
        self.parent.KomutGonder(komut)
        
        
    def closeEvent(self,event):
        self.parent.sicaklik_kontrol_panel_acik = False
        