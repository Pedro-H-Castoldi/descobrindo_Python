from cliente import Cliente
from produto import Produto

def inserir_dados():
    with open('clientes.txt', 'a+', encoding='UTF-8') as clientes:
        clientes.seek(0)
        dados = list(clientes)
        for i in range(len(dados)):
            if dados[i] != '\n':
                cli = dados[i].split('--')

                if cli[5].replace('\n', '') == 'True':
                    cliente = Cliente(cli[1], int(cli[2]), cli[3], cli[4], True)
                    cliente.add()
                else:
                    cliente = Cliente(cli[1], int(cli[2]), cli[3], cli[4], False)
                    cliente.add()

    with open('produtos.txt', 'a+', encoding='UTF-8') as produtos:
        produtos.seek(0)
        dados = list(produtos)
        for i in range(len(dados)):
            if dados[i] != '\n':
                pro = dados[i].split('--')

                produto = Produto(pro[1], pro[2], float(pro[3]), int(pro[4]))
                produto.add_produto()