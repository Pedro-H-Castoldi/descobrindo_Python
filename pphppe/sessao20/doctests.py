"""
Doctests

São testes q colocamos no Docstring das funções/métodos Python,

Para rodar um teste no doctest:
    python -m doctest -v nome_do_modulo.py (mas pode ser executado diretamento do Pycharm, sem precisar executar no terminal)

# Fazendo teste com doctest
def soma(a, b):
    ''' ATENçÂO: as aspas devem ser duplas quando for executar!
    Soma dos numeros a e b
    #>>> soma(1, 2)
    5
    '''
    # tem q ser q nem é mostrado no terminal com '>>>'.
    # Se a soma dos parâmetros a + b == 3, então retorna a soma, senão, retorna dizendo q deu um erro.
    return a + b


# Outro exemplo, aplicando o TDD
def duplicar(valores):
    '''
    Duplicar valores em uma lista
    #>>> duplicar([1, 2, 3])
    [2, 4, 6]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    '''
    #pass # Passo Red do TDD.
    #return [] # 3 erros e 1 passou
    return [2 * elemento for elemento in valores] # Passo Green.

"""

# Erros inesperados

def diga_oi():
    """
    Dizer oi

    >>> diga_oi()
    'Oi'
    """
    # Se o oi for com aspas duplas no doc, irá dá erro, pois está tendo aspas duolas dentro de outas aspas duplas, desse modo,
    # temos q colocar aspas simples lá.
    return "Oi"


def verdade():
    """
    Retorna verdade

    >>> verdade()
    True  
    """
    # Dá erro, pois lá no doc eu coloquei 2 espaços após o True e no retrun eu n os coloquei.
    return True