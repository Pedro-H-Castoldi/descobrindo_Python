"""
Metadados -> São dados intrisicos em arquivos (um exemplo: as propriedades de um arquivo como tamanho, data de modificação, criação etc);

Wraps -> São funções q envolvem elementos com diversas finalidades.


# Problema
def ver_log(fun):
    def logar(*args, **kwargs):
        #Sou uma função dentro de outra....
        print(f'Você está chamando a função: {fun.__name__}')
        print(f'A Codumentação da função: {fun.__doc__}')
        return f'Resultado da soma: {fun(*args, **kwargs)}'
    return logar

@ver_log
def soma(*args):
    #A função soma tem o objetivo de somar números...
    return sum(args)

print(soma(1, 4))

# Esse é o problema. Quando vai pedir os dados de uma função q foi decorada, será mostrado os dados da função decoradora.
print(f'Nome da função: {soma.__name__}')
print(f'Documentação: {soma.__doc__}')
"""

# RESOLVENDO O PROBLEMA
from functools import wraps # É aki q entra o wraps()

def ver_log(fun):
    @wraps(fun) # Para resolver o problema basta importar o wraps() e coloca-lo como decorator na função decoradora
    #com a função ao qual se deseja decorar como parâmetro
    def logar(*args, **kwargs):
        """Sou uma função dentro de outra...."""
        print(f'Você está chamando a função: {fun.__name__}')
        print(f'A Codumentação da função: {fun.__doc__}')
        return f'Resultado da soma: {fun(*args, **kwargs)}'
    return logar

@ver_log
def soma(*args):
    """A função soma tem o objetivo de somar números.."""
    return sum(args)

print(soma(1, 4))

# Esse é o problema. Quando vai pedir os dados de uma função q foi decorada, será mostrado os dados da função decoradora.
print(f'Nome da função: {soma.__name__}')
print(f'Documentação: {soma.__doc__}')