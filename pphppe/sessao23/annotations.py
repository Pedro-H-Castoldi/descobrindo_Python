"""
annotation -> Serve para indicar o tipo das variáveis presentes no nosso programa.

def dizer_oi(nome: str) -> str:
    return f'Oi. Meu nome é {nome}'

print(dizer_oi('Pedro'))

print(dizer_oi.__annotations__) # {'nome': <class 'str'>, 'return': <class 'str'>}, nome q retorna o o tipo do parâmetro e o tipo do retorno.

n1: int = 1

nome: str = 'Luiza'

verdade: bool = True

valor: float = 5.8

print(__annotations__) # Retorna os tipos de todas as variáveis do escopo pertencente a esse printe.


# Annotations em classes

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None: # None pq n retorna nada
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa('Pedro Henrique', 23, 83)

print(p.__dict__)

#print(p.__annotations__) # N tem annotation
print(p.andar.__annotations__)
print(p.__init__.__annotations__)


# Comentários com annotations
import math

def circuferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circuferencia(1))
#print(circuferencia('dois'))

# Com mais de um parâmetro
def nome_bool(nome, analisa=True):
    # type: (str, bool) -> str
    if analisa:
        return f'{nome} é verdadeiro.'
    return f'{nome} é falso'

print(nome_bool('Jigglypuff'))
#print(nome_bool('Renzo', 22))

# Modo 2 (n recomendado)
def nome_bool2(
        nome, # type: str
        analisa=True # type: bool
): # type: (...) -> str
    if analisa:
        return f'{nome} é verdadeiro.'
    return f'{nome} é falso'

print(nome_bool2('Juninho'))
#print(nome_bool2(33, 'aa'))

"""

# Especificando os tipos dos elementos dos iteráveis
from typing import Dict, List, Set, Tuple
nomes: List[str] = ['Juninho', 'Zanolha']

versoes: Tuple[int, int, int] = (1, 2, 3)

opcoes: Dict[str, bool] = {'ar': True, 'bancos_couro': False}

valores: Set[int] = {2, 6, 4}

print(__annotations__)