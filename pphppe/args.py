"""
Entendendo o *args
    - O *args é um parâmetro como qualquer outro. Isso quer dizer q poderá chama-lo de qualquer coisa, desde q comece com o asterisco (*).
    No entanto o chamamos de *args como padrão.
        EX:
            *exemplo # O recomendado é apenas chama-lo de *args

Mas o q é o *args?
    O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
    Então desde já lembre-se que tuplas são imutáveis.

Exemplos:

def soma(n1= 2, n2= 4, n3= 5):
    return n1 + n2 + n3

print(soma(1, 4, 6)) # N dará erro. mesmo se botar menos de 3 argumentos
print(soma(1, 44, 5, 90)) # Irá dá erro, pois só existe espaço para 3 argumentos. O *args irá tratar disso



# Utilizando o *args
def soma(*args): # O asterisco só precisa está na parte q anuncia o parâmetro. Podemos utilizar mais parâmetros na função junto com o *args sem problema
    return sum(args) # Como o args é uma tupla, para se fazer a soma, basta utilizar o 'sum'

print(soma(1, 3)) # É possível colocaro infinitos argumentos (desde q sejam compatíveis com a função, como é uma soma o argumento precisa ser um número)
print(soma(5, 4, 5, 6,))
print(soma(4, 6, 7, 4.4, 33))


# Outra utilização
def reconhecimento(*args):
    if 'Pedro' in args and 'Henrique' in args:
        return 'Seja bem-vindo Pp!'
    return 'Olá. Você não é o Pedro.'

print(reconhecimento('Bezerra', 4, 4.44))
print(reconhecimento('Universo', 'Plano Terreno', 43, 'Pedro'))
print(reconhecimento(44, 1,2, 'Henrique', 'Pedro')) # Esse entrará no if, pois o mesmo possui os nome 'Pedro' e 'Henrique'



# E se o argumento for um conjunto de números como uma lista, tupla, etc?
#Para resolver isso colocamos o asterisco tbm no argumento para fazer o desempacotamento desses números
def multiplica(*args):
    n = 1
    for i, _ in enumerate(args):
        n = args[i] * n
    return n

numeros = [5, 7, 2, 9]

print(multiplica(2, 2, 2))
print(multiplica(numeros)) # N funcionará
print(multiplica(*numeros)) # Desse modo funcionará, pois o conjunto de valores irá ser desempacotado por conta do '*'
"""

def multiplica(*args):
    n = 1
    for i, _ in enumerate(args):
        n = args[i] * n
    return n

numeros = [5, 7, 2, 9]