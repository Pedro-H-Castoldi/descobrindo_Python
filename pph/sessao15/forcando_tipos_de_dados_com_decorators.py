"""
Relembrando da função zip:
    - a = [1, 2, 3]
    - b = [4, 5, 6]
    - c = zip(a, b)
O valor de c será:
    (1,4), (2, 5), (3, 6)
"""

def forca_tipo(*tipos):
    def decorator_f(fun):
        def converte(*args, **kwargs):
            novo_tipo = []
            for (valor, tipo) in zip(args, tipos):
                novo_tipo.append(tipo(valor)) # str('Boruto). No outro ciclo: int(1)
            return fun(*novo_tipo, **kwargs) # Insere o novo dado gerado com as conversões
        return converte
    return decorator_f

@forca_tipo(str, int) # Esses serão os tipos q serão forçados
def vezes(nome, repeticao):
    for n in range(repeticao):
        print(nome)

vezes('Boruto', '5')

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir('6', 2)