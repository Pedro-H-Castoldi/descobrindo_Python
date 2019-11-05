def intervalo(ni, nf):
    if ni < nf:
        nu = ni
        soma = 0
        numeros = []
        while nf >= nu:
            if nu%2 != 0:
                numeros.append(nu)
            nu = nu+1
        print(f'Os números impares entre o intervalo {ni} e {nf} são:')
        for i, _ in enumerate(numeros):
            soma += numeros[i]
            print(f'| \033[1;35m{numeros[i]}', end= '\033[1;37m | ')
        print(f'\n\033[4;37mA soma dos números é:\033[m \033[1;36m{soma}')
    else:
        print('\033[1;31mIntervalo de valores inválido!')

ni = int(input('Digite o número 1: '))
nf = int(input('Digite o número 2: '))
intervalo(ni=ni, nf=nf)

