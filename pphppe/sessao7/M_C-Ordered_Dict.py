"""
O Ordered Dict é um dicionário comum, só q ele possui algo a mais, o mesmo dá a certeza q os dados inseridos no dicionário estarão ordenados por inserção.

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dicionario)

for c, v in dicionario.items():
    print(f'Chave: {c} | Valor: {v}')
"""

from collections import OrderedDict
dicionario = OrderedDict({'A': 1, 'B': 2, 'C': 3, 'D': 4}) # Certeza da ordenação por inserção

for c, v in dicionario.items():
    print(f'CHAVE: {c} | VALOR: {v}')

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
print(d1 == d2) # Vai dizer q os dois dicionários são iguais, mesmo estando em ordem diferente

# Usando o OrderedDict
od1 = OrderedDict({'a': 1, 'b': 2})
od2 = OrderedDict({'b': 2, 'a': 1})
print(od1 == od2) # Agora com o OrderedDict dirá q os 2 dicionários n são iguais (a ordem dos elementos importa pro dicionário)

