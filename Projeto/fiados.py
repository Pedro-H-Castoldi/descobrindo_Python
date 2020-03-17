from cliente import Cliente

from carrinho import Carrinho

from devedores import devedores

from produto import Produto

from compra import Compra

from inserir_dados import inserir_dados
from salvar_cliente import salvar_cliente
from salvar_produto import salvar_produto

def menu():
    inserir_dados()
    while True:
        op = int(input('Escola uma opção: 1- Clientes | 2- Compras | 3- Produtos | 0- Encerrar: '))

        if op == 1:
            print('--- Menu Cliente ---')
            op2 = int(input(f'1- Cadastrar Cliente | 2- Consultar Clientes | 3- Devedores | 0- Voltar Menu: '))
            if op2 == 1:
                nome = str(input('Nome: '))
                idade = int(input('Idade: '))
                cpf = str(input('CPF: '))
                endereco = str(input('Endereço: '))

                cliente = Cliente(nome, idade, cpf, endereco, False)
                cliente.add()
                salvar_cliente()


            elif op2 == 2:
                op3 = int(input('1- Listar Clientes | 2- Pesquisar Cliente | 0- Voltar Menu: '))
                if op3 == 1:
                    Cliente.listar_clientes()
                elif op3 == 2:
                    nome = str(input('Insira o nome do cliente: ')).title().strip()
                    Cliente.listar_clientes_nome(nome)

            elif op2 == 3:
                pass


        elif op == 2:
            print('--- Menu Compra ---')
            op2 = int(input('1- Comprar - 2- Histórico de Compras : '))
            if op2 == 1:
                carrinho = Carrinho()
                carrinho.conferir_cliente()
            elif op2 == 2:
                Compra.historico_de_compras()


        elif op == 3:
            print('--- Menu Produtos ---')
            op2 = int(input('1- Cadastrar Produto | 2- Listar Produtos | 0- Voltar Menu: '))
            if op2 == 1:
                nome = str(input('Nome: '))
                tipo = str(input('Tipo: '))
                preco = float(input('Preço: '))
                quant = int(input('Quantidade: '))

                produto = Produto(nome, tipo, preco, quant)
                produto.add_produto()
                salvar_produto()
            elif op2 == 2:
                op3 = int(input('1- Listar Produtos | 2- Pesquisar Produto | 0- Voltar Menu: '))
                if op3 == 1:
                    Produto.listar_produtos()
                elif op3 == 2:
                    nome = str(input('Insira o nome do produto: ')).title().strip()
                    Produto.listar_produtos_nome(nome)

            elif op2 == 3:
                pass

            elif op2 == 4:
                pass

        else:
            salvar_cliente()
            salvar_produto()
            break

menu()