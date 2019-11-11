lista = []
lista2 = []

while True:
    n = float(input('Insira um número | Para encerrar digite um número negativo: '))
    if n >= 0:
        lista.append(n)
    else:
        break

top25 = filter(lambda n: n <= 25, lista)
top25 = list(top25)

top50 = filter(lambda n: n >= 26 and n <= 50, lista)
top50 = list(top50)

top75 = filter(lambda n: n >= 51 and n <= 75, lista)
top75 = list(top75)

top100 = filter(lambda n: n >= 76 and n <= 100, lista)
top100 = list(top100)

#lista2.append([top25, top50, top75, top100])

print('TOP 25:')
[print(n, end=' ') for n in top25]

print('\n\nTOP 50')
[print(n, end=' ') for n in top50]

print('\n\nTOP 75')
[print(n, end=' ') for n in top75]

print('\n\nTOP 100')
[print(n, end=' ') for n in top100]

