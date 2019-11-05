"""
- Com List Comprehension é possível gerar novas listas com dados processados a partir de um outro interável (list, tuple, etc)

- SINTAX DA LIST COMPREHENSION
    [dado for dado in interável]


# EX 1
numeros = [5, 9, 2, 6]

# O interável 'numeros' será pego e com o List Comprehesiom será pego os valores desse interável e multiplicados cada um por 10
# e então armazenados na lista 'nova'
novo = [dados * 10 for dados in numeros]
print(novo)

# EX 2
novo = [dados / 2 for dados in numeros]
print(novo)

# EX 3 - Usando função
def quadrado(n):
    return n ** 2

print([quadrado(dados) for dados in numeros])


# list comprehension VS loop
# Loop
numeros = [1, 5, 8, 4]
numeros_quadrados = []
for numero in numeros:
    numeros_quadrados.append(numero ** 2)
print(numeros_quadrados)

# List Comprehension
print([numero ** 2 for numero in numeros]) # Fez a mesma coisa q o loop de forma muito mais prática em uma só linha!

"""

# Com strings
vc = 'Várzea da Conceição'
print([nome.upper() for nome in vc])

nomes = ['raissa', 'yuri', 'nightwolf', 'jade']
print([nome.upper() for nome in nomes])

# Colocar a primeira letra do nome em maiúsculo
def maiusculo(n):
    n = n.replace(n[0], n[0].upper())
    return n

print([maiusculo(nome) for nome in nomes])

# Modo 2
print([nome.title() for nome in nomes])

# Outros exemplos
print([n * 2 for n in range(1, 10)])

print([bool(n) for n in [1, '', 0, 33, 'tt']])

print([str(n) for n in [1, 6, 8, 3]])

q = 4
print([n * q for n in range(0, 11)])