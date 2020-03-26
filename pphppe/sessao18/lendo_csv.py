"""
Lendo arquivos CSV

CSV - Comma Separeted Values (Valores Separados por Vírgula).

EX:
    1, 2, 3, 4, 5

OBS: Os valores tbm podem ser separados por ponto e vírgula e espaço.


# Possível de trabalhar, mas trabalhoso

with open('original.csv', encoding='UTF-8') as original:
    dados = original.read()
    #print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas fiferentes para ler dados em arquivos CVS:
    - reader -> Permite que interemos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts.


# Modo reader

from csv import reader

with open('original.csv', encoding='UTF-8') as arq:
    leitor_csv = reader(arq)
    next(leitor_csv) # Faz pular a primeira linha, ou seja, o cabaçalho.
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} Nasceu no(a)(s) {linha[1]} e possui {linha[2]}cm de altura')

"""

# Modo DictReader

from csv import DictReader

with open('original.csv', encoding='UTF-8') as arq:
    leitor_csv = DictReader(arq) # Se for usar um outro separador específica assim: leitor_csv = DictReader(arq, delimiter=';') (exemplo ponto e vírgula).

    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        # Esse método pega o cabeçalho e bota como chave do dic
        print(f"{linha['Nome']} Nasceeu no(a)(os) {linha['País']} e possui {linha['Altura (em cm)']}")