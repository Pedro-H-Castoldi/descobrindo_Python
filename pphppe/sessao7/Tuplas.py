"""
Tuplas são bastante parecidas com listas
Elas possuem 2 diferenças básicas:
    1- As tuplas são representadas por parenteses '()'

    2- Elas são imutáveis, ou seja, depois de criada ela n muda. Toda operação em uma tupla gera uma nova tupla.


#CUIDADO 1: Tuplas são representadas por '()'
tupla1 = (2, 6, 3, 0)
print(tupla1)
print(type(tupla1))

tupla2 = 4, 2, 6, 77
print(tupla2)
print(type(tupla2))



#CUIDADO 2: Tuplas com 1 elemento n são reconhecidas como tuplas. É reconhecido como um int (por exemplo)
tupla3 = (3)
print(tupla3)
print(type(tupla3))

# Para ser reconhecida como tuple é necessário colocar uma vírgula dentro dos parenteses
tupla4 = (5,)
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Tuplas são definidas pela vírgula!
(4) -> N é tupla
(4,) -> É tupla
4 -> É tupla


# Tupla com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))


# Desempacotamento
tuplan = ('Pedro', 'Henrique')
print(tuplan)
print(type(tuplan))
primeiron, segundon = tuplan
print(primeiron)
print(segundon)
print(type(primeiron))


# Adição e remoção de elementos em tuplas n existem, dado q elas são imutáveis


# Valor: maior, menor, soma e tamanho em tuplas
tupla = (66, 8, 3, 2, 11, 34, 6)

print(max(tupla))
print(min(tupla))
print(sum(tupla))
print(len(tupla))


# Concatenação de tuplas
tupla1 = (5, 3, 8)
tupla2 = (99, 33, 22)
print(tupla1)
print(tupla2)

print(tupla1 + tupla2) # Imprimiu as 2 juntas
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # N é exatamente modificar, mas sim, sobrescrever
print(tupla1)


# Verificar se determinado elemento está na tupla
tupla = (55, 'i', 7, 44, 12)
print(12 in tupla)


# Interando sobre uma tupla
tupla = (55, 'i', 7, 44, 12)
for n in tupla:
    print(n, end= ' ')

print('\n')

for tupla in enumerate(tupla):
    print(tupla)


# Contando elementos dentro de uma tupla
tupla = (5, 3, 2, 5, 3, 'y')
print(tupla.count(5))


# Convertendo de string para tupla
convertt = tuple("Juninho é um cachorro")
print(convertt)


# Dica de quando utilizar tuplas:
# SEMPRE quando n for necessário modificar uma coleção de elementos
# EX 1:
meses = ('janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Acesso a uma casa
print(meses[8])

# Interar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1


# Verificar em qual indice o elemento está na tupla
print(meses.index('Setembro'))


# Slicing
# Tupla(inicio:fim:passo)
print(meses[0:9])


# Copiando uma tupla
tupla = (1, 2, 3, 4)
nova = tupla # Com tupla n existe o problemade Shallow Copy
print(tupla)
print(nova)

outra = (5, 6, 7)
nova = nova + outra
print(nova)
print(tupla)


# POR QUE USAR TUPLAS?
    # 1 - Tuplas são mais rápidas q listas;
    # 2 - Tuplas deixam seu código mais seguro.
# * Isso pelo fato de se estar trabalhando com elementos inutáveis!
"""
