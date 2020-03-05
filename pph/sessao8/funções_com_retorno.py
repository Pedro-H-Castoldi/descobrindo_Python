"""
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros) # print n retorna nada (None)
print(f'Retorno de print: {ret_pr}')

def quadrado_de_5():
    print(5 * 5)

# N irá retornar nada
ret1 = print(5 * 5)
print(ret1)

ret2 = quadrado_de_5()
print(ret2)

OBS: Em Python quando a função n retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar os valores com a palavra 'return'

def quadrado_de_5():
    return 5 * 5

print(f'Retorno: {quadrado_de_5()}')

# Criando uma variável para receber o retorno da função
ret = quadrado_de_5()
print(f'Retorno: {ret}')


# Com o 'return' é dada mais flexibilidade
def diz_oi():
    return 'Oi '

alguem = 'Pedro H'
print(f'{diz_oi() + alguem}')


OBS: Sobre o 'return'
    1- Ele finaliza a função, ou seja, sai da execução da função;
    2- Podemos ter em uma função diferentes returns;
    3- Podemos em uma função retornar qualquer tipo de dado, inclusive multiplos valores.

# EX 1 da OBS
def diz_oi():
    print('Estou sendo executado antes do return!')
    return 'Oi '
    print('Nunca serei executado, já que estou depois do return..')

print(diz_oi())


# EX 2 da OBS
def ocasiao():
    variavel = True
    if variavel:
        return 10
    elif variavel is None:
        return -1
    return -10 # Essa é a parte do else, só q ele é desnecessário, já q se n for True e nem None ele logo percorrerá até o return -10..

print(ocasiao())


# EX 3 da OBS
def numeros():
    return 3, 4, 5, 6 # É uma tupla já q está sendo separada por vírgulas (se quisesse lista, tinha q botar [])

n1, n2, n3, n4 = numeros() # Passando um valor para cada variável de acordo com a ordem
print(n1, n2, n3, n4)

print(numeros())
print(type(numeros()))



# Jogo do cara ou coroa
from random import random # números aleatórios entre 0 e 1
def cara_ou_coroa():
    if random() > 0.5:
        return 'Coroa'
    return 'Cara'

print(cara_ou_coroa())



# Erro comum, que na verdade nem é erro, mas sim, codificação desnecessária
def impar_par():
    n = 5
    if n%2 =! 0:
        return 'Impar'
    else:              # 'else' desnecessário! O modo pythonico seria colocar logo o return 'Par'
        return 'Par'


"""

