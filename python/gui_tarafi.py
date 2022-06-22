from tkinter import Frame
from PyQt6.QtWidgets import (
                            QMainWindow, QPushButton, QVBoxLayout,
                            QWidget , QRadioButton,QFormLayout,
                            QLineEdit, QLabel, QFrame,
                            QLayout, QGridLayout
                            )

from PyQt6.QtCore import Qt, QTimer,QRect
from led_kontrol_panel import Led_Kontrol_Panel
from i2c_motor_surucu import I2C_MOTOR_SURUCU
from stil import Stil

from uart import UART, Komut

from qframe import FrameOlustur
# from widget import WidgetOlusturucu

from degiskenler import DEGISENLABELD, HABERLESD, KOMUTLARD, QFRAMELERD, QLAYOUTLARD
from widget import WidgetDondurur

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.TanimlarBaslangic()

        ### TÜM WİDGETLERİN PARENTİ OLACAK WİDGET
        ustwidget = QWidget()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Baglanti)
        ## QFRAME OLUŞTURMA DEĞİŞKENLERİNİN TANIMLAMALARI
        # QFRAME SATIR DEĞİŞKENLERİ
        self.widget_satird = QFRAMELERD["widget_satir"]
        self.widget_satir_1d = self.widget_satird["widget_satir_1"]
        self.widget_satir_2d = self.widget_satird["widget_satir_2"]
        # QFRAME SÜTUN DEĞİŞKENLERİ   
        self.widget_satir_1_sutund = self.widget_satir_1d["widget_sutun"]
        self.widget_satir_1_sutun_1d = self.widget_satir_1_sutund["widget_sutun_1"]
        self.widget_satir_1_sutun_2d = self.widget_satir_1_sutund["widget_sutun_2"]
        self.widget_satir_1_sutun_3d = self.widget_satir_1_sutund["widget_sutun_3"]
        
        self.widget_satir_2_sutund = self.widget_satir_2d["widget_sutun"]
        self.widget_satir_2_sutun_1d = self.widget_satir_2_sutund["widget_sutun_1"]
        self.widget_satir_2_sutun_2d = self.widget_satir_2_sutund["widget_sutun_2"]
        ## QFRAME SATIR 1
        widget_satir_1 = FrameOlustur(parent=ustwidget,widget_d=self.widget_satir_1d)
              
        # QFRAME SATIR 1 SÜTUN 1 
        widget_satir_1_sutun_1 = FrameOlustur(parent=widget_satir_1,widget_d=self.widget_satir_1_sutun_1d)

        #   SATIR 1 SÜTUN 1     
        widget_uart_bilgiler = QWidget(parent=widget_satir_1_sutun_1)
        layout_satir_1_sutun_1 = QGridLayout()
        self.Satir1_Sutun1(layout_sutun=layout_satir_1_sutun_1)
        widget_uart_bilgiler.setLayout(layout_satir_1_sutun_1)
        self.Ortala(eleman = widget_uart_bilgiler,layout=layout_satir_1_sutun_1)
        

        # QFRAME SATIR 1 SÜTUN 2
        widget_satir_1_sutun_2 = FrameOlustur(parent=widget_satir_1,widget_d=self.widget_satir_1_sutun_2d)
        
        #   SATIR 1 SÜTUN 2
        widget_baglanti_bilgiler = QWidget(parent=widget_satir_1_sutun_2)
        layout_satir_1_sutun_2 = QGridLayout()
        self.Satir1_Sutun2(layout_sutun=layout_satir_1_sutun_2)
        widget_baglanti_bilgiler.setLayout(layout_satir_1_sutun_2)
        self.Ortala(eleman=widget_baglanti_bilgiler,layout=layout_satir_1_sutun_2)

        # QFRAME SATIR 1 SÜTUN 3
        widget_satir_1_sutun_3 = FrameOlustur(parent=widget_satir_1,widget_d=self.widget_satir_1_sutun_3d)

        #   SATIR 1 SÜTUN 3
        widget_isim_soyisim = QWidget(parent=widget_satir_1_sutun_3)
        layout_satir_1_sutun_3 = QVBoxLayout()
        self.Satir1_Sutun3(layout_satir_1_sutun_3)
        widget_isim_soyisim.setLayout(layout_satir_1_sutun_3)
        self.Ortala(eleman=widget_isim_soyisim,layout=layout_satir_1_sutun_3)

        ## QFRAME SATIR 2
        widget_satir_2 = FrameOlustur(parent=ustwidget,widget_d=self.widget_satir_2d)

        # SATIR 2 ORTAK BAŞLIK OLUŞTURMA
        self.SatirBaslikOlustur(widget_satir_2,"I2C")
        
        # QFRAME SATIR 2 SÜTUN 1 
        widget_satir_2_sutun_1 = FrameOlustur(parent=widget_satir_2,widget_d=self.widget_satir_2_sutun_1d)

        #   SATIR 2 SÜTUN 1
        widget_led_kontrol_panel = QWidget(parent=widget_satir_2_sutun_1)
        layout_satir_2_sutun_1 = QGridLayout()
        self.Satir2_Sutun1(layout_sutun=layout_satir_2_sutun_1)
        widget_led_kontrol_panel.setLayout(layout_satir_2_sutun_1)
        self.Ortala(eleman=widget_led_kontrol_panel,layout=layout_satir_2_sutun_1)
        
        
        
        # QFRAME SATIR 2 SÜTUN 2
        widget_satir_2_sutun_2 = FrameOlustur(parent=widget_satir_2,widget_d=self.widget_satir_2_sutun_2d)
        
        #   SATIR 2 SÜTUN 2
        widget_i2c_motor_surucu = QWidget(parent=widget_satir_2_sutun_2)
        layout_satir_2_sutun_2 = QGridLayout()
        self.Satir2_Sutun2(layout_sutun=layout_satir_2_sutun_2)
        widget_i2c_motor_surucu.setLayout(layout_satir_2_sutun_2)
        self.Ortala(eleman=widget_i2c_motor_surucu,layout=layout_satir_2_sutun_2)
        
        # Ana Widget Ayarları
        self.setCentralWidget(ustwidget)
        self.setGeometry(500,300,960,540)
        self.setWindowTitle("Gömülü yazılım")


        



        ## Buton Sınıfından Çekilerek Yapılacak

        # BAŞLANGIÇ DEĞERİ
        

    def SatirBaslikOlustur(self,parent:QWidget,text:str):
        layout = QGridLayout(parent=parent)
        baslik = QLabel(text=text)
        baslik.setStyleSheet("font-weight:bold;font-size:12pt")
        layout.addWidget(baslik)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
    def TanimlarBaslangic(self):
        self.ilkbaglanti = True
        self.baglanti_buton_basildi=False
        self.led_kontrol_panel_acik = False
        self.motor_surucu_panel_acik = False
        


    def KomutGonder(self,komut:str):
        self.KomutVar(True)
        basari = self.komut.Haberles(komut= komut)
        if not basari:
            self.Baglanti()
        self.KomutVar(False)
        


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
        
        
    def Satir1_Sutun1(self,layout_sutun):
        layout_sutun = layout_sutun
        layout_baslik = QGridLayout()
        layout_uart = QFormLayout()
        
        #   SATIR 1 SÜTUN 1 WİDGET TANIMLARININ ÇAĞIRILMASI
        sutun_d = QLAYOUTLARD["layout_satir_1d"]["layout_sutun_1d"]
        layout_1d = sutun_d["layout_1_widgetlar"]
        layout_2d = sutun_d["layout_2_widgetlar"]
        
        
        layout_1_widget_1d = layout_1d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_1_widget_1d)
        uart_label = QLabel(text=text)
        uart_label.setStyleSheet(stil)
        uart_label.setAlignment(hiza)
        layout_baslik.addWidget(uart_label)

        layout_2_widget_1d = layout_2d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_2_widget_1d)
        self.portinput = QLineEdit()
        self.portinput.setText(text)

        layout_2_widget_2d = layout_2d["widget_2"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_2_widget_2d)
        self.baudinput = QLineEdit()
        self.baudinput.setText(text)
        
        layout_2_widget_3d = layout_2d["widget_3"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_2_widget_3d)
        self.toinput = QLineEdit()
        self.toinput.setText(text)

        layout_uart.addRow("Port:",self.portinput)
        layout_uart.addRow("Baudrate: ",self.baudinput)
        layout_uart.addRow("Timeout: ",self.toinput)
        
        layout_sutun.addLayout(layout_baslik,1,1,1,1,Qt.AlignmentFlag.AlignTop)
        layout_sutun.addLayout(layout_uart,2,1,1,1,Qt.AlignmentFlag.AlignBottom)
    
    
    def Satir1_Sutun2(self,layout_sutun):
        layout_sutun = layout_sutun
        layout_baglanti_durumu = QFormLayout()
        layout_baglanti_buton = QGridLayout()
        
        #   SATIR 1 SÜTUN 2 WİDGET TANIMLARININ ÇAĞIRILMASI
        sutun_d = QLAYOUTLARD["layout_satir_1d"]["layout_sutun_2d"]
        layout_1d = sutun_d["layout_1_widgetlar"]
        layout_2d = sutun_d["layout_2_widgetlar"]
        
        layout_1_widget_1d = layout_1d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_1_widget_1d)
        self.baglanti_durumu = QLabel(text=text)
        self.baglanti_durumu.setStyleSheet(stil)
        
        layout_1_widget_2d = layout_1d["widget_2"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_1_widget_2d)
        baglanti_durumu_label = QLabel(text=text)
        baglanti_durumu_label.setStyleSheet(stil)
        layout_baglanti_durumu.addRow(baglanti_durumu_label,self.baglanti_durumu)
        
        
        layout_2_widget_1d = layout_2d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d = layout_2_widget_1d)
        self.baglan_buton = QPushButton(text)
        self.baglan_buton.setStyleSheet(stil)
        self.baglan_buton.setCheckable(False)
        self.baglan_buton.clicked.connect(self.BaglantiButonConnect)
        layout_baglanti_buton.addWidget(self.baglan_buton)

        
        layout_sutun.addLayout(layout_baglanti_durumu,1,1,1,1,Qt.AlignmentFlag.AlignTop)
        layout_sutun.addLayout(layout_baglanti_buton,2,1,1,1,Qt.AlignmentFlag.AlignBottom) 
        
    
    def Satir1_Sutun3(self,layout_sutun):
        layout_sutun = layout_sutun

        #   SATIR 1 SÜTUN 3 WİDGET TANIMLARININ ÇAĞIRILMASI
        sutun_d = QLAYOUTLARD["layout_satir_1d"]["layout_sutun_3d"]
        layout_1d = sutun_d["layout_1_widgetlar"]
        
        layout_1_widget_1d = layout_1d["widget_1"]        
        text,stil,hiza = WidgetDondurur(widget_d = layout_1_widget_1d)
        isim_soyisim = QLabel(text)
        isim_soyisim.setStyleSheet(stil)
        layout_sutun.addWidget(isim_soyisim)
        
        layout_1_widget_2d = layout_1d["widget_2"]        
        text,stil,hiza = WidgetDondurur(widget_d = layout_1_widget_2d)
        kullanilan_mcu = QLabel(text)
        kullanilan_mcu.setStyleSheet(stil)
        kullanilan_mcu.setAlignment(hiza)
        layout_sutun.addWidget(kullanilan_mcu)
        
        
        
    def Satir2_Sutun1(self,layout_sutun:QWidget):
        layout_sutun=layout_sutun
        
        #   SATIR 2 SÜTUN 1 WİDGET TANIMLARININ ÇAĞIRILMASI
        sutun_d = QLAYOUTLARD["layout_satir_2d"]["layout_sutun_1d"]
        layout_1d = sutun_d["layout_1_widgetlar"]
        
        layout_1_widget_1d= layout_1d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d=layout_1_widget_1d)
        self.led_kontrol_panel = QPushButton(text)
        self.led_kontrol_panel.setStyleSheet(stil)
        self.led_kontrol_panel.setCheckable(False)
        self.led_kontrol_panel.setDisabled(True)
        self.led_kontrol_panel.clicked.connect(lambda x:self.LedKontrolPanel(layout_sutun=layout_sutun,buton = self.led_kontrol_panel))
        layout_sutun.addWidget(self.led_kontrol_panel)
        
        
    def Satir2_Sutun2(self,layout_sutun:QWidget):
        layout_sutun=layout_sutun
        
        #   SATIR 2 SÜTUN 2 WİDGET TANIMLARININ ÇAĞIRILMASI
        sutun_d = QLAYOUTLARD["layout_satir_2d"]["layout_sutun_2d"]
        layout_1d = sutun_d["layout_1_widgetlar"]
        
        layout_1_widget_1d= layout_1d["widget_1"]
        text,stil,hiza = WidgetDondurur(widget_d=layout_1_widget_1d)
        self.motor_surucu_panel = QPushButton(text)
        self.motor_surucu_panel.setStyleSheet(stil)
        self.motor_surucu_panel.setCheckable(False)
        self.motor_surucu_panel.setDisabled(True)
        self.motor_surucu_panel.clicked.connect(lambda x:self.MotorKontrolPanel(layout_sutun=layout_sutun,buton = self.motor_surucu_panel))
        layout_sutun.addWidget(self.motor_surucu_panel)
        
        
        
        
        
        
        

        
        
        
        
        
        
        
    def Panel_Butonlar(self,aktif:bool):
        if aktif:
            self.led_kontrol_panel.setEnabled(True)
            self.motor_surucu_panel.setEnabled(True)
            
        else:
            self.led_kontrol_panel.setEnabled(False)
            self.motor_surucu_panel.setEnabled(False)
            self.Panel_Pencereler()
            
            
    def Panel_Pencereler(self):
        if self.led_kontrol_panel_acik:
            self.led_kontrol_panel_pencere.close()
        if self.motor_surucu_panel_acik:
            self.motor_surucu_panel_pencere.close()
        
        
    def LedKontrolPanel(self,layout_sutun:QWidget,buton:QWidget):
        if not self.led_kontrol_panel_acik:
            self.led_kontrol_panel_pencere = Led_Kontrol_Panel(parent=self)
            self.Panel_Konumlandir(panel = self.led_kontrol_panel_pencere,satir=self.widget_satir_2d,sutun=self.widget_satir_2_sutun_1d,layout_sutun=layout_sutun,buton=buton)
        else:
            self.led_kontrol_panel_pencere.close()
        
    def MotorKontrolPanel(self,layout_sutun:QWidget,buton:QWidget):
        if not self.motor_surucu_panel_acik:
            self.motor_surucu_panel_pencere = I2C_MOTOR_SURUCU(parent=self)
            self.Panel_Konumlandir(panel = self.motor_surucu_panel_pencere,satir=self.widget_satir_2d,sutun=self.widget_satir_2_sutun_2d,layout_sutun=layout_sutun,buton=buton)
        else:
            self.motor_surucu_panel_pencere.close()
        

    def Panel_Konumlandir(self,panel:QMainWindow,satir:dict,sutun:dict,layout_sutun:QWidget,buton:QWidget):
        x,y,x_,y_ = self.geometry().getRect()
        x1,y1,x1_,y1_ = satir["konum"].getRect()
        x2,y2,x2_,y2_ = sutun["konum"].getRect()
        x3,y3,x3_,y3_ = layout_sutun.parent().geometry().getRect()
        x4,y4,x4_,y4_ = buton.geometry().getRect()
        
        panel_x = x+x1+x2+x3+x3_
        panel_y = y+y1+y2+y3+y4

        panel.move(panel_x,panel_y)












        
        
        
        
    def BaglantiButonConnect(self):
        if self.baglanti_buton_basildi:
            self.BaglantiDurdur()
        else:
            self.Baglanti()
        self.baglanti_buton_basildi = not self.baglanti_buton_basildi
        
        
    def Baglanti(self):
        self.KomutVar(True)
        if not self.ilkbaglanti:
            if self.uart.is_open:
                self.uart.close()
        self.uart = UART(port=self.portinput.text(),baudrate=float(self.baudinput.text()),timeout=float(self.toinput.text()))
        buton = DEGISENLABELD["BUTON"]
        label = DEGISENLABELD["LABEL"]
        if self.uart.baglandi:
            self.komut = Komut(uart= self.uart,zamanasimi=HABERLESD["ZAMAN_ASIMI"])
            basari = self.komut.Haberles(KOMUTLARD["BAGLANTI"])
            if basari:
                self.Basari(buton=buton,label=label)
            else:
                self.Basarisiz(buton=buton,label=label)
        else:
            self.Basarisiz(buton=buton,label=label)

        ## BAĞLANTI BAŞARILI OLUNCAYA KADAR DİĞER TÜM BUTONLAR DİSABLE MODDA OLACAK
        
        self.ilkbaglanti=False
        self.LineEditYazilabilirlik(False)
        self.KomutVar(False)
        
        
    def StartStopTimer(self,start:bool):
        #   TIMER INTERRUPT İLE HER İSTENİLEN SANİYEDE BİR ÇALIŞAN KOMUT YOK İSE BAĞLANTI KONTROL EDİLECEK
        timeout = HABERLESD["TIMER"]
        if start:
            self.timer.start(timeout)
        else:
            self.timer.stop()
        
    def Basari(self,buton:dict,label:dict):
        self.Panel_Butonlar(True)
        
        basarili_buton_text = buton["BAGLANTI"]["BASARILI"]
        basarili_baglanti_durumu = label["BAGLANTI"]["BASARILI"]
        basarili_baglanti_durumu_text = basarili_baglanti_durumu["TEXT"]
        stiller = basarili_baglanti_durumu["STIL"]
        basarili_baglanti_durumu_stil = Stil(id=None,stiller=stiller)
        self.baglan_buton.setText(basarili_buton_text)
        self.baglanti_durumu.setText(basarili_baglanti_durumu_text)
        self.baglanti_durumu.setStyleSheet(basarili_baglanti_durumu_stil)
        
    def Basarisiz(self,buton:dict,label:dict):
        self.Panel_Butonlar(False)
        
        basarisiz_buton_text = buton["BAGLANTI"]["BASARISIZ"]
        basarisiz_baglanti_durumu = label["BAGLANTI"]["BASARISIZ"]
        basarisiz_baglanti_durumu_text = basarisiz_baglanti_durumu["TEXT"]
        stiller = basarisiz_baglanti_durumu["STIL"]
        basarisiz_baglanti_durumu_stil = Stil(id=None,stiller=stiller)
        self.baglan_buton.setText(basarisiz_buton_text)
        self.baglanti_durumu.setText(basarisiz_baglanti_durumu_text)
        self.baglanti_durumu.setStyleSheet(basarisiz_baglanti_durumu_stil)
        
    def BaglantiDurdur(self):
        self.Panel_Butonlar(False)
        
        self.timer.stop()
        if not self.ilkbaglanti:
            if self.uart.is_open:
                self.uart.close()
        buton = QLAYOUTLARD["layout_satir_1d"]["layout_sutun_2d"]["layout_2_widgetlar"]["widget_1"]
        durum = QLAYOUTLARD["layout_satir_1d"]["layout_sutun_2d"]["layout_1_widgetlar"]["widget_1"]
        # BUTON EN BAŞTAKİ HALE GETİRİLDİ
        text,stil,hiza = WidgetDondurur(widget_d = buton)
        self.baglan_buton.setText(text)
        self.baglan_buton.setStyleSheet(stil)
        
        # DURUM LABEL EN BAŞTAKİ HALE GETİRİLDİ
        text,stil,hiza = WidgetDondurur(widget_d = durum)
        self.baglanti_durumu.setText(text)
        self.baglanti_durumu.setStyleSheet(stil)
        
        self.LineEditYazilabilirlik(True)
        
    def KomutVar(self,islemdemi:bool):
        if islemdemi:
            self.StartStopTimer(False)           
        else:
            self.StartStopTimer(True)
            
    def LineEditYazilabilirlik(self,olsun:bool):
        if olsun:
            self.portinput.setEnabled(True)
            self.baudinput.setEnabled(True)
            self.toinput.setEnabled(True)
        else:
            self.portinput.setDisabled(True)
            self.baudinput.setDisabled(True)
            self.toinput.setDisabled(True)
            
            
    def closeEvent(self,event):
        if not self.ilkbaglanti:
            if self.uart.is_open:
                self.uart.close()