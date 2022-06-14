from PyQt6.QtWidgets import QPushButton

class Pbuton(QPushButton):
    def __init__(self,buton_adlari):
        butonlar = []
        for buton_adi in buton_adlari:            
            butonlar.append(super().__init__(buton_adi))
        return butonlar
            
            
