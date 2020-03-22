"""
POO - Herança Múltipla

É a possibilidade de uma classe herdar de múltiplas classes. Desse modo,
a classe filha herda todos os atributos e métodos das super classes.

OBS: A Herança Múltipla pode ser feita de duas maneiras:
    - Multiderivação Direta;
    - Multiderivação Indireta.


# Exemplo de Multiderivação Direta
class Base1():
    pass

class Base2():
    pass

class Base3():
    pass

class Multipladerivacao(Base1, Base2, Base3): # Note q a herança é dada diretamente na classe Multipladerivacao
    pass


# Exemplo de Multipladerivação Indireta
class Base1():
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multipladerivacao(Base3): # Note q a classe Multipladerivacao herda de modo indiretamente as classe  Base2 e Base 1
    pass

# OBS: N importa se a classe herdar diretamente ou n outra classe, a mesma herdará todos os atributos e métodos das super classes.

"""

# EX de Herança Múltipla

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Olá. Meu nome é {self.nome}.'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Olá. Meu nome é {self.nome} da Terra.'

    def andar(self):
        return f'{self.nome} está andando.'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Olá. Meu nome é {self.nome} do mar.'

    def nadar(self):
        return f'{self.nome} está nadando.'

class TerestreAquatico(Aquatico, Terrestre): # Retornará: "Olá. Meu nome é pinguim do mar.". Isso pq a classe Aquatico foi chamada antes da Terrestre.

    def __init__(self, nome):
        super().__init__(nome)


tatu = Terrestre('Tatu')
print(tatu.cumprimentar())
print(tatu.andar())

print()

tubarao = Aquatico('Tubarão')
print(tubarao.cumprimentar())
print(tubarao.nadar())

print()

pinguim = TerestreAquatico('Pinguim')
print(pinguim.cumprimentar()) # Aparece pinguim do mar e não pinguim da terra. Isso pq a primeira classe está primeiro à esquerda na chamada de herança.
print(pinguim.andar())
print(pinguim.nadar())

print()
# Saber se um objeto é uma instância de uma classe
print(f'Pinguim é instância de Terrestre? : {isinstance(pinguim, Terrestre)}') # True
print(f'Tatu é instância de Aquatico? : {isinstance(tatu, Aquatico)}') # False
print(f'Tubarão é instância de objeto? : {isinstance(tubarao, object)}') # True (todos as classes são instâncias de object).