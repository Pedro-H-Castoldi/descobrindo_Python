from ex25_13_variaveis import *
from ex25_13_inserir import *
from ex25_13_insercao_de_dados import *
from ex25_13_remover import *
from ex25_13_inserir_na_lista import *
from ex25_13_busca import *
from ex25_13_niver import *

def home():
    inserirNaLista()
    while True:
        try:
            op = int(input('Escolha uma opção: 1- INSERIR | 2- REMOVER | 3- BUSCA | 4- ANIVERSÁRIOS DO MÊS | 5- SAIR: '))
            if op == 1:
                inserir()
                insercaoDeDados()
            elif op == 2:
                remover()
            elif op == 3:
                busca()
            elif op == 4:
                pass
                niver()
            else:
                break

        except ValueError:
            print('ERRO: Insira um número inteiro!')

home()