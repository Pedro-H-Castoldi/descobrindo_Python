"""
O que são módulos?
    Em Phyton, módulos nada mais são do q outros arquivos Python.

Módulo random -> Possui várias funções para geração de números pseudo-aleatórios (que podem se repetir).


# OBS: Existem 2 formas de se utilizar módulo ou função:

# Forma 1 - Importar todo o módulo de uma vez (N RECOMENDADO).
import random

# A função random() é uma das funções do random, ela gera um número real aleatório entre 0 e 1 (o 1 não é incluido mas o 0 sim - >= 0 < 1.
# random()

# Desta forma todas os atributos do módulo random entrarão na memória, deixando o programa mais pesado, se você saber
# qual funções irá utilizar, essa forma n é recomendada.

print(random.random()) # Note q é necessário botar o nome do método e depois da função separando por ponto (.)

# OBS: A função random() é apenas uma das várias funções q estão dentro do pacote random. Não confunda!


# Forma 2 - Importar apenas a função necessária (RECOMENDADO)
from random import random # Do módulo random importe a função random()

for i in range(5):
    print(f'{random():.2f}') # Note q agora n é mais necessário botar o nome do pacote, agora basta colocar o nome direto da função importada.


# Usando a função uniform() - > Gera um número real pseudo-aleatório com valores estabelecidos
from random import uniform
for i in range(5):
    print(uniform(0, 11)) # valores de 0 à 10


# Função randint -> gera número inteiro pseudo-aleatório de valores estabelecidos
from random import randint
for i in range(5):
    print(randint(0, 11))

"""
# choice -> Gera um valor ateatório dentro de um interável
jogada = ['papel', 'pedra', 'tesoura']

from random import choice
print(choice(jogada))

print(choice('Pedro Henrique Castoldi Bezerra'))