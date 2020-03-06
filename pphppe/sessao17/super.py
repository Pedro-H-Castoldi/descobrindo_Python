"""
POO - O método super()

O método super() se refere à super classe (classe mãe, etc)
"""

# EX
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def barulho(self, som):
        print(f'O {self.__nome} faz {som}.')

class Humano(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie) # Modo usando super()
        self.__raca = raca
        super().barulho('Com o método super é possível acessar qualquer método/atributo da super classe.') # Mas sem q estar no escopo do construtor.

class Cachorro(Animal):

    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie) # Modo usando o nome da super classe (Animal) - N comendado
        self.__raca = raca

h = Humano('Pyong Lee', 'primata', 'asiática')
c = Cachorro('Juninho', 'canino', 'piri')

h.barulho('Eae!!!')
c.barulho('Au Au Au')