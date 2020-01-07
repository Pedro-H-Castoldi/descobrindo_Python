"""
lista = [1, 2, 3, 4, 5]

conjunto = {1, 2, 3, 4, 5}
"""
set = {1, 2, 3, 4, 5}

numeros = {x ** 2 for x in range(0, 10)}
print(numeros)

#DESAFIO! Fazer alteração pra virar de set para dic
numeros = {x: (x ** 2) for x in range(0, 10)}
print(numeros)

# Conjuntos n possui ordenação e nem repetição de elementos
{print(letra) for letra in 'Anime Geek'} # Assim teve ordenação e repetição de letras.. (?)
l = {l for l in 'Anime Geek'}
print(l)