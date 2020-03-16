from cliente import Cliente
from produto import Produto
from compra import Compra
"""
ATENÇÃO
    - CARRINHO SERÁ UMA NOVA CLASSE, O OBJETO CARRINHO TERÁ: CLIENTE, PRODUTOS(LISTA) - ATRIBUTOS DE INSTÂNCIA;
    - A CLASSE COMPRA RECEBERÁ O OBJETO CARRINHO, NELA OS ATRIBUTOS SERÃO: ID_COMPRA, OBJETO CARRINHO - ATRIBUTOS DE INSTÂNCIA.
    - A CLASSE COMPRA TERÁ UM ATRIBUTO DE CLASSE: LISTA_DE_COMPRAS(LISTA). NESSE ATRÍBUTO SERÃO ADICIONADOS TODOS OS OBJETOS DO TIPO COMPRA
    DE TODOS OS CLIENTES DO SISTEMA.
"""
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
        c_cliente = str(input('Insira o nome completo do cliente: '))
        c_cliente = Cliente.listar_clientes_nome(c_cliente)

        if c_cliente:
            self.__cliente = c_cliente
            self.encher_carrinho()

    def encher_carrinho(self):
        self.__l_carrinho.clear()

        while True:
            c_produto = str(input('Insira o nome do produto: '))
            c_produto = Produto.listar_produtos_nome(c_produto)

            if c_produto:
                if c_produto.estoque:
                    self.__l_carrinho.append(c_produto)
                else:
                    print('Produto faltando.')

            op = int(input('1- Continuar Comprando | 2- Ir para o Caixa | 0- Desfazer Carrinho: '))
            if op == 2:
                compra = Compra(self)
                compra.comprar()
                break
            elif op == 0:
                self.__l_carrinho.clear()
                break



"""
def compras():
    cliente = idc = idp = idcompra = erro = teve = 0
    opid = '*'

    idc = int(input('Insira o ID do cliente: '))

    while True:
        for i in clientes:
             if i == idc:
                 cliente = idc
                 break

        if cliente > 0:
            idp = int(input('Insira o ID do produto: '))
            for j in produtos:
                if j == idp:
                    comprado.append(f'{produtos[idp][0]} R${produtos[idp][1]}')
                    erro = teve = 1
                    break

            if erro == 0:
                print('ID do produto não se encontra no sistema.')

            erro = 0


        else:
            print('ID do cliente não se encontra no sistema.')
            opid = str(input('Tentar novamente? S / N: '))
            if opid in 'Nn':
                return 0
            else:
                idc = int(input('Insira o ID do cliente: '))

        if opid == 's':
            opid = '*'
        else:
            op = str(input('Continuar comprando? S / N: '))
            if op in 'Nn':
                break

    idcompra = 1 + idc
    c = comprado
    print(type(c))
    carrinho.update({idcompra: [cliente, clientes[cliente], comprado]})

    if teve > 0:
        op = str(input('Compra fiada?: '))
        if op in 'Ss':
            clientes[cliente][4] = False
            devendo.update(carrinho) # Corrigir {}
            print(devendo)
    else:
        print('Fim.')
"""