"""
Funções de Maior Grandeza ou Higher Order Functions (HOF)

O q isso significa?
    - Quando uma linguagem de programação suporta HOF, indica q podemos ter funções q retornam outras funções,
    assim como passar funções como argumento para outras funções e criar variáveis do tipo funções.

Em Python, as funções são cidadões de primeira classe (first class citizen)


# Passando funções como argumento para outra função

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def operacao(a, b, funcao):
    return funcao(a, b)

print(operacao(1, 5, somar))
print(operacao(1, 5, subtrair))
print(operacao(1, 5, multiplicar))
print(operacao(1, 5, dividir))
"""

# Nested Function (Funções Aninhadas)

# Em Python podemos ter funções dentro de funções, são conhecida por Nested Function ou Inner Function (Função Interna)

# EX
from random import choice

def humor(nome):
    def reacao():
        return choice(('Oi ', 'Que bom te ver ', 'Suma da minha frente AGORA '))
    return reacao() + nome

print(humor('Walyson'))



# Retornando funções dentro de outra funções
def piada():
    def risada():
        return choice(('kkkkkkkkkkkkkkk', 'hahahahahah', 'fosh fosh fosh', 'k'))
    return risada # Repare q a função n está sendo chamada (sem os parenteses), mas sim retornada

#print(piada())
ouvindo = piada() # Se n passar para uma variável a função n imprime a risada
print(ouvindo())



# Funções Internas podem acessar o escopo de funções mais externar

def individo(nome):
    def tipo():
        raca = choice(('humano', 'sayajim', 'namekuseijin', 'boo', 'metamorfo'))
        return f'{nome} é da raça {raca}.' # Acessando a função externa tipo(nome).
    return tipo

ser = individo('Pedro')
print(ser())
print(ser())