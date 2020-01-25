from ex25_13_variaveis import *

def busca():
    while True:
        pn = str(input('Busque pelo nome: ')).title() # Pode pesquisar apenas com a primeira letra do nome.
        achado = 0

        print('NOME             ANIVERSÁRIO         CONTATO')
        for i in range(len(fun)):
            if pn in fun[i][0]:
                print(f'{fun[i][0]}             {fun[i][1]}         {fun[i][2]}')
                achado = 1

        if achado == 0:
            print('     FUNCIONÁRIO NÃO ENCONTRADO.')

        op = str(input('Nova busca? S- SIM | N- NÃO: '))
        if op in 'Nn':
            break