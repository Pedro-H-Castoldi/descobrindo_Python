"""
# Relembrand

def gritar(fun):
    def gritando(*args, **kwargs): # Utilizamos *args e *kwargs para podermos inserir quantos argumentos quisermos (kwargs funciona só com parametros nomeados).
        return fun(*args, **kwargs).upper()
    return gritando

@gritar
def nome(nome):
    return f'Meu nome é {nome}'
@gritar
def comprimentar(estado):
    return f'Olá tudo ok? Eu estou {estado}.'
@gritar
def olhar(coisa):
    return f'Olha o {coisa}'

@gritar
def nomes_4(nome1, nome2, nome3, nome4):
    return f'Senhore(a)s: {nome1}, {nome2} dirijam-se para direita. {nome3} e {nome4}, por gentileza, os senhore(a)s digijan-se para esquerda.'

print(nome('Pedro'))
print(comprimentar('ótimo'))
print(olhar('Sasuke'))
print(nomes_4('Henrique', 'Ana', 'Jessica', nome4='Hilder')) # Na parte de nomeação de parametro se está usando o **kwargs
"""

# Decorators com argumentos
def validacao_do_decorator(valor):
    def interna(fun):
       def dados_pegos_da_fun(*args, **kwargs):
           if args and args[0] != valor: # Se o primeiro valor pego da fun por diferente do argumento valor da função validacao_do_decorator(valor)
               return f'Valor inválido! O primeiro valor deve ser {valor}.'
           return fun(*args, **kwargs) # Senão, executa a função fun.
       return dados_pegos_da_fun
    return interna


@validacao_do_decorator('sushi')
def melhores_comidas(*args):
    return f'Delícia. Chega a manteiga derrete: {args}'

print(melhores_comidas('Receita de tia Rosa', 'sushi', 'camarão')) # Erro pois o primeiro valor n é 'sushi'
print(melhores_comidas('sushi', 'camarão', 'receita de tia Rosa'))