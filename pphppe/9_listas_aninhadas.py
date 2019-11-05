"""
- Algumas linguagens de programação possuiem uma estrutura de dados chamadas de array.
    - Unidimensionsis (Arrays / Vetores)
    - Multidimencionais (Matrizes)

- Em Python nos temos as litas:
    lista = ['oi', True, 33, 5.3, (tuble), [4, 3])


# Criando matriz 3x3
# Fazer uma matriz com valores iguais
matriz = [0, 0, 0]
mm = [matriz] * 3


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[0]) # Imprimindo o primeiro elemento
print(matriz[0][2]) # Imprimindo o valor 2 do primeiro elemento
print(matriz[2][1])


# Mostrando valores com loop
for lista in matriz:
    for i in lista:
        print(i) # Na matriz mostras valor em lista e para cada lista mostrar i (matriz[lista][i])

# List comprehension
[[print(i) for i in lista] for lista in matriz] # Pode ser pensado como no exemplo anterior: matriz[lista][i]

"""

# Gerando um tabuleiro/matriz 3x3
# For lista no range(1, 4) e para cada número desse range (no lista), for i in range(1, 4)
tabuleiro = [[i for i in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)

# Gerando jogadas no jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for lista in range(1, 4)]
print(velha)

# Gerando valores iniciáis (valores default para o início do jogo)
print([['*' for i in range(1,4)] for lista in range(1, 4)])