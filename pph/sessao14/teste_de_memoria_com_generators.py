"""
Teste de memória com generators
Sequência Fibonacci:
    1, 1, 2, 3, 5, 8, 13, 21, ...
"""

def fibonacci_list(max):
    a, b = 0, 1
    list = []

    while len(list) < max:
        list.append(b)
        a, b = b, a + b
    return list

#print(fibonacci(8)) # Assim fica tudo um na frente do outro

for nu in fibonacci_list(8):
    print(nu)

# Utilizando generator (consome muito menos memória)
def fibonacci_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        yield b
        a, b = b, a + b
        cont += 1

for nu in fibonacci_gen(8):
    print(nu)