n = int(input('Digite um número: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

while True:
    if n < 10:
        print(f'Unidade: {u}')
        break
    if n > 9 and n < 100:
        print(f'Unidade: {u}\nDezena: {d}')
        break
    if n > 99 and n < 1000:
        print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}')
        break
    if n > 999 and n < 10000:
        print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')
        break