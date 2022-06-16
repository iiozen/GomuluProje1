from stil import Stil


def WidgetDondurur(widget_d:dict):
    label = widget_d["label"]
    stiller = widget_d["stiller"]
    hiza = widget_d["hiza"]
    
    if stiller!=None:
        stiller = Stil(id=None,stiller=stiller)
    return [label,stiller,hiza]