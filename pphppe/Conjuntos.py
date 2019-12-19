"""
Conjuntos em qualquer linguagem de programação faz referência a teoria da matemática.
- Em Python os conjuntos são chamados de 'Sets'.

Dito isso, na mesma forma q na Matemática:
    - Sets (conjuntos) n possuem valores duplicados;
    - Sets n possuem valores ordenados;
    - Elementos n são acessados via indice, ou seja, conjuntos n são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas n nos importamos com a ordenação deles.
Quando n precisamos se preocupar com chaves, valores e itens duplicados.

Os Sets são referênciados em Python por '{}'
Diferenças entre conjuntos (sets) e mapas (dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.


# Declarando um conjunto (Os números repetidos serão ignorados, os números serão ordenados de um modo q o set desejar).
# Forma 1
conjunto = set({1, 2, 3, 3, 4, 5, 6, 6, 2, 7}) # Os números repetidos serão ignorados
print(conjunto)
print(type(conjunto))

# Forma 2 - Mais comum
conjunto = {2, 1, 2, 2, 3, 4, 3, 4, 5, 0}
print(conjunto)
print(type(conjunto))

if 3 in conjunto:
    print('Tem o 3!')
else:
    print('Não tem o 3..')


# Sets n possuiem uma ordem, além de ignorar valores repetidos
# Irá ter 7 elementos pois lista aceita valores repetidos
lista = [4, 2, 3, 3, 5, 4, 1]
print(f'Lista: {lista} com {len(lista)}')

# Irá ter 7 elementos pois tupla aceita valores repetidos
tupla = (4, 2, 3, 3, 5, 4, 1)
print(f'Tupla: {tupla} com {len(tupla)}')

# Irá ter 5 elementos pois dicionário n aceita chaves repetidas
dicionário = {}.fromkeys([4, 2, 3, 3, 5, 4, 1], 'valor')
print(f'Dicionário: {dicionário} com {len(dicionário)}')

# Irá ter 5 elementos pois set n aceita valores repetidos
set = {4, 2, 3, 3, 5, 4, 1}
print(f'Set: {set} com {len(set)}')


# Sets aceitam qualquer tipo de valores
set = {5, 3.3, True, (6,)}
print(set)
print(type(set))

# Podemos interar em um set normalmente
for i in set:
    print(i)


# Uso interesante de sets
# Imagine q em um evento se quer saber o número de pessoas q compareceram e informe as cidades dessas pessoas
publico = ['São Paulo', 'Cedro', 'Fortaleza', 'Campinas', 'Campinas', 'Cedro', 'Cedro', 'Cedro']
print(publico)
print(f'No evento compareceram {len(publico)} pessoas.')

# Agora se quer saber de quantas cidades diferentes o público veio
cidade = set(publico)
print(cidade)
print(f'Veio pessoas de {len(cidade)} cidades diferentes.')



# Adicionar valores ao set
# eles são mutáveis
set.add(22)
set.add(2) # Note q o número 2 n será adicionado, já q o mesmo seria um valor repetido no conjunto

print(set)



# Remover valores (n é indice, é necessário informar o valor q será retirado, tbm n retorna os valores removidos)
# Forma 1 - Se pedir para remover um valor n existente, uma mensagem de erro aparecerá
set.remove(8)
#set.remove(33) # Erro
print(set)

# Forma 2 - Se pedir pra remover um valor n existente, nada irá acontecer (n aparece a mensagem de erro)
set.discard(2)
set.discard(44) # N interrompe o a execução
print(set)


# Copiando conjuntos
#Forma 1 - Deep Copy
novo.txt = set.copy()
novo.txt.add(19)

print(set)
print(novo.txt) # A ordem muda mas os elementos são os mesmos

# Forma 2 - Shallow Copy
novo.txt = set
novo.txt.add(111)

print(set)
print(novo.txt)


# Remover todos os valores do conjunto
set.clear()
print(set)



# Métodos Matemáticos
# Imagine q existem dois cursos, um de Python e outro de Java. Deseja-se unir os conjuntos e então obter
#os nomes dos estudantes de cada curso em um só conjunto, sendo q alunos q fazem um curso tbm podem fazer o outro.
estudantes_Python = {'Pedro', 'Marcos', 'Mária', 'Pierre', 'Anastácia'}
estudantes_Java = {'Anastácia', 'Garcia', 'Mária', 'Pedro', 'Pierre', 'Bartholomeu'}

# Unir conjuntos
# Forma 1
estudantes1 = estudantes_Python.union(estudantes_Java) # Tanto faz a ordem dos nomes
print(estudantes1)

# Forma 2 - Utiliza-se '|'
estudantes2 = estudantes_Java | estudantes_Python
print(estudantes2)


# Obter os alunos q estão em ambos os cursos
# Forma 1
ambos1 = estudantes_Python.intersection(estudantes_Java)
print(ambos1)

# Forma 2 - Utiliza-se '&'
ambos2 = estudantes_Java & estudantes_Python
print(ambos2)


# Alunos q só estão presentes em apenas 1 dos cursos
só_Python = estudantes_Python.difference(estudantes_Java)
print(só_Python)

só_Java = estudantes_Java.difference(estudantes_Python)
print(só_Java)
"""

set = {5, 8, 2, 1}

# Maior valor, menor valor, soma dos valores e tamanho do conjunto
print(max(set))
print(min(set))
print(sum(set))
print(len(set))