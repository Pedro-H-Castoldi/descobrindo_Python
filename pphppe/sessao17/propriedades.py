"""
Propriedades - Properties

Em algumas linguagens de programação como o Java, ao declarar atributos privados nas classses,
é de costume criar métodos públicos para manipular esses atributos. Esses métodos são conhecidos
por getters e setters. Os getters retornam o valor do atributo e os setters dão a possibilidade
de alterar o valor do atributo.


# MODO SEM PROPRIEDADES
class Conta:
    cont = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.cont + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.cont += self.__numero

    def extrato(self):
        print(f'Titular: {self.__titular} - Saldo: {self.__saldo}')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Saque efetuado com sucesso.')
            else:
                print('Saldo insuficiente.')
        else:
            print('ERRO. Insira um valor válido.')

    def depositar(self, valor):
        if valor > 0:
            if valor + self.__saldo <= self.__limite:
                self.__saldo += valor
                print('Deposito efetuado com sucesso.')
            else:
                print('Deposito não efetuado. Limite insuficiente.')
        else:
            print('ERRO. Insira um valor válido.')

    def tranferir(self, valor, destino):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor

                destino.__saldo += valor
                print(f'Tranferência para o destinatário {destino.__titular} com sucesso.')
            else:
                print('Saldo insuficiente,')
        else:
            print('ERRO. Insira um valor válido')

    # Utilizando getters para retornar os valores dos atributos privados e setters para alterar os valores dos atributos (setters são perigosos)
    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def set_limite(self, limite):
        self.__limite = limite

c1 = Conta('Pedro Henrique Castoldi Bezerra', 10000, 1000000)
c2 = Conta('Juliana Castoldi Bezerra', 8788, 1000000)

c1.extrato()

c1.tranferir(5000, c2)

c1.extrato()
c2.extrato()

# Utilizando os getters (podemos trabalhar com os valores dos atributos fora da classe)
# Somar os saldos dos objetos c1 e c2
soma = c1.get_saldo() + c2.get_saldo()
print(f'A soma dos saldos dos titulares {c1.get_titular()} e {c2.get_titular()} é: {soma}')

# Utilizando o setters para aumentar o limite
c1.set_limite(150000)
print(c1.__dict__)
"""

# MODO COM PROPRIEDADES
# Usando propriedades, os getters e setters ficam mais simples e práticos, eles nem sequer são apresentados como métodos
class Conta:
    cont = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.cont + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.cont += self.__numero

    @property # Decorador (modo equivale ao get)
    def numero(self):
        return self.__numero
    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite

    @limite.setter # É usado o nome do property para destacar q se está trabalhando sobre o property feito acima (@nome_property.setter(self)
    def limite(self, novo_limite):
        self.__limite = novo_limite

    # Utilizando property no q seria um método comum
    @property
    def valor_total(self):
        print(f'O valor total do titular {self.titular} é: {self.saldo + self.limite}')


    def extrato(self):
        print(f'Titular: {self.__titular} - Saldo: {self.__saldo}')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Saque efetuado com sucesso.')
            else:
                print('Saldo insuficiente.')
        else:
            print('ERRO. Insira um valor válido.')

    def depositar(self, valor):
        if valor > 0:
            if valor + self.__saldo <= self.__limite:
                self.__saldo += valor
                print('Deposito efetuado com sucesso.')
            else:
                print('Deposito não efetuado. Limite insuficiente.')
        else:
            print('ERRO. Insira um valor válido.')

    def tranferir(self, valor, destino):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor

                destino.__saldo += valor
                print(f'Tranferência para o destinatário {destino.__titular} com sucesso.')
            else:
                print('Saldo insuficiente,')
        else:
            print('ERRO. Insira um valor válido')


c1 = Conta('Pedro Henrique Castoldi Bezerra', 10000, 1000000)
c2 = Conta('Juliana Castoldi Bezerra', 8788, 1000000)

#c1.extrato()

#c1.tranferir(5000, c2)

#c1.extrato()
#c2.extrato()

# Trabalando com o property
# Soma dos saldo dos objetos c1 e c2
print(f'A soma dos saldos dos titulares {c1.titular} e {c2.titular} é de: R${c1.saldo + c2.saldo}.') # Note q n se chama método '()'. Muito mais prático.
#print(f'A soma dos saldos dos titulares {c1.get_titular()} e {c2.get_titular()} é: {c1.get_saldo() + c2.get_saldo()}') # Modo sem property.

# Trabalgando com property.setter
print(c1.__dict__)
c1.limite = 1500000 # Muito mais prático
#c1.set_limite(150000) # Modo sem property.setter
print(c1.__dict__)

c2.valor_total