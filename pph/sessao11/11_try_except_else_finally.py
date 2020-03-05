"""
Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!!!

OBS: A função do usuário é destruir o sistema.


# else - É executado somente quando o erro não ocorrer.
n = 0 # com o else não dará o NameError, atribuir um valor à n no começo se tornou optativo.

try:
    n = int(input('Digite um número inteiro: '))
except ValueError:
    print('Valor errado')
else:
    print(f'Você digitou {n}') # Essa mensagem só será exibida se não ocorrer o erro.


# Finally - SEMPRE é executado, tendo erro ou não.
try:
    n = int(input('Digite um número inteiro: '))
except ValueError:
    print('Erro no valor inserido.')
else:
    print(f'Você digitou o número {n}.')
finally:
    print('Processo encerrado.')

# OBS: O finally é utilizado geralmente para fechar ou desalocar recursos


# EX mais complexo (ERRADO)
def multi(a, b):
    return f'RESULTADO: {a * b}'

try:
    na = int(input('Digite o primeiro número: '))
except ValueError:
    print('Erro no valor.')

try:
    nb = int(input('Digite o segundo número: '))
except ValueError:
    print('Erro no valor.')
else:
    print(multi(na, nb))

# EX mais complexo (CORRETO):
# O programador é responsável pelas entradas da sua função, então o mesmo deve trata-las.


def divisao(a, b):
    try: # Tratando erro dentro da função
        return f'{int(a) / int(b):.2f}' # Convertendo do string para int
    except ValueError:
        return 'Valor inserido inválido.'
    except ZeroDivisionError:
        return 'Não é possível dividir um número por zero.'


na = input('Digite um número: ') # Note q as entradas fora da função não tem um tipo definido. Isso é definido dentro da função.
nb = input('Digite um número: ')

print(divisao(na, nb))

"""

# EX complexo de forma SEMI-GENERICA
def divisao(a, b):
    try:
        return f'{int(a) / int(b) :.2f}'
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um erro.'

na = input('Digite um número: ')
nb = input('Digite um número: ')

print(divisao(na, nb))