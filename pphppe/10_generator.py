"""
Existem:
    - List Comprehension;
    - Set Comprehension;
    - Dictionary Comprehension;
    - Generator Expression (usando Tuple).

"""

# Utilizando o Generator:
nomes = ['Pablo', 'Pedro', 'Patrícia', 'Arioldo']

print(any((nome[0] == 'P' for nome in nomes)))

# List Comprehension:
res = [nome[0] == 'P' for nome in nomes]
print(type(res))
print(res)

# Generator:
res = (nome[0] == 'P' for nome in nomes)
print(type(res))
print(res) # O Generator conseme menos recursos e memória pois ele não gera uma 'lista' de atributos para imprimir (mais aconselhável)

# O generator é aconselhável de usar quando n se deseja imprimir o interável, mas sim checa-lo.

# getsizeof -> Mostra em bytes a quantidade de memória que o elemento ocupa
from sys import getsizeof
print(getsizeof('Pedro Henrique Castoldi Bezerra'))
print(getsizeof(1))
print(getsizeof(True))
print(getsizeof([]))

# Quantidade de bytes que cada tipo de comprehension ocupa na memória:
list_comp = getsizeof([x for x in range(1000)])
set_comp = getsizeof({x for x in range(1000)})
dic_comp = getsizeof({x: x for x in range(1000)})
generator = getsizeof(x for x in range(1000))

print('Os valores de bytes são:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dic Comprehension: {dic_comp} bytes')
print(f'Generator Expression Comprehension: {generator} bytes') # Note q o Generator consome muito menos da memória

# É possível interar no Generator Expression? SIM:
n = (x * 2 for x in range(10))
print(type(n))
print(n) # N será printado os valores assim, e sim um object Generator Expression

# Para printar os valores:
for i in n:
    print(i)