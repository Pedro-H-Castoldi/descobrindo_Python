from datetime import date
import cliente
import salvar_historico_de_pagamentos
import salvar_fiados

class Pagamento:

    historico = []
    confirmar = True

    def __init__(self, dados, tipo):
        self.__dados = dados
        self.__tipo = bool(tipo)
        self.__h_pagamento = []
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
                    self.__data_p = data.strftime('%d/%m/%Y')
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
                        self.__data_p = data.strftime('%d/%m/%Y')
                        self.h_pagamento.append(self)

                        if self.__dados.devendo == 0:
                            print(f'As contas de {self.cliente.nome} estão em dia.')
                            cliente.Cliente.mudar_estatus(self.cliente)
                            self.dados.cliente_f.estado = False
                            salvar_fiados.salvar_fiados()
                            self.extrato()
                            break
                        else:
                            print(f'Agora o cliente {self.cliente.nome} está devendo: \033[31mR${self.dados.devendo}.\033[0;0m')
                            salvar_fiados.salvar_fiados()
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
            print(f'\nData: {self.data_p}')
            print(f'TOTAL: {self.dados.total}')

        else:
            print('EXTRATO')
            print(f'Cliente: {self.cliente.nome}  CPF: {self.cliente.cpf}')
            print(f'TOTAL DO VALOR PAGO: {self.__valor}')
            print(f'\nData: {self.data_p}')
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
        salvar_historico_de_pagamentos.salver_pagamentos()

    @classmethod
    def historico_de_pagamento(cls, cliente):
        encontado = False
        for dado in Pagamento.historico:
            if dado[0].id == cliente:
                encontado = True
                print(f'Cliente: {dado[0].nome}')
                for i in range(len(dado[1])):
                    if dado[1][i].tipo:
                        print(
                            f'  {i + 1} - Valor: {dado[1][i].dados.total} - Data: {dado[1][i].data_p} - Tipo: \033[1;36mPagamento de compra à vista\033[0;0m.')

                    else:
                        print(
                            f'  {i + 1} - valor: {dado[1][i].valor} - Data: {dado[1][i].data_p} - Tipo: \033[1;33mPagamento de conta fiada\033[0;0m.')
                break
        if encontado == False:
            print('O histórico de pagamentos desse cliente não existe.')