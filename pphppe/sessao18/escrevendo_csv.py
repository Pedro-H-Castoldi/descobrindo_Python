"""
Escrevendo em Arquivos CSV

reader (leitor), writer (escritor).

writerrow() -> Escreve uma linha.


# Escrevendo em arquivo CSV
from csv import writer

# writer() -> Gera um objeto para que possamos escrever em arquivos CSV;
# writerow() -> Escreve em cada linha por vez em um arquivo CSV.

with open('filmes.csv', 'w', encoding='UTF-8') as arq:
    escritor_csv = writer(arq)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração']) # Criando o cabeçalho.

    while filme != 'sair':
        filme = str(input('Título: '))
        if filme != 'sair':
            genero = str(input('Gênero: '))
            duracao = int(input('Duração em minutos: '))

            escritor_csv.writerow([filme, genero, duracao]) # Irá colocar cada dado em seu respectivo local de cabeçalho.
        else:
            print('Encerrado.')

# OBS: Toda vez q for executar a escrita, o cabeçalho é escrito junto, repetindo ele no texto (isso se usar o modo 'a').

"""

# DictWriter

from csv import DictWriter

with open('filmes2.csv', 'a+', encoding='UTF-8') as arq:
    cabecalho = ['Título', 'Gênero', 'Duração']

    escritor_csv = DictWriter(arq, fieldnames=cabecalho) # Criando cabeçalho.
    escritor_csv.writeheader() # Inserindo cabeçalho.
    filme = None

    while filme != 'sair':
        filme = str(input('Título: '))
        if filme != 'sair':
            genero = str(input('Gênero: '))
            duracao = int(input('Duração em minutos: '))

            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao}) # A chave tem q ser escrita q nem como foi anunciada lá encima.

# O cabeçalho é escrito novamente se usar o modo 'a'.