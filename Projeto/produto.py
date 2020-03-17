
class Produto:

    cont = 0
    l_produtos = []

    def __init__(self, nome, tipo, preco, quant):
        self.__id = Produto.cont + 1
        self.__nome = nome.title()
        self.__tipo = tipo
        self.__preco = preco
        self.__quant = quant
        self.ver_estoque()
        Produto.cont = self.__id

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, n_nome):
        self.__nome = n_nome

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, n_tipo):
        self.__tipo = n_tipo

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, n_preco):
        self.__preco = n_preco

    @property
    def quant(self):
        return self.__quant
    @quant.setter
    def quant(self, n_quant):
        self.__quant = n_quant

    @property
    def estoque(self):
        return self.__estoque

    def ver_estoque(self):
        if self.__quant > 0:
            self.__estoque = True
        else:
            self.__estoque = False

    def add_produto(self):
        Produto.l_produtos.append(self)

    @classmethod
    def diminuir_quant(cls, carrinho):
        for i in range(len(carrinho)):
            for j in range(len(Produto.l_produtos)):
                if carrinho[i].id == Produto.l_produtos[j].id:
                    Produto.l_produtos[j].quant -= 1

    @classmethod
    def listar_produtos(cls):
        for produto in Produto.l_produtos:
            print(f'ID: {produto.id}  -  Nome: {produto.nome}  - Tipo: {produto.tipo}'
                  f'-  Preço: {produto.preco:.2f}  -  Quantidade: {produto.quant} - Estoque: {produto.estoque}')

    @classmethod
    def listar_produtos_nome(cls, nome):
        encontrado = False
        cont_ex = 0
        for produto in Produto.l_produtos:
            if produto.nome == nome:
                encontrado = True
                print(f'ID: {produto.id}  -  Nome: {produto.nome}  - Tipo: {produto.tipo}'
                      f'  -  Preço: {produto.preco:.2f}  -  Quantidade: {produto.quant} - Estoque: {produto.estoque}')
                return produto

        if not encontrado:
            print('Produto não encontrado')
            return False






"""
                Esse CRUD será feito por meio de outro método..
                op = int(input('1- Editar | 2- Excluir | 0- Ok: '))
                if op == 1:
                    Produto.editar_produto(produto)
                elif op == 2:
                    Produto.remover_produto(cont_ex)
            cont_ex += 1

        if not encontrado:
            print('Produto não encontrado.')
           

    @classmethod
    def editar_produto(cls, o_produto):
        e_nome = str(input(f'Nome - {o_produto.nome}: '))
        e_tipo = str(input(f'Tipo - {o_produto.tipo}: '))
        e_preco = float(input(f'Preço - {o_produto.preco}: '))
        e_quant = int(input(f'Quantidade - {o_produto.quant}: '))

        o_produto.nome = e_nome
        o_produto.tipo = e_tipo
        o_produto.preco = e_preco
        o_produto.quant = e_quant
        print('Produto editado com sucesso.')

    @classmethod
    def remover_produto(cls, ex):
        Produto.l_produtos.pop(ex)
        print(f'Produto removido com sucesso.')
"""
