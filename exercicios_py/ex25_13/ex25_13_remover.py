from ex25_13_variaveis import *
from ex25_13_insercao_de_dados import *

def remover():
    cont = nada = rrr = 0
    with open('agenda.txt', encoding='UTF-8') as ag:
            try:
                while True:
                    re = str(input('Insira o nome do funcionário que se deseja ser excluído: '))
                    for i in range(len(fun)):
                        if re.lower() == fun[i][0].lower():
                            rrr = i
                            cont += 1
                            print(cont)

                    if cont > 1:
                        print('Foi notado que há mais de um funcionário com esse nome. Insira o número de telefone do mesmo para remoção: ')
                        rt = str(input('TELEFONE: '))
                        if len(rt) != 11:
                            raise TypeError

                        t = int(rt)

                        rt = f'({rt[0:2]}){rt[2]}{rt[3:7]}-{rt[7:]}'
                        print(rt)

                        for j in range(len(fun)):
                             if rt == fun[j][1] and re.lower() == fun[j][0].lower():
                                fun.pop(j)
                                nada = 1
                        if nada == 0:
                            rr = str(input(
                                f'Nenhum número associado com o nome {re} foi encontrado. Excluir todos os contatos com esse nome? S- SIM | N- NÃO: '
                            ))
                            if rr in 'Ss':
                                for k in range(len(fun)):
                                    if fun[k][0].lower() == re.lower():
                                        fun.pop(k)
                                break
                            else:
                                return 'FUNCIONÁRIO NÃO ENCONTRADO!'
                    elif cont == 1:
                        fun.pop(rrr)
                        break

                    else:
                        print('Funcionário não encontrado.')
                        break

                op = str(input('Nova remoção? S- Sim | N- NÃO: '))
                if op in 'Nn':
                    print(fun)
                    insercaoDeDados()

            except TypeError:
                print('Algo deu erra!')