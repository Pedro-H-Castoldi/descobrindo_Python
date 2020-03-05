"""
POO - Métodos
- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
q o objeto pode realizar no sistema.

Em Python, dividimos os métodos em 2 tipos: Métodos de Instância e Métodos de Classe.

O método __init__() é um método especial chamado de Contrutor, a função dele é de construir o objeto.

OBS:
    - Em Puthon, todo elemento q inicia e termina com duplo underline é chamado de Dunder (Double Underline);
    - Os métodos Dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por mais q possamos criar nossos próprios métodos Dunder (underline no início e no fim) n é aconselhado!
Python tem vários métodos com essa forma de nomeclatura, isso pode acarretar à mudança de comportamento desses métodos internos da linguagem.
Desse modo, evite ao máximo criar funções Dunder. Se possivel nunca o faça.



# Método de Instância (são os métodos q estão dentro da classe)

class Lampada:

    def __init__(self, cor, voltagem, ligada):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__ligada = ligada

class ContaCorrente:

    cont = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.cont + 1
        self.__limite = limite
        self.__saldo = saldo

        ContaCorrente.cont = self.__numero


class Produto:

    importo = 1.05
    cont = 0

    def __init__(self, nome, descricao, preco):
        self.__id = Produto.cont + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = (preco * Produto.importo)

        Produto.cont = self.__id

    # Método de instância
    def desconto(self, porcentagem):
        #Retorna o valor do produto com desconto
        return self.__preco * (100 - porcentagem) / 100

# Criptografar senha
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 200000, salt_size= 16) # Foi chamada a biblioteca de criptografia e demos mais força a ela.

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # Verificar se a senha inserida é a mesma q foi criada
    def senha_verifica(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False



p1 = Produto('Notebook Dell', 'Eletrônico', 2100)
#print(p1.__dict__)
print(p1.desconto(20))
#print(p1.__dict__)


user1 = Usuario('Pedro Henrique', 'Castoldi Bezerra', 'pedrohenrique.bzr@gmail.com', '54321')
print(user1.nome_comple


print('Cadastramento de usuário')
nome = str(input('Nome: '))
sobrenome = str(input('sobrenome: '))
email = str(input('E-mail: '))
senha = str(input('Senha: '))
confirmar_senha = str(input('Confirme a senha: '))

if senha == confirmar_senha:
    user1 = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Cadastro feito com sucesso!')

print('\nLogin')
senha = str(input('Informe a senha: '))

if user1.senha_verifica(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha do usuário criptografada: {user1._Usuario__senha}.') # Modo de acesso n correto
"""

# Método de Instância - métodos q trabalham com atributos de instância

class Lampada:

    def __init__(self, cor, voltagem, ligada):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__ligada = ligada

class ContaCorrente:

    cont = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.cont + 1
        self.__limite = limite
        self.__saldo = saldo

        ContaCorrente.cont = self.__numero


class Produto:

    importo = 1.05
    cont = 0

    def __init__(self, nome, descricao, preco):
        self.__id = Produto.cont + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = (preco * Produto.importo)

        Produto.cont = self.__id

    # Método de instância
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__preco * (100 - porcentagem) / 100


# Métodos de Classe - Métodos q trabalham sem utilizar os atributos de instância (esses métodos são conhecidos como Métodos Estáticos em outras linguagens)

# Criptografar senha
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    cont = 0

    # Método de claase
    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}') # Retorna o nome da classe Usiario.
        print(f'Temos {cls.cont} usuario(s) no sistema.')

    # Método estático (a difereça entre ele e o de classe é q o método estático n recebe nada como parâmetro, já do de classe recebe a classe)
    @staticmethod
    def definicao():
        return 'UTFX335'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.cont + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 200000, salt_size= 16) # Foi chamada a biblioteca de criptografia e demos mais força a ela.
        Usuario.cont = self.__id
        print(f'Usiário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # Verificar se a senha inserida é a mesma q foi criada
    def senha_verifica(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método privado
    def __gera_usuario(self):
        return self.__email.split('@')[0] # Retorna apenas a casa 0 da lista esplit, ou seja, antes do @


#user1 = Usuario('Jigglypuff', 'Castoldi Bezerra', 'jipuff@gmail.com', '12345')
#Usuario.conta_usuario() # Forma correta.
#user.conta_usuario() # Forma incorreta


print(Usuario.cont)
print(Usuario.definicao())

user2 = Usuario('Zanolha', 'Castoldi Bezerra', 'zanolha@gmail.com', '43210')
print(user2.cont)
print(user2.definicao()) # Note q pra chamar o método estático tem q botar os parenteses


