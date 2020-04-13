import cliente
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
        c_cliente = cliente.Cliente.cliente_dados(c_cliente)

        if c_cliente:
            self.__cliente = c_cliente
            self.encher_carrinho()

    def encher_carrinho(self):
        self.__l_carrinho.clear()

        while True:
            c_produto = str(input('Insira o nome do produto: ')).title()
            c_produto = Produto.produto_dados(c_produto)
            Produto.ver_estoque(c_produto)

            if c_produto:
                if c_produto.estoque:
                    while True:
                        cont = 0
                        quant = int(input(f'Quantidade de {c_produto.nome} X {c_produto.quant} : '))
                        if quant > 0 and c_produto.quant >= quant:
                            while cont < quant:
                                cont += 1
                                self.l_carrinho.append(c_produto)
                            break
                        elif quant <= 0:
                            print('Insira uma quantidade válida.')
                        else:
                            print(f'A quantidade pedida é maior que a quantidade em estoque.')
                            print(f'O produto {c_produto.nome} tem em estoque {c_produto.quant} unidade(s).')
                            op = int(input(f'1- Tentar novamente | 0- Cancelar: '))
                            if op != 1:
                                break
                else:
                    print('Produto faltando.')

            if not self.l_carrinho:
                op = int(input('1- Continuar comprando | 0- Sair: '))
                if op == 0:
                    break
            else:
                op = int(input('1- Continuar Comprando | 2- Ir para o Caixa | 0- Desfazer Carrinho: '))
                if op == 2:
                    comprar = Compra(self)
                    comprar.comprar()
                    break
                elif op == 0:
                    self.l_carrinho.clear()
                    break
