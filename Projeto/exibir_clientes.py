from variaveis_g import *

def consultarClientes():
    op = int(input('1- LISTA DE CLIENTES | 2- PESQUISAR CLIENTE: '))
    if op == 1:
        print(f'ID      Nome                        CPF         Idade       Endereço                          Situação')
        for i in clientes:
            if clientes[i][4]:
                situacao = 'Conta paga'
            else:
                situacao = 'devendo'
            print(f'{i}           {clientes[i][0]}                {clientes[i][2]}  {clientes[i][1]} {clientes[i][3]}             {situacao}')
    else:
        p = str(input('Digite o ID ou o nome do cliente: '))
        if p in '12345678910':
            p = int(p)
        else:
            p = p.lower()
        for i in clientes:
            if i == p or clientes[i][0].lower() == p:
                if clientes[i][4]:
                    situacao = 'Conta paga'
                else:
                    situacao = 'Devendo'
                print(f'ID      Nome                        CPF         Idade       Endereço                          Situação')
                print(f'{i}           {clientes[i][0]}                {clientes[i][2]}  {clientes[i][1]} {clientes[i][3]}             {situacao}')
