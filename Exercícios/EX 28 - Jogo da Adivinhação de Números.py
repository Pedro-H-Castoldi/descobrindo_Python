from random import choice
from time import sleep

print(f'-=-'*20)
print('Eae! Está pronto???\nEm que número eu pensei de 0 a 5?')
print(f'-=-'*20)
pn = [0, 1, 2, 3, 4, 5]

while True:
    pensei = choice(pn)
    na = int(input('Digite o número que pensei: '))
    print('PROCESSANDO...')
    sleep(1)
    if na >= 0 and na <= 5:
        print('\n')
        if na == pensei:
            print(f'UAU!!! Você acertou!!! Eu havia pensado no número {pensei}...')
        else:
            print(f'TE PEGUEI! Na verdade eu pensei no número {pensei}!!!')
        res = str(input('EAE. VAMOS DE NOVO???? S/N '))
        if res in 'Nn':
            print('TE VEJO NA PRÓXIMA!!!')
            break
        print('\n')





