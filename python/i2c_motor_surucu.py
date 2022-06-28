from PyQt6.QtWidgets import (
    QMainWindow,QWidget,QVBoxLayout,
    QHBoxLayout, QLabel,QDial
                            )
from degiskenler import  KOMUTLARD,PENCERE_ADLARID

class I2C_MOTOR_SURUCU(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["motor_kontrol_panel"]
        
        self.motor_islem = KOMUTLARD["MOTOR"]["ISLEM"]["SUR"]
        
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        widget = QWidget()
        layoutv = QVBoxLayout()
        
        layout_sirali = QHBoxLayout()
    
        
        self.motor_hiz = QDial()
        self.motor_hiz.setMinimum(0)
        self.motor_hiz.setMaximum(4095)
        self.motor_hiz.setValue(0)
        self.motor_hiz.sliderReleased.connect(self.MotorHizYaz)
        self.delay_deger = QLabel()
        self.delay_deger.setText(f"%{(self.motor_hiz.value()*100/4095):>05.1f}")
        layout_sirali.addWidget(self.motor_hiz)
        layout_sirali.addWidget(self.delay_deger)
 


        
        layoutv.addLayout(layout_sirali)
        
        widget.setLayout(layoutv)
        
        
        
        self.setCentralWidget(widget)
        
        self.show()
        self.parent.motor_surucu_panel_acik = True
        
    def MotorHizYaz(self):
        gelen = self.motor_hiz.value()
        gelen = str(gelen)
        self.delay_deger.setText(f"%{(self.motor_hiz.value()*100/4095):>05.1f}")
        motor_secim = self.motor_islem
        if len(gelen)<4 and gelen!="0000":
            sifirci = 4-len(gelen)
            t = ""
            for i in range(sifirci):
                t = t + "0"
            gelen = t + gelen
        komut = motor_secim+gelen
        self.parent.KomutGonder(komut)
        
    def closeEvent(self,event):
        self.parent.motor_surucu_panel_acik = False
        