from PyQt6.QtWidgets import (
    QMainWindow,QWidget,QVBoxLayout,QRadioButton,QPushButton,
    QHBoxLayout,QGridLayout, QSlider, QLabel
                            )
from degiskenler import GUI_LABELD, KOMUTLARD,PENCERE_ADLARID
from PyQt6.QtCore import Qt

class Led_Kontrol_Panel(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["led_kontrol_panel"]
        self.led_yak = KOMUTLARD["LED"]["ISLEM"]["LD_YAK"]
        self.led_sondur = KOMUTLARD["LED"]["ISLEM"]["LD_SONDUR"]
        self.led_delay = KOMUTLARD["LED"]["ISLEM"]["LD_DELAY"]
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        layoutv = QVBoxLayout()
        layouth1 = QHBoxLayout()
        satir_1 = ["L1","L2","L3","L4","L5","L6","L7","L8"]
        for text in satir_1:
            self.ButonOlustur(layout=layouth1,text=text,secim=None)
            
        layouth2 = QHBoxLayout()
        satir_2 = ["L9","L10","L11","L12","L13","L14","L15","L16"]
        for text in satir_2:
            self.ButonOlustur(layout=layouth2,text=text,secim=None)     


 
        layout_orta = QHBoxLayout()
        self.ButonOlustur(layout=layout_orta,text="HEPSİ",secim="HEPSI")
        
        layout_sirali = QHBoxLayout()
        # self.ButonOlustur(layout=layout_sirali,text="ARTIRMALI",secim=None)
        self.artirmali_buton = QPushButton(text="SIRALI")
        self.artirmali_buton.setCheckable(True)
        self.artirmali_buton.clicked.connect(lambda x:self.ButonBasildi(
            komut = KOMUTLARD["LED"]["SECIM"]["SIRALI"],
            buton=self.artirmali_buton))
        self.artirmali_buton.setStyleSheet("background-color:rgb(195,195,195)")
        
        delay_hiz_label = QLabel(text = "GECİKME HIZI: ")
        self.delay_hiz = QSlider(orientation=Qt.Orientation.Horizontal)
        self.delay_hiz.setMinimum(100)
        self.delay_hiz.setMaximum(2000)
        self.delay_hiz.setValue(500)
        self.delay_hiz.sliderReleased.connect(self.DelayYaz)
        self.delay_deger = QLabel()
        self.delay_deger.setText("%d ms"%(self.delay_hiz.value()))
        layout_sirali.addWidget(self.artirmali_buton)
        layout_sirali.addWidget(delay_hiz_label)
        layout_sirali.addWidget(self.delay_hiz)
        layout_sirali.addWidget(self.delay_deger)
 


        
        layoutv.addLayout(layouth1)
        layoutv.addLayout(layout_orta)
        layoutv.addLayout(layouth2)
        layoutv.addLayout(layout_sirali)
        
        widget.setLayout(layoutv)
        
        
        self.setCentralWidget(widget)
        
        self.show()
        self.parent.led_kontrol_panel_acik = True
        
    def DelayYaz(self,):
        gelen = self.delay_hiz.value()
        gelen = str(gelen)
        self.delay_deger.setText("%d ms"%self.delay_hiz.value())
        # if self.artirmali_buton.isChecked():
        led_secim = self.led_delay
        if len(gelen)==3:
            gelen = "0"+gelen
        komut = led_secim+gelen
        self.parent.KomutGonder(komut)

        
    def ButonOlustur(self,layout:QWidget,text:str,secim):
        if secim==None:
            secim = text
        buton = QPushButton(text=text)
        buton.setCheckable(True)
        buton.clicked.connect(lambda x:self.ButonBasildi(komut = KOMUTLARD["LED"]["SECIM"][secim],
                                                         buton=buton))
        buton.setStyleSheet("background-color:rgb(195,195,195)")
        layout.addWidget(buton)
        
        
        
    def ButonBasildi(self,komut:str,buton:QPushButton):
        if buton.isChecked():
            led_secim = self.led_yak
            buton.setStyleSheet("background-color:rgb(252,148,148)")
        else:
            led_secim = self.led_sondur
            buton.setStyleSheet("background-color:rgb(195,195,195)")
            
        komut = led_secim+komut
        self.parent.KomutGonder(komut)
        
        
    def closeEvent(self,event):
        self.parent.led_kontrol_panel_acik = False
        