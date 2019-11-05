"""
 Tipo de dado sem tipo

 OBS: O tipo None é representado com letra maiúscula - None
 certo = None
 errado = None

 Quando utilizar?
    - Podemos utilizar None quando for necessário utilizar uma variável q não se deseja dar um tipo a ela
     logo de cara, isso até ela receber depois um valor final.

 OBS: O tipo None em Python sempre é considerado como falso (False)
"""

# Criação sem tipo
numeros = None
print(numeros)
print(type(numeros))

# Variável recebe um tipo (Nesse caso o tipo 'tuple')
numeros = 1, 5, 8
print(numeros)
print(type(numeros))