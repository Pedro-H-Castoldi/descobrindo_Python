from ex25_13_variaveis import *

def niver():
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro')
    print('                 Pesquisar aniversários do mês')
    try:
        while True:
            valido = existe = m = 0

            mes = str(input('Insira o mês: '))

            for i in range(len(meses)):
                if meses[i] == mes.lower():
                    mes = int(i + 1)
                    existe = 1
                    break

            if int(mes):
                mes = int(mes)
                if mes < 1 or mes > 12:
                    raise ValueError
                else:
                    valido = 1
                    existe = 1

            if existe == 0:
                raise ValueError

            if valido:
                print('     Aniversariantes do Mês!!!\n')
                for i in range(len(fun)):
                    if mes < 10:
                        if fun[i][1][3:] == f'0{mes}':
                            m = 1
                            print(*fun[i])
                    else:
                        if fun[i][1][3:] == f'0{mes}':
                            m = 1
                            print(*fun[i])

            if m == 0:
                print('     Nenhum aniversário encontrado nesse mês..\n')

            op = str(input('Nova busca? S- SIM | N- NÃO: '))
            if op in 'Nn':
                break

    except ValueError:
        print('ERRO: Insira um mês válido.')
