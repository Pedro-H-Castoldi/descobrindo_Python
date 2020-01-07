nome = 'Pedro Henrique'
print(nome)
print(type(nome))

# Cria uma lista de strings (Pedro, Henrique)
#print(nome.split())

"""
[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13] 
['P', 'e', 'd', 'r', 'o', ' ', 'H', 'e', 'n', 'r', 'i', 'q', 'u', 'e']
"""

# Irá imprimir do P(0) até d(2) n imprime a casa 3 e sim a 2. Se quiser imprimir a 3 faz nome[0:4]
print(nome[0:3]) # Isso é chamado de Slice de string

# [::-1] -> Comece do primeiro elemento, vá até o último e então inverta!
print(nome[::-1])

print(nome.split()[0]) # Vai imprimir o primeiro item da lista (Pedro)
print(nome.split()[1]) # Vai imprimir o Segundo item da lista (Henrique)

# Substituir letra
print(nome.replace('P', 'W'))