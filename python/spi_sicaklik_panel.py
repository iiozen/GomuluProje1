from PyQt6.QtWidgets import (
    QMainWindow,QWidget,
    QHBoxLayout, QLabel,
                            )
from degiskenler import  KOMUTLARD,PENCERE_ADLARID,SICAKLIK_STILLERID


class SPI_SICAKLIK_KONTROL_PANEL(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["sicaklik_kontrol_panel"]
        self.sicaklik_oku = KOMUTLARD["SICAKLIK"]["ISLEM"]["OKU"]
        self.sicaklik_okuma_dur = KOMUTLARD["SICAKLIK"]["ISLEM"]["DUR"]
        self.oku = False
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        
        layout_sirali = QHBoxLayout()
        
        self.sicaklik_deger_ = QLabel("   BAŞLATILMADI")
        self.sicaklik_deger_.setStyleSheet("background-color:gray;color:white;font-weight:bold")
        self.sicaklik_deger_.setFixedSize(100,50)
        
        layout_sirali.addWidget(self.sicaklik_deger_)
        
        widget.setLayout(layout_sirali)
        
        self.setCentralWidget(widget)
        
        sicaklik_oku = self.sicaklik_oku
        
        komut = "1111"
        self.Uart2OkumaIslemci()
        komut = sicaklik_oku+komut
        self.parent.KomutGonder(komut)
        
        self.show()
        self.parent.sicaklik_kontrol_panel_acik = True
        
        
        
    def Uart2OkumaIslemci(self):
        self.parent.Uart2_Veri_Oku(True)
        self.sicaklik_connection = self.parent.uart2_veri_okur.signals.progress.connect(lambda x:self.SicaklikOkundu(x))
        
            
    def SicaklikOkundu(self,sicaklik):
        sicaklik = str(sicaklik,"utf-8")
        if sicaklik.startswith("SO"):
            sicaklik = sicaklik[2:-1] + " ℃"
            self.sicaklik_deger_.setText("      "+sicaklik)
            self.YaziRenginiBelirle(sicaklik=sicaklik)
    
    def YaziRenginiBelirle(self,sicaklik):
        try:
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
        except:
            pass
        
    def closeEvent(self,event):
        self.parent.uart2_veri_okur.signals.disconnect(self.sicaklik_connection)
   

        self.parent.Uart2_Veri_Oku(False)
    
        sicaklik_oku = self.sicaklik_okuma_dur
        komut = "1111"
        komut = sicaklik_oku+komut
        self.parent.KomutGonder(komut)
        self.parent.sicaklik_kontrol_panel_acik = False
        
