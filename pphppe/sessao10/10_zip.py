"""
O zip() cria um interável que pega os valores de outros interáveis e os agregam passando eles então como pares.


#EX
l1 = [1, 6, 4]
l2 = [88, 54, 3]

zip1 = zip(l1, l2, 'abc')
print(zip1) # Retorna um zip object
print(type(zip1))

print(list(zip1)) # Note q foi pego cada primeiro elemento das 2 lustas e divididos em pares por meio de tuplas

# usanco dic
zip1 = zip(l1, l2) # Dá erro se botar mais do q 2 interáveis em um zip q será tranformado em dic
print(dict(zip1))


# O zip() prioriza o menor interável, ou seja, se um interável for maior do que outro, o zip encerrará quando o menor interável acabar,
#isso fará com q elementos de interáveis maiores n apareçam.
l3 = [55, 3, 88, 9, 332, 21, 6]
print(list(zip(l1, l2, l3))) # Nem todos os elementos de l3 apareceram, os elementos l1 e l2 apareceram todos pois ambos são do mesmo tamanho.


# Podemos utilizar tipos de interáveis diferentes em um mesmo zip():
l = [5, 7, 8]
t = 11, 89, 'a'
d = {'a' : 1, 'b': 55, 'c': 87}

print(list(zip(l, t, d.values()))) # values() no dic para aparecer os valores, sem isso apareceria as chaves.

# Descompactando *:
tu = ((1, 4), (8, 12), (0, 3))
print(tuple(zip(*tu))) # Cpm o '*' descompactou e formou pares das tuplas q estavam dentro da tupla mãe.
"""

# Aplicação mais complexa:
# Pegar amaior nota de alunos
n1 = [10, 5, 7]
n2 = [8, 8, 10]
alunos = ['Anunciada', 'Ortolangia', 'Eduardo']

dados = {no[0]: max(no[1], no[2]) for no in zip(alunos, n1, n2)}
print(dados)

# Usando map()
dados = zip(alunos, map(lambda nota: max(nota), zip(n1, n2)))
print(list(dados))