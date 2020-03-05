"""
Decoradores (Decorators)

O q são decorators?
    - Decorators são funções;
    - Decorators envolve outras funções e aprimoram seus comportamentos;
    - Decorators tbm são exemplos de Higher Order Functions;
    - Decorators possuem uma sintaxe própria, usando um '@' (Syntact Sugar / Açúcar Sintático).


# Decorators como função (sem Syntact Sugar, n recomendado)
# Processo de decorar a função
def educado(funcao):
    def sendo_educado():
        print('Olá. Tudo bem?')
        funcao() # Onde chama a função em meio à decoração
        print('Sinta-se à vontade.')
    return sendo_educado()

def saudacao():
    print('Bem-vindo(a) à nossa casa.')

def saudacao_raiva():
    print('SER TERRENO MALDITO!!!')
# Imprimindo a função saudacao sem ser decorada
#saudacao()

# Imprimindo de modo decorada
educado(saudacao)

educado(saudacao_raiva)

"""

# Recorator com Syntact Sugar (recomendado)
def seja_realmente_educado(funcao):
    def educacao():
        print('Olá. Tudo bem?')
        funcao()
        print('É um prazer conhece-lo.')
    return educacao

@seja_realmente_educado
def nome():
    print('Meu nome é Pedro Henrique!') # Tem q ser print, n return aki.

nome() # Basta chamar normalmente a função q logo depois ela será decorada por meio do @

@seja_realmente_educado
def dormir():
    print('Quero dormir.')

dormir()

# OBS: Esse método é usado para acionar outra função antes de acessar a q a gente deseja (analisei e deduzi isso)

# Não confunda Decorator com Decorator Function
    # - @ -> Decorator;
    # - Função q será usada para decorar uma função -> Decorator Function.