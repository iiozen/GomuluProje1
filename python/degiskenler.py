from PyQt6.QtCore import QRect

UARTD={
    "UART":{
        "PORT":"COM2",
        "BAUDRATE": 115200,
        "TIMEOUT":0.1
    }
}


HABERLESD = {
    "ZAMAN_ASIMI":1,
    "OKUMA_ADET":1,
    "ONAY":b'1'
}

KOMUTLARD = {
    "LED":{
        "ISLEM":{
            "LD_SONDUR":"LS",
            "LD_YAK":"LY"
        },
        "SECIM":{
            "LD_HEPSI":"0",
            "LD_MAVI":"1",
            "LD_YESIL":"2",
            "LD_KIRMIZI":"3",
            "LD_SARI":"4"
        }
    }
}


GUI_LABELD = {
    "LED":{
        "ISLEM":{
            "SONDUR":"SÖNDÜR",
            "YAK":"YAK"
        },
        "SECIM":{
            "HEPSI":"HEPSİ",
            "MAVI":"MAVİ",
            "YESIL":"YEŞİL",
            "KIRMIZI":"KIRMIZI",
            "SARI":"SARI"
        }
    }
}

PENCERE_ADLARID={
    "BASLANGIC":"Bağlantı Başlat"
}

QFRAMELERD = {
    "widget_satir":{
        "widget_satir_1":{
        "id":"widget_satir_1",
        "konum":QRect(0,0,960,140),
        "stiller":["border:3px solid white"]
        },
        "widget_sutun":{
                "widget_sutun_1":{
                    
                }
            }

    }
}