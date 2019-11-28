"""
É utilizado o try/except para tratar erros no código. Previnido assim do programa parar de funcionar e
o usuário receba uma mensagem de erro inesperada.

Forma mais geral de usar:
try:
    //execução da problematica.
except:
    //o q deve ser feito em caso de problema.


# EX 1 - Tratando erro de forma genérica:
try:
    menu() # Tenta executar a função menu()
except:
    print('Algo deu errado..') # Se caso dé errado imprima essa mensagem


# EX 2 - Tratando erro de forma específica:
try:
    menu()
except NameError:
    print('Você está tentando usar uma função inexistente.')

try:
    len(5)
except NameError: # O erro irá estourar, pois o erro q está sendo tratado aki é o NameError, e o erro q está acontecendo é o TypeError.
    print('Você está tentando utilizanr uma função inexistente')


# EX 3 - Tratando erro de forma específica com detalhes do erro:
try:
    len(5)
except TypeError as err: # O erro irá estourar, pois o erro q está sendo tratado aki é o NameError, e o erro q está acontecendo é o TypeError.
    print(f'A aplicação gerou o seguinte erro: {err}')


#EX 4 - Especificando varios erros e deixando um genérico:
try:
    print('ph'[12])
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err:
    print(f'Deu TypeError: {err}')
except:
    print('Ouve um erro na aplicação.')

OBS: É SEMPRE recomendado tratar dos erros de forma específica!
"""

# EX 5 - Tratando de erro dentro da função:
def dic(dic, key):
    try:
        return dic[key]
    except KeyError:
        return 'Deu erro na chave.'
    except NameError:
        return 'Deu erro no dic'
    except:
        return 'Algo deu errado.'

nomes = {'Juninho': 'cachorro'}


print(dic(nomes, 'Jigglypuff')) # Erro na chave