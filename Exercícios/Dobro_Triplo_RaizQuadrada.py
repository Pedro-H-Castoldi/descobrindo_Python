print(' OLÁ! Seja bem-vindo ao Calculer!!!')

while True:
    n = int(input('Insira um numero que deseja calcular: '))
    d = n*2
    t = n*3
    r = n**(1/2)
    print(f'O dobro de {n} é: {d}')
    print(f'O triplo de {n} é: {t}')
    print(f'A raiz quadra de {n}: {r:.2f}')

    print(' Resultado')
    print(f'DOBRO........: {d}\nTRIPLO.......: {t}\nRAIZ QUADRADA: {r:.2f}')
    res = input('Insirir um novo número ou encerrar? S/N: ')
    if res in 'Nn':
        break
print('Finalizado!')