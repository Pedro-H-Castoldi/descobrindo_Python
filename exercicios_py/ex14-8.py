def gasolina(dkm, qgasto=1):
    kml = (dkm/qgasto)
    if kml < 8:
        return f'O consumo é de {kml}km/l. \033[1;31mVENDA O CARRO\033[m'
    elif kml >= 8 and kml <= 14:
        return f'O consumo é de {kml}km/l. \033[1;33mECONÔMICO\033[m'
    return f'O consumo é de {kml}km/l. \033[1;36mSUPER ECONÔMICO!'

print(gasolina(11, 4))