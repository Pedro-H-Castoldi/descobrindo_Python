from carrinho import *
from produto import Produto
from cliente import Cliente
from caderno_de_fiados import Fiado
from salvar_produto import salvar_produto

class Compra:

    cont = 0
    l_compras = []

    def __init__(self, carrinho):
        self.__id = Compra.cont + 1
        self.__carrinho_c = carrinho.l_carrinho
        self.__cliente_c = carrinho.cliente
        Compra.cont = self.__id

    @property
    def id(self):
        return self.__id
    @property
    def carrinho_c(self):
        return self.__carrinho_c
    @property
    def cliente_c(self):
        return self.__cliente_c
    @property
    def total(self):
        return self.__total

    def comprar(self):
        total = 0

        print(f'Cliente {self.cliente_c.nome}:')

        for i in range(len(self.carrinho_c)):
            print(f'    {i} - ID Produto: {self.carrinho_c[i].id} - Produto: {self.carrinho_c[i].nome} - Preço: {self.carrinho_c[i].preco}')
            total += self.carrinho_c[i].preco

        self.__total = total
        print(f'Total: {self.total}')

        while True:
            op = int(input('1- Compra à vista | 2- Fiado | 3- Cancelar : '))
            if op == 1:
                confirmar = int(input('1- Confirmar compra à vista? | 2- Voltar : '))
                if confirmar == 1:
                    Produto.diminuir_quant(self.carrinho_c)
                    self.add_compra()
                    salvar_produto()
                    break
            elif op == 2:
                confirmar = int(input('1- Confirmar compra fiado? | 2- Voltar : '))
                if confirmar == 1:
                    Produto.diminuir_quant(self.carrinho_c)
                    self.add_compra()
                    salvar_produto()
                    self.cliente_c.devendo = True
                    break
            else:
                break

    def add_compra(self):
        Compra.l_compras.append(self)

    @classmethod
    def historico_de_compras(cls):
        print(Compra.l_compras)
        for compra in Compra.l_compras:
            print(f'ID Compra: {compra.id} - Cliente: {compra.cliente_c.nome}:')
            for j in range(len(compra.carrinho_c)):
                print(f'    {j} - ID Produto: {compra.carrinho_c[j].id} - Produto: {compra.carrinho_c[j].nome} - Preço: {compra.carrinho_c[j].preco}')
            print(f'Total: {compra.total}')
            print()