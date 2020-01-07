"""
Collections -> high-performance Container Datetypes

Counter (Contador)
Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter q é parecido com um dicionário,
contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade de vezes q este elemento
se repete na lista.
"""

# Realizando o import
from collections import Counter

# Exemplo 1
# Se pode utilizar qualquer tipo de interável, nesse exemplo irá ser utilizado uma lista
numeros = [1, 4, 1, 1, 1, 5, 4, 5, 5, 5, 4, 4, 2, 4, 6, 5, 5, 5, 5, 5, 3]

cont = Counter(numeros)
# As chaves são os elementos da lista e os valores a quantidade de vezes q o elemento se repete. EX: 5: 9
print(cont)
print(type(cont))

# Exemplo 2 - Com strings
print(Counter('Pedro Henrique Castoldi Bezerra'))



# Exemplo 3
texto = 'Um guia de TV no Japão, revelou um novo.txt título para o anime Pokémon Sun e Moon' \
        ' que mostra uma relação com um dos gêneros mais famosos atualmente no mundo dos ' \
        'jogos, que vai ao ar no dia 07 de julho. Este capítulo mostrará as rodadas preliminares' \
        ' na Liga Pokémon de Alola, onde 151 treinadores se enfrentarão até sobrarem 16 competidores' \
        ' em batalha. Confira:'

# print(texto.split()) # Separa palavre por palavra (n faz parte do Counter)

tex = Counter(texto)
print(tex)

# Encontrar as 5 palavras com mais ocorrência no texto
print(tex.most_common(5))

t = 'gjktrngjk nrgjn'
t = Counter(t)
print(t.most_common(3))