"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após a representação do objeto do mundo real de forma computacional,
devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe como
variáveis do tipo definido na classe.
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def cliente_diz_oi(self):
        return f'Oi. eu sou {self.__nome}'

class ContaCorrente:

    cont = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.cont + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.cont = self.__numero

    def identifica_cliente(self):
        # Acessa o atributo cliente, q no caso para ter acesso ao conteúdo privado deve acessa a classe Cliente no atributo nome
        return f'O cliente da conta {self.__numero} é o(a) cliente {self.__cliente._Cliente__nome}' # Acesso de modo errado

class Usiario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


lamp1 = Lampada('amarela', 220, 60)
lamp1.liga_desliga()
print(f'A Lampada está ligada? {lamp1.checa_lampada()}')

cli1 = Cliente('Zanolha', '123.456.789.10')

cc = ContaCorrente(10000, 4500, cli1) # Note q o objeto cli1 da classe Cliente está sendo botado como argumento pro parâmetro cliente na classe ContaCorrente

print(cc.identifica_cliente())

# Acessando um método de outra classe (para isso um objeto da classe q se deseja acessar deve estar presente)
print(cc._ContaCorrente__cliente.cliente_diz_oi())