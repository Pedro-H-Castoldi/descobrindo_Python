"""
Não confunda sorted() com sort(), o sort() só funciona em listas, já o sorted() funciona em qualquer tipo de interável;

Sorted como o nome já diz, serve para ordenar;

OBS: o sorted SEMPRE retornará uma lista.


# EX:
n = (2, 8, 6, 4, 9, 2)

print(n)

print(sorted(n)) # Note q o q será retornado, será uma lista com os valores ordenados do menor para o maior.
print(tuple(sorted(n))) # Converter o valor retornado de list para tuple.

print(n) # O sorted() n modifica o interável, printando novamente sem o sorted os numeros voltam ao seu estado normal.

print(sorted(n, reverse=True)) # Ordenar do maior para o menor




users = [
    {'username': 'motaromk3', 'tweets': []},
    {'username': 'sindel', 'tweets': ['Eu sou a rainha que mudará o destino dos reinos', 'Estou de volta próximo mês...']},
    {'username': 'joker', 'tweets': ['Quem quer dar uma gargalhada?']},
    {'username': 'mileena', 'tweets': []}
]

# Ordenar os tweets pelos os nomes dos usuários (estamos utilizando essa operação em um dic):
print(users)

# Ordenando nomes  por ordem alfabética:
print(sorted(users, key=lambda usn: usn['username'], reverse=True)) # Para fazer a ordenação é necessário especificar a chave (key) do dic, utilizando uma lambda.

# Ordenar pelo número de tweets:
print(sorted(users, key=lambda ntww: len(ntww['tweets'])))


"""

# Musicas mais tocadas
musicas = [
    {'nome': 'Bohemia Rhapsody', 'tocou': 10000000},
    {'nome': 'Espere não Vá', 'tocou': 30000},
    {'nome': 'Paz do Mundo', 'tocou': 500000},
]

# Ordenar da menos tocada pra mais tocada:
print(sorted(musicas, key=lambda toc: toc['tocou']))