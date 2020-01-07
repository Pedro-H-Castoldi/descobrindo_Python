"""
raise-> Lança exceções

OBS: O raise n é uma fução, é uma palavra reservada assim como, def, None, True.

Com o raise podemos criar nossas próprias mensagens de erro.

- Forma de usar:
    raise tipoDoErro('Mensagem de erro')

EX:
    def imprimecor(tex, color):
    if type(tex) is not str:
        raise TypeError('Erro. O texto deve ser uma string')
    if type(color) is not str:
        raise TypeError('Erro. a cor deve ser uma string.')
    print(f'O texto "{tex}" será impresso em {color}.')

    imprimecor('ee', 4)

OBS:
    Assim como o return o raise finaliza a função.
"""

# EX:
def imprimecor(tex, color):
    color = color.lower()
    cores = ('azul', 'verde', 'amarelo', 'branco', 'vermelho', 'preto', 'rosa')

    if type(tex) is not str:
        raise TypeError('Erro. O texto deve ser uma string')

    if type(color) is not str:
        raise TypeError('Erro. a cor deve ser uma string.')

    if color not in cores:
        raise ValueError('Cor inválida.')

    print(f'O texto "{tex}" será impresso em {color}.')

imprimecor('ee', 'roxo')