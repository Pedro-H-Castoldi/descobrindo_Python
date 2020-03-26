from cliente import Cliente
from produto import Produto
from compra import Compra

class Carrinho:

    def __init__(self):
        self.__l_carrinho = []

    @property
    def l_carrinho(self):
        return self.__l_carrinho
    @property
    def cliente(self):
        return self.__cliente


    def conferir_cliente(self):
        c_cliente = str(input('Insira o nome completo do cliente: ')).title()
        c_cliente = Cliente.listar_clientes_nome(c_cliente)

        if c_cliente:
            self.__cliente = c_cliente
            self.encher_carrinho()

    def encher_carrinho(self):
        self.__l_carrinho.clear()

        while True:
            c_produto = str(input('Insira o nome do produto: ')).title()
            c_produto = Produto.listar_produtos_nome(c_produto)

            if c_produto:
                if c_produto.estoque:
                    self.l_carrinho.append(c_produto)
                else:
                    print('Produto faltando.')

            if not self.l_carrinho:
                op = int(input('1- Continuar comprando | 0- Sair: '))
                if op == 0:
                    break
            else:
                op = int(input('1- Continuar Comprando | 2- Ir para o Caixa | 0- Desfazer Carrinho: '))
                if op == 2:
                    compra = Compra(self)
                    compra.comprar()
                    break
                elif op == 0:
                    self.l_carrinho.clear()
                    break
