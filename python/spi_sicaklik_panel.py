from PyQt6.QtWidgets import (
    QMainWindow,QWidget,QVBoxLayout,QRadioButton,QPushButton,
    QHBoxLayout,QGridLayout, QSlider, QLabel,
                            )
from degiskenler import  KOMUTLARD,PENCERE_ADLARID,SICAKLIK_STILLERID
from PyQt6.QtCore import QThread
from uart2veriokuma import UART3DEGEROKU


class SPI_SICAKLIK_KONTROL_PANEL(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["sicaklik_kontrol_panel"]
        self.sicaklik_oku = KOMUTLARD["SICAKLIK"]["ISLEM"]["OKU"]
        self.sicaklik_okuma_dur = KOMUTLARD["SICAKLIK"]["ISLEM"]["DUR"]
        self.oku = False
        self.sicaklik_liste = []
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        layoutv = QVBoxLayout()
        
        layout_sirali = QHBoxLayout()
       
        self.artirmali_buton = QPushButton(text="SICAKLIK OKU")
        self.artirmali_buton.setCheckable(True)
        self.artirmali_buton.clicked.connect(lambda x:self.ButonBasildi(
            komut = "1111",
            ))
        self.artirmali_buton.setStyleSheet("background-color:rgb(195,195,195)")
        
        
        self.sicaklik_deger_ = QLabel("   BAŞLATILMADI")
        self.sicaklik_deger_.setStyleSheet("background-color:gray;color:white")
        self.sicaklik_deger_.setFixedSize(100,50)
        
        layout_sirali.addWidget(self.artirmali_buton)
        layout_sirali.addWidget(self.sicaklik_deger_)

 

        layoutv.addLayout(layout_sirali)
        
        widget.setLayout(layoutv)
        
        
        self.setCentralWidget(widget)
        
        

        
        self.show()
        self.parent.sicaklik_kontrol_panel_acik = True
        
        
        
    def ButonBasildi(self,komut:str):   
        if self.artirmali_buton.isChecked():
            sicaklik_oku = self.sicaklik_oku
            self.artirmali_buton.setStyleSheet("background-color:rgb(252,148,148)")
            self.Uart2OkumaIslemci(True)
        else:
            sicaklik_oku = self.sicaklik_okuma_dur
            self.artirmali_buton.setStyleSheet("background-color:rgb(195,195,195)")
            self.Uart2OkumaIslemci(False)
            
        komut = sicaklik_oku+komut
        self.parent.KomutGonder(komut)


    def Uart2OkumaIslemci(self,basla:bool):
        if basla:
            self.thread = QThread()
            self.sicaklik_okur = UART3DEGEROKU(uart=self.parent.uart2)
            self.sicaklik_okur.baslat = basla
            self.sicaklik_okur.moveToThread(self.thread)
            self.thread.started.connect(self.sicaklik_okur.run)
            self.sicaklik_okur.progress.connect(lambda x:self.SicaklikOkundu(x))
            self.sicaklik_okur.finished.connect(self.thread.quit)
            self.sicaklik_okur.finished.connect(self.sicaklik_okur.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            self.sicaklik_okur.baslat = basla

            
            
    def SicaklikOkundu(self,sicaklik):
        sicaklik = str(sicaklik,"utf-8")
        if sicaklik.startswith("SO"):
            sicaklik = sicaklik[2:-1] + " ℃"
            self.sicaklik_deger_.setText("      "+sicaklik)
            self.YaziRenginiBelirle(sicaklik=sicaklik)
    
    def YaziRenginiBelirle(self,sicaklik):
        sicaklik = float(sicaklik[:-2])
        tavan = 125
        aralik = 17
        renk = SICAKLIK_STILLERID["6"]
        tavan_aralik = tavan- aralik
        aralik1 = tavan_aralik - aralik
        aralik2 = aralik1 - aralik
        aralik3 = aralik2 - aralik
        aralik4 = aralik3 - aralik
        aralik5 = aralik4 - aralik
        aralik6 = aralik5 - aralik
        aralik7 = aralik6 - aralik
        aralik8 = aralik7 - aralik
        aralik9 = aralik8 - aralik
        if sicaklik > tavan_aralik:
            renk = SICAKLIK_STILLERID["1"]
        elif sicaklik > aralik1:
            renk = SICAKLIK_STILLERID["2"]
        elif sicaklik > aralik2:
            renk = SICAKLIK_STILLERID["3"]
        elif sicaklik > aralik3:
            renk = SICAKLIK_STILLERID["4"] 
        elif sicaklik > aralik4:
            renk = SICAKLIK_STILLERID["5"]
        elif sicaklik > aralik5:
            renk = SICAKLIK_STILLERID["6"] 
        elif sicaklik > aralik6:
            renk = SICAKLIK_STILLERID["7"]
        elif sicaklik > aralik7:
            renk = SICAKLIK_STILLERID["8"] 
        elif sicaklik > aralik8:
            renk = SICAKLIK_STILLERID["9"] 
        elif sicaklik > aralik9:
            renk = SICAKLIK_STILLERID["10"] 
        elif sicaklik <= aralik9:
            renk = SICAKLIK_STILLERID["11"] 

        self.sicaklik_deger_.setStyleSheet(renk)
        
    def closeEvent(self,event):
        self.parent.sicaklik_kontrol_panel_acik = False
        try: 
            self.Uart2OkumaIslemci(False)
        except:
            pass
        