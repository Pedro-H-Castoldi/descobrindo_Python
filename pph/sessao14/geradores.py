"""
Geradores
    - Generators (Geradores) são Iterators (iteradores);
    - Todo Generator é um Iterator, mas nem todo Iterator é um Generator.

Mais informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    Generators podem ser criados com expressões geradoras.

DIFERENÇAS ENTRE FUNÇÕES E GENERATOR FUNCTIONS (FUNÇÕES GERADORAS)
------------------------------------------------------------------------------------
/ Funções                              / Generator Functions                       /
------------------------------------------------------------------------------------
/ Utilizam return                     / Utilizam yield                             /
------------------------------------------------------------------------------------
/ Retorna uma unica vez              / Pode usar yield multiplas vezes             /
------------------------------------------------------------------------------------
/ Quando executado retorna 1 valor  / Quando executado retorna um Generator        /
------------------------------------------------------------------------------------


# Utilizando Generator Function
def conta_ate(limite):
    inicio = 1
    while inicio <= limite:
        yield inicio # retorna a variável inicio até o limite estimado, se passar do limite dará um erro.
        inicio += 1

# Uma Generator Function n é um Geenerator, ela gera um Generator
gera = conta_ate(3)
print(next(gera)) # 1
print(next(gera)) # 2
print(next(gera)) # 3
# print(next(gera)) ERROR: StopIteration
"""

# Utilizando Generator Function
def conta_ate(limite):
    inicio = 1
    while inicio <= limite:
        yield inicio # retorna a variável inicio até o limite estimado, se passar do limite dará um erro.
        inicio += 1


gera = conta_ate(3)
print(next(gera)) # 1

print('qqq')

# Tbm pode usar o for
for gg in gera:
    # N precisa usar next() pq o for já insere essa função por debaixo dos panos
    print(gg) # Note q irá ser iniciado o for o com número 2

# Com o Generator é retornado de 1 por 1 os valores, o yield retorna o valor e fica esperando para ser retornado o outro sem sair da função.
#Para retornar todos os valores de uma só vez basta tranformar, por exemplo, para uma lista.
geral = list(conta_ate(10))
print(geral)
