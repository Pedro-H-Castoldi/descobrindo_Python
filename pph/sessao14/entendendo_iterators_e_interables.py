"""
Iterator ->
    - Um objeto q pode ser iterado;
    - Um objeto q retorna um dado, sendo um elemento por vez quando um função next() é chamada.

Interable ->
    - Um objeto q retornará um iterator quando a função iter() for chamada.
"""

nome = 'Boruto'
numeros = [1, 4, 7, 9, 0]

# Erro pois eles n são Iterators e sim Iterables
#print(next(nome))
#print(next(numeros))

# Transformando em iterator
t1 = iter(nome)
t2 = iter(numeros)

# Agora será imprimido o iterator cada vez q a função nrxt() for chamada, retornando 1 dado por vez
print(next(t1)) # B
print(next(t1)) # o
print(next(t1)) # r
print(next(t1)) # u
print(next(t1)) # t
print(next(t1)) # o

print(next(t2))

# OBS: se chamar a função next() mais vezes q o iterator tem de caracteres, dará um erro.

# Quando se usa o for, essas funções mostradas (iter(), next()) são rodadas por baixo dos panos.