"""
POO - Atributos

Atributos -> Representam as características do objeto. Desse modo, podemos representar os estados
de um objeto computacionalmente.


Em Python, dividimos os atributos em 3 tipos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinamicos.

# Atributos de Instância: São atributos declarados dentro de um método construtor.

# OBS: Método Construtor é um método responsável por construir um objeto.


 Em Python, por convenção, ficou decidido q todo atributo de uma calsse é público,
 ou seja, pode ser acessado em todo o projeto. Caso seja necessário tratar um atributo como privado,
 ou seja, q deve ser utilizado/acessado somente dentro da própria classe onde está declarado,
 utilizamos "__" duplo underscore no inicio do seu nome (isso é conhecido como Name Mangling).



# Classes com Atributos de Instância Público
class Lampada:

    def __init__(self, volts, cor): # Esse é o construtor (declaramos os atributos já dentro do contrutor...).
        self.volts = volts
        self.cor = cor
        self.ligada = False

class Cliente:

    def __init__(self, nome, endereco, data_nasc, cpf):
        self.nome = nome
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.cpf = cpf

# Classes com Atributos de Instância Privado
class Acesso:

    def __init__(self, email, senha):
        self.email = email # Público
        self.__senha = senha # Privado

# OBS: No Python, mesmo o atributo sendo privado, n necessáriamente ele n poderá ser acessado fora da classe.
# Ainda podemos ter acesso a ele de modo n recomendado..

user = Acesso('pedrohenrique.bzr@gmail.com', '24091996') # Criando um objeto e utilizando o construtor para definir seus atributos

# Acessando atributo público
print(user.email)

# Acessando atributo privado dá um erro
#print(user.senha) # Erro
#print(user.__senha) # Erro

# Acessando de modo q n dê erro, mas n recomendado, ou seja, vc pode, mas n deveria..
print(user._Acesso__senha) # Name Mangling


# Acessando atributo privado de modo sem preocupação, já q o mesmo será acessado dentro da sua classe
class Pessoa:
    def __init__(self, nome, tel, cpf):
        self.nome = nome
        self.tel = tel
        self.__cpf = cpf

    # Criando um método q permitirá acessar ao atributo privado dentro de sua classe nativa
    def acesso_atributo_privado(self):
        return self.__cpf

juninho = Pessoa('Juninho Castoldi Bezerra', '33333333333', 8888888888)
print(juninho.nome)
print(juninho.tel)
print(juninho.acesso_atributo_privado()) # Executando o método para ter acesso ao atributo provado



O q significa atributos de instância?
    Significa q ao criarmos instâncias/objetos de uma classe, todas as instâncias/objetos terão esses atributos



class User:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

user1 = User('user1@gmail.com', '12345')
user2 = User('user2@gmail.com', '54321')

print(user1.email)
print(user2.email)




# Atributo de Classe
# Esses atributos são declarados diretamente da classe, ou seja, fora do construtor.
# Geralmente já é inicializado com um valor e esse valor é compartilhado com todas as instâncias da classe.

# Ex de Atributo de Classe
class Produto:
    # Atributo de Classe
    imposto = 1.05
    contador = 0 # Contador para o ID

    def __init__(self, nome, descricao, preco):
        self.id = (Produto.contador + 1) # ID recebe o valor do contador + 1
        self.nome = nome
        self.descricao = descricao
        self.preco = (preco * Produto.imposto) # Adicionando o valor do imposto ao valor do produto

        Produto.contador = self.id # O contador recebe o valor do ID


p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox One', 'Video Game', 2800)

# Note q o valor do imposto para todos os objetos é igual
print(p1.imposto) # Acesso incorreto de um atributo de classe
print(p2.imposto) # Acesso incorreto de um atributo de classe

# Valor do produto mais a taxa de imposto
print(p1.preco) # 2300 -> 2415
print(p2.preco) # 2800 -> 2949

print(p1.id) # 1
print(p2.id) # 2

print(Produto.imposto) # Podemos acessar o valor do atributo de classe sem chamar um objeto (acesso de modo correto a um atributo de classe).

# OBS: Em linguagens como o Java, os atributos conhecidos como Atributos de Classe aki no Python, são definidos como Atributos Estáticos.
"""

class Produto:
    imposto = 1.05 # Atributo de Classe
    contador = 0 # Contador para o ID

    def __init__(self, nome, descricao, preco):
        self.id = (Produto.contador + 1) # ID recebe o valor do contador + 1
        self.nome = nome
        self.descricao = descricao
        self.preco = (preco * Produto.imposto) # Adicionando o valor do imposto ao valor do produto

        Produto.contador = self.id # O contador recebe o valor do ID

# Atributos Dinâmicos: Um atributo de instância q pode ser criado em tempo de execução.
# OBS: O Atributo Dinâmico será exclusivo somente da instância q o criou

# EX
feijao = Produto('Feijão', 'Marcearia', 5.40)
ventilador = Produto('Ventilador Mondial', 'Eletrodomestico', 220.30)

# Criando um Atributo Dinâmico
feijao.peso = '5kg'

print(f'Produto: {feijao.nome}      Descrição: {feijao.descricao}       Peso: {feijao.peso}       Preço: {feijao.preco:.2f}')

# Erro pois n existe o atributo peso no ventilador
#print(f'Produto: {ventilador.nome}      Descrição: {ventilador.descricao}       Peso: {ventilador.peso}       Preço: {ventilador.preco:.2f}')



print(feijao.__dict__) # Retorna um dicionário com todos os atributos do objeto
print(ventilador.__dict__)
#print(Produto.__dict__) # Retorna um dicionário com todos os atributos da Classe

# Removendo atributos
del feijao.peso # Removendo peso do objeto feijão
del feijao.descricao

print(feijao.__dict__)
print(ventilador.__dict__)
