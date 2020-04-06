from produto import Produto
import pagamento
import caderno_de_fiados
from salvar_produto import salvar_produto
from datetime import date
import salvar_fiados
import salvar_historico_de_compras

class Compra:

    cont = 0
    l_compras = []

    def __init__(self, carrinho):
        self. __id = Compra.cont + 1
        self.__carrinho_c = carrinho.l_carrinho
        self.__cliente_c = carrinho.cliente
        data = date.today()
        data = f'{data.day}/{data.month}/{data.year}'
        self.__data = data
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
    def data(self):
        return self.__data
    @property
    def total(self):
        return self.__total
    @property
    def tipo(self):
        return self.__tipo

    def comprar(self):
        total = 0

        print(f'Cliente {self.cliente_c.nome}:')

        for i in range(len(self.carrinho_c)):
            print(f'    {i+1} - ID Produto: {self.carrinho_c[i].id} - Produto: {self.carrinho_c[i].nome} - Preço: {self.carrinho_c[i].preco}')
            total += self.carrinho_c[i].preco

        total = float(f'{total:.2f}')
        self.__total = total
        print(f'Total: {self.total} | Data {self.data}')

        while True:
            op = int(input('1- Compra à vista | 2- Fiado | 3- Cancelar : '))
            if op == 1:
                confirmar = int(input('1- Confirmar compra à vista? | 2- Voltar : '))
                if confirmar == 1:
                    Produto.diminuir_quant(self.carrinho_c)
                    self.__tipo = True
                    self.add_compra()
                    salvar_produto()
                    pagar = pagamento.Pagamento(self, True)
                    break
            elif op == 2:
                confirmar = int(input('1- Confirmar compra fiado? | 2- Voltar : '))
                if confirmar == 1:
                    Produto.diminuir_quant(self.carrinho_c)
                    self.__tipo = False
                    self.add_compra()
                    salvar_produto()
                    self.cliente_c.estado = True
                    fiado = caderno_de_fiados.Fiado(self)
                    salvar_fiados.salvar_fiados()
                    break
            else:
                break

    def add_compra(self):
        Compra.l_compras.append(self)
        salvar_historico_de_compras.salvar_comprar()

    @classmethod
    def historico_de_compras_cliente(cls, id):
        encontrado = False
        for compra in Compra.l_compras:
            if id == compra.cliente_c.id:
                encontrado = True
                if compra.tipo:
                    print(f'ID Compra: {compra.id} - Tipo: À Vista:')
                else:
                    print(f'ID Compra: {compra.id} - Tipo: Fiado:')
                for i in range(len(compra.carrinho_c)):
                    print(f'    {i+1} - ID Produto: {compra.carrinho_c[i].id} - Produto: {compra.carrinho_c[i].nome} - Preço: {compra.carrinho_c[i].preco}')
                print(f'Total: {compra.total} | Data: {compra.data}')
                print()

        if encontrado == False:
            print('Cliente não possui um histórico de compras.')

    @classmethod
    def historico_de_compras(cls):
        for compra in Compra.l_compras:
            if compra.tipo:
                print(f'ID Compra: {compra.id} - Tipo: À Vista - Cliente: {compra.cliente_c.nome}:')
            else:
                print(f'ID Compra: {compra.id} - Tipo: Fiada - Cliente: {compra.cliente_c.nome}:')
            for i in range(len(compra.carrinho_c)):
                print(f'    {i+1} - ID Produto: {compra.carrinho_c[i].id} - Produto: {compra.carrinho_c[i].nome} - Preço: {compra.carrinho_c[i].preco}')
            print(f'Total: {compra.total} | Data: {compra.data}')
            print()