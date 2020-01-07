"""
Pense no seguinte:
    - lista = [1, 2, 3]
    - tupla = (1, 2, 3) or 1, 2, 3
    - conjunto {1, 2, 3}
    - dicionario = {'a': 1, 'b': 2, 'c': 3} # {'chave': valor}

    SINTAXE:
    {'chave': valor for valor in interavel}


# EX 1
numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

"""

# Pode colocar outros inreráveis como lista, tuplas tendo chave e n só valor
lista = [1, 2, 3]
tupla = 1, 2, 3
conjunto = {1, 2, 3}

quadrado = {valor: valor ** 2 for valor in lista} # Pega o valor original e bota como chave, e o valor elevado ao quadrado
print(quadrado)

quadrado = {valor: valor ** 2 for valor in tupla}
print(quadrado)

quadrado = {valor: valor ** 2 for valor in conjunto}
print(quadrado)


# Agregar chave e valores
chaves = 'abcd'
numeros = [1, 2, 3, 4]

agregar = {chaves[i]: numeros[i] for i in range(0, len(numeros))}
print(agregar)


# EXs com lógica condicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = {n: ('Par' if n % 2 == 0 else 'Impar') for n in numeros} # o () é só pra deixar organizado
print(res)