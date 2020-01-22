from ex25_13_variaveis import *

def insercaoDeDados():
    with open('agenda.txt', 'w+', encoding='UTF-8') as ag:
        for i in range(len(fun)):
            ag.write(f'{fun[i][0].title()} -- {fun[i][1]} -- {fun[i][2]}\n')
        ag.seek(0)