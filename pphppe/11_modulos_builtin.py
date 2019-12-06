"""
Trabalhando com módulos builtin

Quando o Python inicia, o mesmo carrega só o que está na linguagem nativa, como for, builtins como sum, max, etc.
Ele não carrega os módulos, para o Python carregá-los, é necessário importa-los.


# Utilizando apelicos (alias) para os módulos
import random as ran
print(ran.random())


# Importando todas as funções do módulo de uma vez, com a vantagem de quando for chamar a função n precisar colocar o nome do pacote
from random import *
print(uniform(0, 6))


# Utilizando apelidos (alias) para as funções
from random import randint as rint, choice as cho
print(rint(0, 11))

p = ['Sindel', 'Terminator', 'Nightwolf', 'Shang Tsung']
print(cho(p))
"""

# Quando se tem muitas funções importadas, é recomendado que as coloquem em uma tuple
from random import (
    random,
    randint,
    shuffle,
    choice,
    uniform
)

n = [1, 3, 5, 0]

print(choice(n))
print(random())
print(randint(0, 6))
print(uniform(0, 6))
shuffle(n)
print(*n)