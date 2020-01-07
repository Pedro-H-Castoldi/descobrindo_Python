"""
A partir da versão Python3+ a função reduce() n é mais uma função alocada (built-in). Agora é necessário
importar essa função pelo módulo "functools".

Guido Van Rossun: Utiliza reduce() se for realmente necessário. Em todo caso, a maioria das vezes (99%)
um loop for é mais entendível.

- Entendendo reduce():
# Imagine q vc tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]

# E vc recebe uma função q recebe 2 parâmetros:
def func(a, b): # Função q servirá de parâmetro com 2 parâmetros (a e b).
    return a ** b
# Assim como map() e filter(), a função reduce() recebe 2 parâmetros (função e interável).
#No entanto, a função que servirá de parâmetro deverá ter 2 parâmetros, diferentemente de map() e filter() q a função só tem 1 parâmetro

reduce(func, dados)

# A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos 2 primeiros elementos e salvando o resultado;
    Passo 2: res2 = f(res1, a3) # Aplica a função no primeiro resultado e no terceiro elemento do interável;
    Passo n resn = (resn-1, n) # Assim sucessivamente.

# Ou seja, reduce() aplica a função no resultado anterior junto com o dado do interável, assim sucessivamente até o ultimo elemento.
func(func(func(a1, a2), a3), a4), ...), an)

"""
# Funcionando na prática:
from functools import reduce

numeros = [5, 4, 3, 2, 1]

# Precisamos de uma função que receba 2 parâmetros:
mult = lambda a, b: a * b

res = reduce(mult, numeros)
print(res)

# Utilizando loop normal:
res = 1
for i in numeros:
    res = res * i

print(res)

