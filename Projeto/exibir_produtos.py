from variaveis_g import *

def verProduto():
    op = int(input('1- LISTA DE PRODUTOS | 2- PESQUISAR PRODUTO: '))
    if op == 1:
        print(f'ID          Produto                 Preço           Situação')
        for i in produtos:
            if produtos[i][2]:
                situacao = 'em estoque'
            else:
                situacao = 'sem estoque'

            print(f'{i}           {produtos[i][0]}                R${produtos[i][1]}                {situacao}')
    else:
        p = str(input('Digite o ID ou o nome do produto: '))
        if p in '12345678910':
            p = int(p)
        else:
            p = p.title()
        for i in produtos:
            if i == p or produtos[i][0] == p:
                if produtos[i][2]:
                    situacao = 'em estoque'
                else:
                    situacao = 'sem estoque'
                print(f'ID   Produto   Preço  Situação')
                print(f'{i}     {produtos[i][0]}        {produtos[i][1]}     {situacao}')