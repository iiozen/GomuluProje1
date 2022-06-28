from PyQt6.QtWidgets import (
    QMainWindow        )
from degiskenler import  KOMUTLARD,PENCERE_ADLARID

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        

class SPI_ADC_PANEL(QMainWindow):
    def __init__(self,parent:QMainWindow):
        super().__init__(parent=parent)
        pencere_ad = PENCERE_ADLARID["adc_panel"]
        self.adc_oku = KOMUTLARD["ADC"]["ISLEM"]["OKU"]
        self.adc_okuma_dur = KOMUTLARD["ADC"]["ISLEM"]["DUR"]
        self.oku = False
        self.adc_liste = []
        self.adc_liste_beyaz =[3 for x in range(100)]
        self.adc_grafik_x = list(range(100))
        self.setWindowTitle(pencere_ad)
        self.parent = parent
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        
        self.setCentralWidget(self.canvas)
        
        adc_oku = self.adc_oku
        
        komut = "1111"
        self.Uart2OkumaIslemci()
        komut = adc_oku+komut
        self.parent.KomutGonder(komut)
        
        self.show()
        self.parent.adc_panel_acik = True
        
        
        
        
    def Uart2OkumaIslemci(self):
        self.parent.Uart2_Veri_Oku(True)
        self.adc_connection = self.parent.uart2_veri_okur.signals.progress.connect(lambda x:self.ADCOkundu(x))

            
    def ADCOkundu(self,adc):
        adc = str(adc,"utf-8")
        if adc.startswith("AO"):
            adc = adc[2:]
            self.GrafikCiz(adc=adc)
        
    def GrafikCiz(self,adc):
        try:
            adc = float(adc)
            if len(self.adc_liste)>=100:
                self.adc_liste = self.adc_liste[1:] + [adc]
            else:
                self.adc_liste.append(adc)
            self.canvas.axes.cla()
            self.canvas.axes.plot(self.adc_grafik_x, self.adc_liste_beyaz, 'w')
            uz = list(range(len(self.adc_liste)))
            self.canvas.axes.plot(uz, self.adc_liste, 'r')
            self.canvas.draw()   
        except:
            pass


        
    def closeEvent(self,event):
        self.parent.uart2_veri_okur.signals.disconnect(self.adc_connection)

        self.parent.Uart2_Veri_Oku(False)

        adc_oku = self.adc_okuma_dur
        komut = "1111"
        komut = adc_oku+komut
        self.parent.KomutGonder(komut)
        self.parent.adc_panel_acik = False
        

        