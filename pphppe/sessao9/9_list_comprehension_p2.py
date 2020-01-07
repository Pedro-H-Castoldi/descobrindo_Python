"""
 É possível adicionar estruturas condicionais lógicas em nossa List Comprehensiion

"""

numeros = [3, 76, 4, 9, 2, 8]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print(pares)
print(impares)

# Refatorando

# O módulo de um número par tem resto zero e então ele retorna 0, q é considerado False, desse modo, n será armazenado na lista 'pares'
# para solucionar isso colocamos uma negação q fará com que 0 vire True (not False = True)
pares = [n for n in numeros if not n % 2]

# Como um módulo de um número impar tem resto, ele retornará 1, logo será considerado True, desse modo, n é preciso fazer alterações
impares = [n for n in numeros if n % 2]

print(pares)
print(impares)

print([n * 2 if not n % 2 else n / 2 for n in numeros])