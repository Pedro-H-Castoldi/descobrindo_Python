from ex25_13_variaveis import *
from ex25_13_insercao_de_dados import *

def remover():
    with open('agenda.txt', encoding='UTF-8') as ag:
            try:
                while True:
                    cont = nada = rrr = ex = x = 0

                    re = str(input('Insira o nome do funcionário que se deseja ser excluído: ')).title()
                    for i in range(len(fun)):
                        if re.lower() == fun[i][0].lower():
                            rrr = i
                            cont += 1

                    if cont > 1:
                        print('Foi notado que há mais de um funcionário com esse nome. Insira o número de telefone do mesmo para remoção: ')
                        rt = str(input('TELEFONE: '))
                        if len(rt) != 11:
                            raise TypeError

                        t = int(rt)

                        rt = f'({rt[0:2]}){rt[2]}{rt[3:7]}-{rt[7:]}'

                        for j in range(len(fun)):
                            fun[j][2] = str(fun[j][2]).replace('\n', '')
                            if rt == str(fun[j][2]) and re.lower() == fun[j][0].lower():
                                print('Excluído')
                                fun.pop(j)
                                nada = 1
                                break

                        if nada == 0:
                            rr = str(input(
                                f'Nenhum número associado com o nome {re} foi encontrado. Excluir todos os contatos com esse nome? S- SIM | N- NÃO: '
                            ))
                            if rr in 'Ss':
                                for k in range(len(fun)):
                                    if fun[k][0].lower() == re.lower():
                                        ex += 1
                                        print(ex)

                            else:
                                print('FUNCIONÁRIO NÃO ENCONTRADO!')

                    elif cont == 1:
                        fun.pop(rrr)
                        print(f'Funcionário {re} excluido com sucesso.')

                    else:
                        print('FUNCIONÁRIO NÃO ENCONTRADO!')

                    if ex:
                        while x <= ex + 1:
                            for i in range(len(fun)):
                                if fun[i][0].lower() == re.lower():
                                    fun.pop(i)
                                    break
                                x += 1

                    insercaoDeDados()

                    op = str(input('Nova remoção? S- Sim | N- NÃO: '))
                    if op in 'Nn':
                        break

            except TypeError:
                print('Algo deu erra!')