"""
POO - Polimorfismo

Vamos dividir esse nome em duas palavras:
    - Poli -> Muitas;
    - Morfis -> Formas.

Ou seja, Polimorfismo quer dizer muitas formas.

Quando se reimplementa um método de uma super classe numa classe filha, essa operação é chamada de sobrecrita de método (Overrinding).
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        # Obriga a classe filha implementar o método, sobrecrevendo o método dentro da mesma.
        raise NotImplementedError('A Classe filha precisa implementar esse método')

    def comer(self):
        return f'{self.nome} está comendo.'


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.nome} fala miau.' # Se n implementar dá erro.

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.nome} fala riu riu.' # Se n implementar da erro.

jigglypuff = Gato('Jigglypuff')
hantaro = Rato('Hantaro')

print(jigglypuff.comer())
print(jigglypuff.falar())

print(hantaro.comer())
print(hantaro.falar())
