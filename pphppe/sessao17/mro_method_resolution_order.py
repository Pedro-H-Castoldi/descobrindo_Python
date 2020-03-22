"""
POO - Method Resolution Order (MRO)

Method Resolution Order (Resolução de Ordem de Métodos) , é a ordem
de execução dos métodos (quem será executado primeiro).

Em Python podemos conferir o MRO de 3 maneiras:
    - Via propriedade da classe __mro__;
    - Via método mro();
    - Via help.

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome} da terra.'

    def andar(self):
        return f'{self.nome} está andando.'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome} da água.'

    def nadar(self):
        return f'{self.nome} está nadando.'

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

pingu = Pinguim('Pingu')

print(pingu.cumprimentar()) # Vai aparecer da terra pois a classe Terra está sendo herdada primeiro.

# Vendo o MRO por propriedade
print(Pinguim.__mro__)

# Via método
print(Pinguim.mro())

# Via help
print(help(Pinguim))