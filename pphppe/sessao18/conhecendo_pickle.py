"""
Conhecendo Pickle

A Função do Pickle é realizar o seguinte processo:
    - Objeto Python -> Binarização;
    - Binarização -> Objeto Python.

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle n é seguro contra dados malicioso, desse modo,
n é recomendado trabalhar com esse tipo de arquivo se vindo de fontes desconhecidas.
"""

import pickle
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def fala(self):
        print(f'{self.nome} ?')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fala(self):
        print(f'{self.nome} mia.')

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fala(self):
        print(f'{self.nome} late.')

cachorro = Cachorro('Juninho')
gato = Gato('Jigglypuff')

# Escrita em arquivos pickle (serialização)
with open('animais.pickle', 'wb') as arq: # esse b no 'wb' indica q será binarizado.
    pickle.dump((cachorro, gato), arq) # Se fosse só um objeto n precisava abir mais um parêntese.

# Lendo arquivos pickle (deserialização)
with open('animais.pickle', 'rb') as arq: # Pega os objetos armazenados no arquivo pickle e insere na linguagem.
    cachorro, gato = pickle.load(arq)
    print(f'O gato chama-se {gato.nome}')
    print(f'Gato é do tipo: {type(gato)}')
    gato.fala()
    print(gato)

    print(f'O cachorro chama-se {cachorro.nome}')
    print(f'O cachorro é do tipo: {type(cachorro)}')
    cachorro.fala()
    print(cachorro)