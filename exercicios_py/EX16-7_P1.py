num = []
for i in range(5):
    n = float(input(f'Digite o {i+1}° número: '))
    num.append(n)
cod = int(input('Digite o código: '))

if cod  == 1:
    for i, _ in enumerate(num):
        print(num[i])
elif cod == 2:
    num.reverse()
    for i, _ in enumerate(num):
        print(num[i])
elif cod == 0:
    print('FINALIZADO.')
else:
    print('CÓDIGO INVÁLIDO!')
