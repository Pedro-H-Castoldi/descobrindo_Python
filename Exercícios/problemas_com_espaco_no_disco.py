nomes = []
espacos = []
porcentagem = []
dados = []

while True:
    nome = str(input('Nome: '))
    espaco = int(input('Espaço ocupado: '))

    nomes.append(nome)
    espacos.append(espaco)

    r = str(input('Continuar? S - SIM | N - NÃO: '))
    if r in 'Nn':
        break


def zipar(no, es, po):
    zipp = list(zip(no, es, po))
    print('NOME                 MB            PORCENTAGEM')
    for i in range(len(zipp)):
        print(f'{zipp[i][0]}:           {zipp[i][1]:.5f}            {zipp[i][2]:.2f}')


def porcentagemOcupada(mb):
    total = sum(mb)

    for i in range(len(mb)):
        por = (mb[i] * 100)/total
        porcentagem.append(por)
    zipar(nomes, espacos, porcentagem)


def conversao (b):
    for i in range(len(espacos)):
        espacos[i] = espacos[i] / 1048576
    porcentagemOcupada(espacos)

conversao(espacos)
