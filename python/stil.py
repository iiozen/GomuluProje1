def Stil(id:str or None,stiller:list):
    if id!=None:
        
        stilb = "#"+id+"{"
        stil= ";".join(stiller)
        stil = stilb+stil+"}"
        
    else:
        stil = ";".join(stiller)
    return stil        