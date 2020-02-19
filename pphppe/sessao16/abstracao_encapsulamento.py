"""
POO - Abstração e Encapsulamento

O Grande objetivo é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> Cápsula


                Classe
        ---------------------
        | atributos e métodos |
        |_____________________|

Relembrando atributos e métodos privados em Python
    - Imagine q temos uma classe chamada Pessoa contendo um atributo privado chamado __nome
    e um método privado chamado __falar().
    Esses elementos só devem/deveriam ser acessados dentro da classe. Mas o Python n bloqueia esse acesso
    fora da classe. Em Python ocorre o fenômeno chamado Name Mangling, q faz uma alteração de como
    acessar aos elementos privados.

Exemplo de acessar atributo/elemento privado fora da classe em Python:
    - instancia_Pessoa__nome # Acessando atributo privado
    - instancia_Pessoa__falar() # Acessando método privado


Abstração em POO, é expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário (É como a chamada telefonica,
a operadora esconde os passos conplexos de se estabelecer uma conexão entre os 2 telefones e mostra só o q realmente o usuário deseja ver).
"""

# Encapsular é deixar o nosso código seguro dentro da classe, com atributos privados, etc.

class Conta:
    cont = 500

    def __init__(self, titular, saldo, limite):
        if(saldo <= limite):
            self.__numero = Conta.cont
            self.__titular = titular
            self.__saldo = saldo
            self.__limite = limite
            Conta.cont += 1
        else:
            print('ERRO: Saldo maior que o limite.')

    def extrato(self):
        return f'TITULAR: {self.__titular}\nNÚMERO: {self.__numero}\nSALDO: {self.__saldo}\nLIMITE: {self.__limite}'

    def depositar(self, valor):
        if valor > 0:
            if self.__saldo + valor <= self.__limite:
                self.__saldo += valor
            else:
                print('Limite insuficiente.')
        else:
            print('O valor deve ser acima de 0.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor deve ser acima de 0.')

    def transferencia(self, valor, conta_destino):
        # PASSO 1-> Remover o valor do saldo de quem fará a tranferência
        self.__saldo -= valor
        # Tbm poderia ser feito assim (mais prático)
        #self.sacar(valor)

        self.__saldo -= 10 # Cobrança da tranferência

        # PASSO 2-> Adicionar à conta destino o valor mandado no saldo
        conta_destino.__saldo += valor
        # Tbm poderia ser feito assim (mais prático)
        #conta_destino.depositar(valor)


cliente = Conta('Juninho', 5000, 10000)
cliente2 = Conta('Zanolha', 2500, 2500)

#cliente2.depositar(1)
#cliente2.sacar(100)

print(cliente.extrato())
print(cliente2.extrato())

cliente2.transferencia(100, cliente) # Saldo o cliene2 cairá para 2490 e do cliente subirá para 5100
print()

print(cliente.extrato())
print(cliente2.extrato())

#cliente2.depositar(10000)

# OBS: N é obrigado deixar os métodos privados para fazer o encapsulamento.


