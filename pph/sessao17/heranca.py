"""
POO - Herança (Inheritance)

O objetivo da herança é reaproveitar código. Também extender nossas classes.

OBS:
    - Com a herança, a partir de uma classe existente, é possível herdar atributos e
    métodos de uma classe herdada.;
    - Quando uma classe é herdada de outra, ela herda todos os métodos e atributos da classe mãe.


Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda.

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matrícula.
"""

# Exemplo de uma classe mãe(super, pai, genérica, etc)
# Funcionário e cliente possuem muitas coisas em comum, nome, sobrenome, cpf. Isso pq ambos são pessoas
# Nesse caso é feita a classe mãe (pessoa), q passará seus atributos e métodos para seus filhos (cliente, funcionário).

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def exibir_nome(self):
        print(f'{self.__nome} {self.__sobrenome}.')

# Classes filhas (subclasses, etc)

class Cliente(Pessoa): # Note q está indicando dentro dos parenteses q a classe Cliente herda da classe Pessoa
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super(Cliente, self).__init__(nome, sobrenome, cpf) # A função super() coloca os argumentos no parâmetro da classe mãe.
        self.__renda = renda # Renda é um atributo exclusivo da classe Cliente, desse modo ela n fica no super()

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da classe mãe
        self.__matricula = matricula

    # Sobrescrita de método: Ocorre quando se reescreve um método herdado da super classe
    def exibir_nome(self):
        print(f'Nome : {self._Pessoa__nome} - Matrícula: {self.__matricula}.')
        #print(self.__nome) # N dá tem q acessar assim: self._Pessoa__nome

        # Podemos acessar diretamente o método da classe mãe
        #super().exibir_nome()


c1 = Cliente('Juniho', 'Castoldi', '123.456.789-70', 10000)
f1 = Funcionario('Luiza', 'Castoldi', '987.654.321-43', 20081128)

c1.exibir_nome()
f1.exibir_nome()

print(c1.__dict__) # Veja q os atributos herdados é chamado pela super classe, e os exclusivos pela classe filha.
print(f1.__dict__)