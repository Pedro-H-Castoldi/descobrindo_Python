while True:
    n = int(input('Digite um número para saber o seu antecessor e seu sucessor: '))
    print(f'ANTECESSOR: {n-1}')
    print(f'SUCESSOR..: {n+1}')
    res = input('Analisar mais um número? S/N: ')
    if res in 'Nn':
        break
print('Finalizado!')