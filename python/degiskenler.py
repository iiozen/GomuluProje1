from PyQt6.QtCore import QRect,Qt


UARTD={
    "UART1":{
    "PORT":"COM2",
    "BAUDRATE": "115200",
    "TIMEOUT":"0.1"
    },
    "UART2":{
    "PORT":"COM3",
    "BAUDRATE": "115200",
    "TIMEOUT":"1"
    }
}


HABERLESD = {
    "ZAMAN_ASIMI":2,
    "OKUMA_ADET":1,
    "ONAY":b'1',
    "TIMER":1000
}

KOMUTLARD = {
    "BAGLANTI":"BGL000",
    "LED":{
        "ISLEM":{
            "LD_SONDUR":"LS",
            "LD_YAK":"LY",
            "LD_DELAY":"LD"
        },
        "SECIM":{
            "L1":"0100",
            "L2":"0200",
            "L3":"0300",
            "L4":"0400",
            "L5":"0500",
            "L6":"0600",
            "L7":"0700",
            "L8":"0800",
            "L9":"0900",
            "L10":"1000",
            "L11":"1100",
            "L12":"1200",
            "L13":"1300",
            "L14":"1400",
            "L15":"1500",
            "L16":"1600",
            "HEPSI":"0000",
            "SIRALI":"2200"
        }
    },
    "MOTOR":{
        "ISLEM":{
            "SUR":"MS"
        }
    },
    "SICAKLIK":
        {
            "ISLEM":
                {
                    "OKU":"SO",
                    "DUR":"SD"
                }
        },
        "ADC":  
            {
                "ISLEM":
                    {
                        "OKU":"AO",
                        "DUR":"AD"
                    }
            }
}

SICAKLIK_STILLERID = {
    "1":"background-color:gray;color:rgb(255,14,3);font-weight:bold",
    "2":"background-color:gray;color:rgb(253,79,19);font-weight:bold",
    "3":"background-color:gray;color:rgb(252,184,49);font-weight:bold",
    "4":"background-color:gray;color:rgb(254,239,85);font-weight:bold",
    "5":"background-color:gray;color:rgb(255,254,196);font-weight:bold",
    "6":"background-color:gray;color:rgb(255,255,255);font-weight:bold",
    "7":"background-color:gray;color:rgb(211,255,254);font-weight:bold",
    "8":"background-color:gray;color:rgb(163,253,254);font-weight:bold",
    "9":"background-color:gray;color:rgb(123,232,253);font-weight:bold",
    "10":"background-color:gray;color:rgb(95,205,254);font-weight:bold",
    "11":"background-color:gray;color:rgb(71,183,255);font-weight:bold",
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
    "led_kontrol_panel":"LED KONTROL PANELİ",
    "motor_kontrol_panel":"MOTOR SÜRME PANELİ",
    "sicaklik_kontrol_panel":"SICAKLIK KONTROL PANELİ",
    "adc_panel":"ADC PANELİ"
}

QFRAMELERD = {
    "widget_satir":{
        "widget_satir_1":{
        "id":"widget_satir_1",
        "konum":QRect(0,0,960,140),
        "stiller":["border:3px solid white"],
        "widget_sutun":{
                "widget_sutun_1":{
                    "id":"widget_satir_1_sutun_1",
                    "konum":QRect(0,0,320,140),
                    "stiller":["border:3px solid white"]
                },
                "widget_sutun_2":{
                    "id":"widget_satir_1_sutun_2",
                    "konum":QRect(320,0,320,140),
                    "stiller":["border:3px solid white"]
                },
                    "widget_sutun_3":{
                    "id":"widget_satir_1_sutun_3",
                    "konum":QRect(640,0,320,140),
                    "stiller":["border:3px solid white"]
                }
            }
        },
        "widget_satir_2":{
        "id":"widget_satir_2",
        "konum":QRect(0,140,960,100),
        "stiller":["border:3px solid white"],
        "widget_sutun":{
                "widget_sutun_1":{
                    "id":"widget_satir_2_sutun_1",
                    "konum":QRect(0,0,400,100),
                    "stiller":["border:3px solid white"]
                },
                "widget_sutun_2":{
                    "id":"widget_satir_2_sutun_2",
                    "konum":QRect(560,0,400,100),
                    "stiller":["border:3px solid white"]
                }
            }
        },
        "widget_satir_3":{
        "id":"widget_satir_3",
        "konum":QRect(0,240,960,100),
        "stiller":["border:3px solid white"],
        "widget_sutun":{
                "widget_sutun_1":{
                    "id":"widget_satir_3_sutun_1",
                    "konum":QRect(0,0,400,100),
                    "stiller":["border:3px solid white"]
                },
                "widget_sutun_2":{
                    "id":"widget_satir_3_sutun_2",
                    "konum":QRect(560,0,400,100),
                    "stiller":["border:3px solid white"]
                }
            }
        }, 

    }
}


layout_satir_1_sutun_1d = {
    "layout_1_widgetlar":{
            "widget_1":{
            "label":"UART1 ve UART2 BİLGİLERİ",
            "stiller":["font-weight:bold","font-size:10pt"],
            "hiza":Qt.AlignmentFlag.AlignCenter,
                        }
                },
    "layout_2_widgetlar":{
                "widget_1":{
                    "label":UARTD["UART1"]["PORT"],
                    "stiller":None,
                    "hiza":None,
                },
                "widget_2":{
                    "label":UARTD["UART1"]["BAUDRATE"],
                    "stiller":None,
                    "hiza":None,
                },
                "widget_3":{
                    "label":UARTD["UART1"]["TIMEOUT"],
                    "stiller":None,
                    "hiza":None,
                }
            },
        "layout_3_widgetlar":{
                "widget_1":{
                    "label":UARTD["UART2"]["PORT"],
                    "stiller":None,
                    "hiza":None,
                },
                "widget_2":{
                    "label":UARTD["UART2"]["BAUDRATE"],
                    "stiller":None,
                    "hiza":None,
                },
                "widget_3":{
                    "label":UARTD["UART2"]["TIMEOUT"],
                    "stiller":None,
                    "hiza":None,
                }
            }

        
}

layout_satir_1_sutun_2d = {
    "layout_1_widgetlar":
        {
        "widget_1":
            {
            "label":"BEKLİYOR   ",
            "stiller":["font-size:14pt","font-weight:bold","color:gray"],
            "hiza":None,
            },
        "widget_2":
            {
            "label":"Bağlantı Durumu: ",
            "stiller":["font-size:12pt"],
            "hiza":None,
            }
        },
    "layout_2_widgetlar":
        {
        "widget_1":
            {
            "label":"BAĞLANTIYI BAŞLAT",
            "stiller":["font-size:11pt"],
            "hiza":None,
            },
        }
}
layout_satir_1_sutun_3d={
      "layout_1_widgetlar":
          {
        "widget_1":
            {
            "label":"IŞINER İSMAİL ÖZEN",
            "stiller":["font-size:16pt","font-weight:bold"],
            "hiza":None,
            },
        "widget_2":
            {
            "label":"STM32F103C8",
            "stiller":["font-size:12pt","font-style:italic"],
            "hiza":Qt.AlignmentFlag.AlignCenter,
            }
          }
}


layout_satir_2_sutun_1d={
      "layout_1_widgetlar":
          {
        "widget_1":
            {
            "label":"  LED KONTROL PANELİ  ",
            "stiller":["font-size:12pt","font-weight:normal"],
            "hiza":None,
            }
          }
}
layout_satir_2_sutun_2d={
      "layout_1_widgetlar":
          {
        "widget_1":
            {
            "label":"  MOTOR KONTROL PANELİ  ",
            "stiller":["font-size:12pt","font-weight:normal"],
            "hiza":None,
            }
          }
}

layout_satir_3_sutun_1d={
      "layout_1_widgetlar":
          {
        "widget_1":
            {
            "label":"  SICAKLIK KONTROL PANELİ  ",
            "stiller":["font-size:12pt","font-weight:normal"],
            "hiza":None,
            }
          }
}
layout_satir_3_sutun_2d={
      "layout_1_widgetlar":
          {
        "widget_1":
            {
            "label":"  ADC OKUMA PANELİ  ",
            "stiller":["font-size:12pt","font-weight:normal"],
            "hiza":None,
            }
          }
}
QLAYOUTLARD = {
    "layout_satir_1d":{
        "layout_sutun_1d":layout_satir_1_sutun_1d,
        "layout_sutun_2d":layout_satir_1_sutun_2d,
        "layout_sutun_3d":layout_satir_1_sutun_3d
    },
    "layout_satir_2d":{
        "layout_sutun_1d":layout_satir_2_sutun_1d,
        "layout_sutun_2d":layout_satir_2_sutun_2d,
    },
    "layout_satir_3d":{
        "layout_sutun_1d":layout_satir_3_sutun_1d,
        "layout_sutun_2d":layout_satir_3_sutun_2d,
    }
}

DEGISENLABELD={
    "BUTON":
        {
            "BAGLANTI":
                {
                    "BASARILI":"BAĞLANTIYI KES",
                    "BASARISIZ":"ARAMAYI DURDUR"
                }
        },
    "LABEL":
        {
            "BAGLANTI":
                {
                    "BASARILI":
                        {
                            "TEXT":"BAŞARILI",
                            "STIL":["font-size:14pt","font-weight:bold","color:green"]
                        },
                    "BASARISIZ":
                        {
                            "TEXT":"ARANIYOR",
                            "STIL":["font-size:14pt","font-weight:bold","color:red","font-style:italic"]
                        }
                }
        }
}