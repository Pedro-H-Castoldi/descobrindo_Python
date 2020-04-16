def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'para manter a forma.'
    else:
        final = 'pois só se vive uma vez.'

    return f'Comi {comida} {final}'

def dormir(hora):
    if hora > 8:
        return 'Dormir demais! Perdi a hora.'
    return f'Continuo cansado após dormir por {hora} horas..'

def eh_engracada(nome):
    engracados = ['Tatá', 'Gisely']
    if nome in engracados:
        return True
    return False