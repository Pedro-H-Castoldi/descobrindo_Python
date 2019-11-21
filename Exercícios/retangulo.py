def retangulo():
    t = True
    while t:
        c = int(input('Insira a quantidade de colunas: '))
        l = int(input('Insira a quantidade de linhas: '))

        if c > 0 and c <= 20:
            if l > 0 and l <= 20:
                if c != l:
                    t = False
        print('Erro. insira o número de colunas e linhas de no minimo 1 e no máximo 20.\n'
        'Insira também valores diferentes para colunas e linhas.')

    print('-+' * c)

    sp = ' ' * (c*2 - 2)

    ql ='|'

    for i in range(l):
        print(f'|{sp}{ql}')
    print('+-' * c)

retangulo()