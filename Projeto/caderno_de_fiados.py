import pagamento
import compra

class Fiado:

    l_compras_fiadas = []

    def __init__(self, compra):
        self.__caderno = []
        self.__cliente_f = compra.cliente_c
        self.anotando_fiado(compra)

    @property
    def caderno(self):
        return self.__caderno
    @caderno.setter
    def caderno(self, compra):
        self.__caderno.append([compra.id, compra.carrinho_c, compra.data, compra.total])
    @property
    def cliente_f(self):
        return self.__cliente_f
    @property
    def total_ja_pago(self):
        return self.__total_ja_pago
    @total_ja_pago.setter
    def total_ja_pago(self, valor):
        self.__total_ja_pago = valor
    @property
    def devendo(self):
        return self.__devendo
    @devendo.setter
    def devendo(self, pagar):
        self.__devendo = pagar

    def anotando_fiado(self, compra):
        ver = False
        obj = type(object)
        if not Fiado.l_compras_fiadas:
            self.__total_ja_pago = 0
            self.caderno.append(compra)
            self.add_devendo()
            Fiado.l_compras_fiadas.append(self)
        else:
            for cliente_v in Fiado.l_compras_fiadas:
                if cliente_v.cliente_f.id == compra.cliente_c.id:
                    ver = True
                    obj = cliente_v
                    break

            if ver:
                obj.cliente_f.estado = True
                obj.caderno.append(compra)
                obj.add_devendo()

            else:
                self.__total_ja_pago = 0
                self.caderno.append(compra)
                self.add_devendo()
                Fiado.l_compras_fiadas.append(self)

    def add_devendo(self):
        total = 0
        for i in range(len(self.caderno)):
            for j in range(len(self.caderno[i].carrinho_c)):
                total += self.caderno[i].total

        devendo = total - self.total_ja_pago
        devendo = float(f'{devendo:.2f}')
        self.__devendo = devendo

    @classmethod
    def listar_clientes_f(cls):
        print('-- Lista de Fiados --')
        for fiado in Fiado.l_compras_fiadas:
            if fiado.cliente_f.estado:
                print(
                    f'ID Cliente: {fiado.cliente_f.id} - Nome: {fiado.cliente_f.nome} - Idade: {fiado.cliente_f.idade}'
                    f' - CPF: {fiado.cliente_f.cpf} - Endereço: {fiado.cliente_f.endereco} - \033[31mDEVENDO: {fiado.devendo}\033[0;0m')

    @classmethod
    def devedor_compras(cls, nome):
        encontrado = False
        for fiado in Fiado.l_compras_fiadas:
            if fiado.cliente_f.nome == nome:
                encontrado = True
                print(f'Cliente- {fiado.cliente_f.nome}:')
                for i in range(len(fiado.caderno)):
                    print(f'ID Compra: {fiado.caderno[i].id}')
                    for j in range(len(fiado.caderno[i].carrinho_c)):
                        print(
                            f'    {j + 1} - ID Produto: {fiado.caderno[i].carrinho_c[j].id} - Produto: {fiado.caderno[i].carrinho_c[j].nome} - Preço: {fiado.caderno[i].carrinho_c[j].preco}'
                        )
                    print(f'Total: {fiado.caderno[i].total} | data: {fiado.caderno[i].data}')
                print(f'\033[31mDEVENDO AO TODO: R${fiado.devendo}\033[0;0m')
                print()

                while True:
                    op = int(input('1- Pagar | 2- Histórico de Pagamentos | 3- Historico de Compras | 0- Voltar: '))
                    if op == 1:
                        pagar = pagamento.Pagamento(fiado, False)
                        if pagamento.Pagamento.confirmar:
                            break
                    elif op == 2:
                        pagamento.Pagamento.historico_de_pagamento(fiado.cliente_f.id)
                        break
                    elif op == 3:
                        compra.Compra.historico_de_compras_cliente(fiado.cliente_f.id)
                        break
                    else:
                        break
        if encontrado == False:
            print('Cliente não encontrado no caderno de devedores.')

    @classmethod
    def historico_de_fiados(cls):
        for fiado in Fiado.l_compras_fiadas:
            print(f'Cliente- {fiado.cliente_f.nome}:')
            for i in range(len(fiado.caderno)):
                print(f'ID Compra: {fiado.caderno[i].id}')
                for j in range(len(fiado.caderno[i].carrinho_c)):
                    print(
                        f'    {j + 1} - ID Produto: {fiado.caderno[i].carrinho_c[j].id} - Produto: {fiado.caderno[i].carrinho_c[j].nome} - Preço: {fiado.caderno[i].carrinho_c[j].preco}'
                    )
                print(f'Total: {fiado.caderno[i].total} | data: {fiado.caderno[i].data}')
            print(f'\033[31mDEVENDO AO TODO: R${fiado.devendo}\033[0;0m')
            print()