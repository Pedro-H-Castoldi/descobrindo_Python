from ex25_13_variaveis import *

def inserirNaLista():
    with open('agenda.txt', 'a+', encoding='UTF-8') as ag:
        ag.seek(0)
        dados = list(ag)
        for i in range(len(dados)):
            if dados[i] != '\n':
                a = dados[i]
                a = a.split(' -- ')
                fun.append(a)

        print(fun)