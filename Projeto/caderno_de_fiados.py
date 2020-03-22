
class Fiado():

    l_compras_fiadas = []

    def __init__(self, compra):
        self.__caderno = []
        self.anotando_fiado(compra)
        self.add_fiado()


    @property
    def caderno(self):
        return self.__caderno
    @caderno.setter
    def caderno(self, compra):
        self.__caderno.append([compra.id, compra.carrinho_c, compra.data,compra.total])
    @property
    def cliente_f(self):
        return self.__cliente_f

    def anotando_fiado(self, compra):
        cont = 0
        obj = type(object)
        if not Fiado.l_compras_fiadas:
            self.__cliente_f = compra.cliente_c
            self.caderno.append(compra)
        else:
            for cliente_v in Fiado.l_compras_fiadas:
                if cliente_v.cliente_f.id == compra.cliente_c.id:
                    cont += 1
                    obj = cliente_v

            if cont != 0:
                self.__cliente_f = ''
                obj.caderno.append(compra)
            elif cont == 0:
                self.__cliente_f = compra.cliente_c
                self.caderno.append(compra)


    def add_fiado(self):
        if self.cliente_f == '':
            pass
        else:
            Fiado.l_compras_fiadas.append(self)

    @classmethod
    def listar_clientes_f(cls):
        print('-- Lista de Fiados --')
        for fiado in Fiado.l_compras_fiadas:
            print(f'ID Cliente: {fiado.cliente_f.id} - Nome: {fiado.cliente_f.nome} - Idade: {fiado.cliente_f.idade}'
                  f'- CPF: {fiado.cliente_f.cpf} - Endereço: {fiado.cliente_f.endereco}')

    @classmethod
    def historico_de_fiados(cls):
        for fiado in Fiado.l_compras_fiadas:
            devendo = 0
            print(f'Cliente- {fiado.cliente_f.nome}:')
            for i in range(len(fiado.caderno)):
                print(f'ID Compra: {fiado.caderno[i].id}:')
                for j in range(len(fiado.caderno[i].carrinho_c)):
                    print(
                        f'    {j + 1} - ID Produto: {fiado.caderno[i].carrinho_c[j].id} - Produto: {fiado.caderno[i].carrinho_c[j].nome} - Preço: {fiado.caderno[i].carrinho_c[j].preco}'
                    )
                    # Fazer isso de maneira mais Pythonica (criar um atributo devendo rodando um for em outro método).
                    devendo += fiado.caderno[i].carrinho_c[j].preco
                print(f'Total: {fiado.caderno[i].total} | data: {fiado.caderno[i].data}')
            print(f'\033[31mDEVENDO AO TODO: R${devendo}\033[0;0m')
            print()