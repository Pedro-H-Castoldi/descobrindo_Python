"""
Funções onde a passagem de parâmetros é opicional
    - EX de uma função onde a passagem de parâmetro é opicional:
        print('Juninho é um cachorrinho')
        print() # N foi atribuido nenhum parâmetro e mesmo assim não gerou nenhum tipo de erro.

    - EX de função onde a passagem de parâmetro é obrigatória:
        def exponencial(n, p):
            return n ** p

        print(exponencial(3, 3))
        print(exponencial()) # Erro ocasionado pela falta do parâmetro obrigatório


# Parâmetro opicional
# Com com parâmetro e = 2 o mesmo ficará opicional, desse modo n precisa botar nenhum argumento quando for chamar a função.
# Isso tbm serve para o n. Para ambos ficarem opicionais basta: 'def elevacao(n=3, e=2)'
def elevacao( n, e=2):
    return  n ** e

print(elevacao(2))
print(elevacao(2, 10)) # Colocando o argumento 10 o parâmetro 'e' irá recebe-lo, logo irá ser feita a operação com o 10 e n mais com o 2

#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração
# MODO ERRADO
# def ex(nu=2, exp):
#    return nu ** exp

#print(ex(5)) # Irá dá erro pois o argumento 5 estará indo para o parâmetro nu e n pro exp

# MODO CORRETO
def ex(exp, nu=2): # Veja q agora o parâmetro q n é default está vindo primeiro
    return nu ** exp

print(ex(5)) # O argumento 5 dessa forma estará indo para o parâmetro exp


# Função com ambos os parâmetros default
def soama(nu1=8, nu2=9):
    return nu1 + nu2

print(soama(5, 9))
print(soama(2))
print(soama())
print(soama(nu2=7)) # Isso faz com q o argumento 7 vá para o 'nu2' sem precisar botar o primeiro argumento antes



def ola(nome='Pedro Henrique', gostoso=False):
    if nome == 'Pedro Henrique' and gostoso:
        return 'Olá PH gostosão e fodão!'
    elif nome == 'Pedro Henrique' and gostoso == False:
        return 'Você não é o PH Castoldi então.'
    return f'Olá {nome}..'

print(ola())
print(ola(gostoso= True))
print(ola('Guervisionson'))
print(ola(True))

# Por que usar funções com parâmetros default?
    - Nos permite ser mais flexíveis nas funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de códigos.

OBS: Podemos usar qualquer tipo de dados (até mesmo funções) em funções default.



# Utilizando outras funções como argumento para o parâmetro default de uma função

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def funfun(num1, num2, fun=soma):
    return fun(num1, num2)

print(funfun(2, 2, subtracao)) # Irá chamar a função 'subtracao'
print(funfun(3, 3)) # Irá chamar a função 'soma'
print(funfun(4, 4, multiplicacao)) # Irá chamar a função 'multiplicacao'



# Escopo - Evitar problemas e confusão:
nome = 'Pedro' # Variável global

def oi():
    nome = 'Juninho' # Variável local
    return f'Oi {nome}' # Irá trocar o nome Predo por Juninho

print(oi())

# As variáveis locais possuem prioridade sobre as globais



# Variáveis locais só trabaham dentro do local onde estão inseridas, como por exemplo, nas funções
def eae():
    cachorro = 'Juninho'
    return f'Eae {cachorro}'

print(eae())
print(cachorro) # Dará um erro pois essa variável n existe fora da função



# Se declarar uma variável global e utiliza-la dentro da função (usando ela como incremento dela mesma) não irá funcionar
total = 0

#def incre():
#    total+= 1 # irá dá erro pois ela não foi declarada dentro da função (a variável total n possui nenhum tipo de valor)
#    return total


#print(incre())

# Solução para isso
def incre():
    global total # Desse modo indicará q a variável é global e está pegando o valor q a foi adicionada na declaração (o zero)
    total+= 1
    return total

print(incre())
"""

# Podemos ter funções q são declaradas dentro de outras funções e tbm existe uma forma de escopo de variável
def fora():
    contador = 0

    def dentro(): # Função dentro de outra função
        nonlocal contador # Declarando q n é uma função local, mas tbm ela n é global. Isso é utilizado quando uma função dentro de outra pega uma variável
        contador+= 1
        return contador
    return dentro()

print(fora())