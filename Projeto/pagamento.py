from datetime import date
class Pagamento:
    
    confirmacao = True
    
    def __init__(self, dados):
        self.__cliente = dados.cliente_f
        self.__dados = dados
        self.__historico_p = []
        self.pagar()

    @property
    def cliente(self):
        return self.__cliente
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
                if self.dados.devendo > 0:
                    print(
                        f'Agora o cliente {self.cliente.nome} está devendo: \033[31mR${self.dados.devendo}.\033[0;0m')
                else:
                    print(f'As contas de {self.cliente.nome} estão em dia.')
                    self.cliente.estado = False

                data = date.today()
                self.__data = f'{data.day}/{data.month}/{data.year}'
                self.historico_p.append(self)
                self.extrato()
            else:
                Pagamento.confirmacao = False
        else:
            print('Insira um valor válido.')
            Pagamento.confirmacao = False

    def extrato(self):
        print(f'Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}')
        print(f'valor: {self.valor}')
        print(f'Data: {self.data}')
        self.historico()

    def historico(self):
        print(f'Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}')
        cont = 0
        for i in range(len(self.historico_p)):
            print(f'{i+1} - Valor do pagamento: {self.historico_p[i].valor} - Data: {self.historico_p[i].data}')

    def total_ja_pago(self):
        total_pago = 0
        for i in range(len(self.historico_p)):
            total_pago += self.historico_p[i].valor

        return total_pago
