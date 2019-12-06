from cadastrar_cliente import cadastrarCliente

from efetuar_compra import compras

from devedores import devedores

from exibir_produtos import verProduto

from exibir_clientes import consultarClientes

from variaveis_g import *
def menu():
    while True:
        op = int(input('Escola uma opção: 1- Cadastrar Cliente, 2- Devendo, 3- Compras, 4- Consultar Produto, 5- Consultar clientes,  - Encerrar: '))

        if op == 1:
            cadastrarCliente()
        elif op == 2:
            devedores()
        elif op == 3:
            compras()
        elif op == 4:
            verProduto()
        elif op == 5:
            consultarClientes()
        else:
            break

menu()