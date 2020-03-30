from datetime import date
from cliente import Cliente
class Pagamento:

    historico = []
    confirmar = True

    def __init__(self, dados, tipo):
        self.__dados = dados
        self.__tipo = bool(tipo)
        self.__h_pagamento = [] # Historico de pagamentos de um determinado objeto (compras fiadas e à vista).
        self.pagar()
        self.add_h()

    @property
    def dados(self):
        return self.__dados
    @property
    def tipo(self):
        return self.__tipo
    @property
    def valor(self):
        return self.__valor
    @property
    def data_p(self):
        return self.__data_p
    @property
    def h_pagamento(self):
        return self.__h_pagamento
    @h_pagamento.setter
    def h_pagamento(self, dados):
        if self.tipo:
            self.h_pagamento.append([self.tipo, self.dados.carrinho_c, self.data_p, self.dados.total])
        else:
            self.h_pagamento.append([self.tipo, self.data_p, self.valor])
    @property
    def cliente(self):
        return self.__cliente

    def pagar(self):
        if self.tipo:
            self.__cliente = self.dados.cliente_c
            print(f'ID da compra: {self.dados.id}')
            print(f'Cliente: {self.cliente.nome}  CPF: {self.cliente.cpf}')
            for i in range(len(self.dados.carrinho_c)):
                print(f'    {i+1} - Produto {self.dados.carrinho_c[i].nome} - Preço: {self.dados.carrinho_c[i].preco}')
            print(f'\nData: {self.dados.data}')
            print(f'TOTAL: {self.dados.total}')

            while True:
                op = int(input(f'1- Confirmar pagamento no valor de {self.dados.total} | 0- Cancelar: '))
                if op == 1:
                    data = date.today()
                    self.__data_p = data = f'{data.day}/{data.month}/{data.year}'
                    self.h_pagamento.append(self)
                    self.extrato()
                    break
                else:
                    op2 = int(input('1- Confirmar cancelamento | 0- Voltar: '))
                    if op2 == 1:
                        print('Compra cancelada.')
                        break

        else:
            self.__cliente = self.__dados.cliente_f
            Pagamento.confirmar = True
            self.__valor = float(input('Insira o valor: '))
            if self.valor > 0 and self.valor <= self.__dados.devendo:
                op = int(input(f'1- Confirmar pagamento no valor de {self.valor} | 0- Cancelar: '))
                while True:
                    if op == 1:
                        self.dados.devendo -= self.valor
                        self.dados.devendo = float(f'{self.dados.devendo:.2f}')
                        self.dados.total_ja_pago += self.valor
                        data = date.today()
                        self.__data_p = data = f'{data.day}/{data.month}/{data.year}'
                        self.h_pagamento.append(self)

                        if self.__dados.devendo == 0:
                            print(f'As contas de {self.cliente.nome} estão em dia.')
                            Cliente.mudar_estatus(self.cliente)
                            self.dados.cliente_f.estado = False
                            self.add_h()
                            self.extrato()
                            break
                        else:
                            print(f'Agora o cliente {self.cliente.nome} está devendo: \033[31mR${self.dados.devendo}.\033[0;0m')
                            self.extrato()
                            break
                    else:
                        op2 = int(input('1- Confirmar cancelamento | 0- Voltar: '))
                        if op2 == 1:
                            print('Pagamento cancelada.')
                            Pagamento.confirmar = False
                            break
    def extrato(self):
        if self.__tipo:
            print('EXTRATO')
            print(f'ID da compra: {self.dados.id}')
            print(f'Cliente: {self.cliente.nome}  CPF: {self.cliente.cpf}')
            for i in range(len(self.dados.carrinho_c)):
                print(f'    {i + 1} - Produto {self.__dados.carrinho_c[i].nome} - Preço: {self.__dados.carrinho_c[i].preco}')
            print(f'\nData: {self.dados.data}')
            print(f'TOTAL: {self.dados.total}')

        else:
            print('EXTRATO')
            print(f'Cliente: {self.cliente.nome}  CPF: {self.cliente.cpf}')
            print(f'TOTAL DO VALOR PAGO: {self.__valor}')
            print(f'DEVENDO: {self.dados.devendo}')

    def add_h(self):
        if not Pagamento.historico:
            Pagamento.historico.append([self.cliente, self.h_pagamento])
        else:
            ver = False
            obj = type(object)
            for dado in Pagamento.historico:
                if dado[0].id == self.cliente.id:
                    ver = True
                    obj = dado[1]
                    break

            if ver:
                obj.append(self) # Isspo pode ser utilizado no caderno de fiados
            else:
                Pagamento.historico.append([self.cliente, self.h_pagamento])

        for dado in Pagamento.historico:
            print(f'Cliente: {dado[0].nome}')
            for i in range(len(dado[1])):
                if dado[1][i].tipo:
                    print(f'  {i+1} - Valor: {dado[1][i].dados.total} - Data: {dado[1][i].data_p} - Tipo: Pagamento de compra à vista.')

                else:
                    print(f'  {i+1} - valor: {dado[1][i].valor} - Data: {dado[1][i].data_p} - Tipo: Pagamento de conta fiada.')
"""
    # ESSA CLASSE NÃO DEVERIA EXISTIR. TUDO ISSO VAI PRO CADERNO DE DEVEDORES
    confirmacao = True
    
    def __init__(self, dados):
        self.__cliente_p = dados.cliente_f
        self.__dados = dados
        self.__historico_p = []
        self.pagar()

    @property
    def cliente_p(self):
        return self.__cliente_p
    @property
    def dados(self):
        return self.__dados
    @property
    def valor(self):
        return self.__valor
    @property
    def data(self):
        return self.__data
    @property
    def historico_p(self):
        return self.__historico_p
    @historico_p.setter
    def historico_p(self, obj):
        self.__historico_p.append([obj.valor, obj.data])


    def pagar(self):
        Pagamento.confirmacao = True
        self.__valor = float(input('Insira o valor do pagamento: '))

        if self.valor > 0 and self.valor <= self.dados.devendo:
            op = int(input(f'1- Confirmar pagamento | 0- Cancelar: '))
            if op == 1:
                self.dados.devendo -= self.valor
                data = date.today()
                self.__data = f'{data.day}/{data.month}/{data.year}'
                self.historico_p.append(self)

                if self.dados.devendo > 0:
                    print(
                        f'Agora o cliente {self.cliente_p.nome} está devendo: \033[31mR${self.dados.devendo}.\033[0;0m')
                else:
                    print(f'As contas de {self.cliente_p.nome} estão em dia.')
                    self.cliente_p.estado = False
                    Cliente.mudar_estatus(self.cliente_p)


                self.extrato()
            else:
                Pagamento.confirmacao = False
        else:
            print('Insira um valor válido.')
            Pagamento.confirmacao = False



# ISSO PODE FICAR EM UMA CLASSE SERAPARADA (A MESMA DE HISTORICO)
    def extrato(self):
        print(f'Cliente: {self.cliente_p.nome} - CPF: {self.cliente_p.cpf}')
        print(f'valor: {self.valor}')
        print(f'Data: {self.data}')
        self.historico()

# ISSO DEVE SER UMA CLASSE SEPARADA, ONDE ABRANJE OS PAGAMENTOS À VISTA E PAGAMENTOS DE PRODUTOS FIADOS (VAI SER UMA CONDIÇÃO PARA FIADO E PARA À VISTA)
    def historico(self):
        print(f'Cliente: {self.cliente_p.nome} - CPF: {self.cliente_p.cpf}')
        cont = 0
        for i in range(len(self.historico_p)):
            print(f'{i+1} - Valor do pagamento: {self.historico_p[i].valor} - Data: {self.historico_p[i].data}')

    def total_ja_pago(self):
        total_pago = 0
        for i in range(len(self.historico_p)):
            total_pago += self.historico_p[i].valor

        return total_pago
"""