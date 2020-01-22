# Q2
with open('arq.txt', encoding='UTF-8') as arq:
    print(f'o arquivo "{arq.name}" possui {len(arq.readlines())} linhas.')


# Q3
cont = 0
with open('arq.txt', encoding='UTF-8') as arq:
    ar = list(arq)
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j].lower() in 'aeiouáãàéêíóôõú':
                cont += 1
    print(f'O arquivo "{arq.name}" possui {cont} vogais.')


# Q4
cont = 0
with open('arq.txt', encoding='UTF-8') as arq:
    ar = list(arq)
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j].lower() in 'bcdfghjklnmpqrstvxwyz':
                cont += 1
    print(f'O arquivo {arq.name} possui {cont} cossoantes.')