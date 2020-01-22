# Q11
ar = str(input('Informe o nome do arquivo que será trabalhado: '))
try:
    with open(ar, encoding='UTF-8') as arq:
        cont = 0
        pa = []
        palavra = str(input('Informe uma palavra: '))
        arl = list(arq)
        for i in range(len(arl)):
            pa.append(arl[i].split())
        for i in range(len(pa)):
            for j in range(len(pa[i])):
                if pa[i][j].lower() == palavra.lower():
                    cont += 1
                if pa[i][j].lower() == palavra.lower() + '!' or pa[i][j].lower() == palavra.lower() + '.' or pa[i][j].lower() == palavra.lower() + ',' or pa[i][j].lower() == palavra.lower() + ':':
                    cont += 1

        print(f'A palavra "{palavra}" repete {cont} vezes no arquivo {ar}')
except FileNotFoundError:
    print(f'Erro: Nome do arquivo inválido!')