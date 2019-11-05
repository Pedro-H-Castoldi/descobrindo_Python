"""
Docstrings é uma documentação do que a função faz. Isso por meio de textos como esse q vc está lendo.
Para acessar o Docstring é necessário utilizar o terminal e usar as ferramentas:
    - help (aparece as informações mais claramente, mas n reconhece acentos, etc)
    - __doc__ (a desvantagem é q n possui quebra de linha, a vangatem é q reconhece acentos, etc)
"""

def diz_oi():
    """ Função que diz oi""" # Docstring
    return 'OI!'


def soma(n1, n2):
    """
    Faz uma soma
    :param n1: Pega um argumento como parâmetro como o primeiro número
    :param n2: Pega um argumento como parâmetro como o segundo número
    :return: Retorna a soma do n1 com o n2
    """
    return n1 + n2
