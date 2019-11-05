#EX 1
for i in range(0, 10):
    if i == 6:
        print(f'\nNumero {i} encontrado..')
        break
    else:
        print(i, end=' ')
print('Loop finalizado!')

#EX 2
while True:
    r = input('Digite "sair" para sair: ')
    if r == 'sair':
        break