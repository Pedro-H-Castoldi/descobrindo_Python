"""
JSON e Pickle

JSON -> JavaScript Object Notation.

API -> São meios de comunicação entre os serviços oferecidos por empresas (Facebook, Twitter, YouTube, etc), e terceiros (nós programadores).


import json

pro = json.dumps(['produto', {'Ventilador': ('Eletrodoméstico', 'bivolt', 280)}])

print(type(pro))
print(pro) # Note q ele mudou as aspas simples para aspas duplas automaticamente para deixar tudo compativel com o JSON.


class Gato:

    def __init__(self, nome, raca, idade):
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca
    @property
    def idade(self):
        return self.__idade

zanolha = Gato('Zanolha', 'Pirica', 2)

print(zanolha.__dict__)

ret = json.dumps(zanolha.__dict__)
print(ret)


# Integrando o JSON com o Pickle
import jsonpickle

class Gato:

    def __init__(self, nome, raca, idade):
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca
    @property
    def idade(self):
        return self.__idade

zanolha = Gato('Zanolha', 'Pirica', 2)

#ret = jsonpickle.encode(zanolha)
#print(ret) # Desse modo fica mais bem estruturado, mostrando q é um objeto.

# Escrevendo um arquivo json/pickle

with open('gato.json', 'w', encoding='UTF-8') as arq:
    ret = jsonpickle.encode(zanolha) # encode -> Para inserir dados em um arquivo
    arq.write(ret)

"""

# Integrando o JSON com o Pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca, idade):
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca
    @property
    def idade(self):
        return self.__idade


# Lendo um arquivo json/pickle

with open('gato.json', 'r', encoding='UTF-8') as arq:
    dados = arq.read()
    ret = jsonpickle.decode(dados) # decode -> Pegar dados do arquivos lidos e passar para uma variável
    print(ret) # Traz o objeto
    print(type(ret)) # Tipo class Gato
    print(ret.nome)
    print(ret.raca)
    print(ret.idade)