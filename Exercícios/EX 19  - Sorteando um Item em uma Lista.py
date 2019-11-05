import random
nomes = []
"""
while True:
    n = str(input('Digite um nome: '))
    nomes.append(n)
    res = str(input('Continuar? S/N: '))
    if res in 'Nn':
        break

print(f'{random.choice(nomes)}')
"""


# EX 20 - Ordem de Nomes aleatória
cont = 1
while True:
    no = str(input(f'Digite o {cont}° nome: '))
    nomes.append(no)
    res = str(input('Continuar? S/N: '))
    if res in 'Nn':
        break
    cont+= 1

random.shuffle(nomes)
print(nomes, end = " ")