from math import trunc # Como só irá utilizar a função trunc faz assim. Para importar toda a biblíoteca: import math
# EX1
n = float(input('Digite um número: '))
print(f'O número {n} em sua forma inteira é: {trunc(n)}') # Utilizando somente o trunc. Se a a biblíoteca fosse toda passada seria: math.trunc(n)

# EX2
n = float(input('Digite um número: '))
print(f'O número {n} em sua forma inteira é: {int(n)}')

# EX3
n = float(input('Digite um número: '))
print(f'O número {n} em sua forma inteira é: {n :.0f}')
