nomes = []
espacos = []
porcentagem = []
dados = []

while True:
    nome = str(input('Nome: '))
    espaco = int(input('Espaço ocupado: '))

    nomes.append(nome)
    espacos.append(espaco)

    r = str(input('Continuar? S - SIM | N - NÃO'))
    if r in 'Nn':
        break


def zipar(no, es, po):
    for i in range(len(no)):
        dados.append([no[i], es[i], po[i]])
    for j in range(len(dados)):
        print(dados[i])


def porcentagemOcupada(mb):
    total = sum(mb)

    for i in range(len(mb)):
        por = (mb[i] * 100)/total
        porcentagem.append(por)
    zipar(nomes, espacos, porcentagemOcupada)


def conversao (b):
    for i in range(len(espacos)):
        espacos[i] = espacos[i] / 1048576
    porcentagemOcupada(espacos)

conversao(espacos)
