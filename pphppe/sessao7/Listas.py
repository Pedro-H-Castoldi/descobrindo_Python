"""
Listas em Python são representadas por [];
É possivel acrescentar elementos nas listas até onde a memória suportar!
as listas são multáveis
As listas podem possuir elementos de vários tipos dentro de uma só lista (int, bool, string, até mesmo outras listas, etc).

if 8 in lista5:
    print('Número 8 encontrado!')
else:
    print('Número não encontrado..')

#Podemos ordenar a lista
print(f'Antes da ordenação:\n {lista1}\n')
lista1.sort()
print(f'Após a ordenação:\n {lista1}')

print(lista1.count(23))
print(lista6.count('e'))

#Adicionar elementos a lista com a função 'append'. OBS: Só é possível adicionar 1 elemento por vez
print(f'Antes de adicionar:\n{lista1}\n')
lista1.append(24)
lista1.append(5)
print(f'Apóos adicionar:\n{lista1}')

#Lista dentro de outra lista como elemento únuco (sublista)
lista1.append([1, 5, 3])
print(lista1)

#Mesmo sendo outra lista, os elementos são reconhecidos como da 'lista1' já que os mesmos estão dentro dela.
if [1, 5, 3] in lista1: #Só encontrará com conjunto citado..
    print('Números encontrados.')
else:
    print('Números não encontrados.')

#Coloca daca elemento da lista como valor adicional a lista. N aceita só 1 elemento, para isso usa-se o 'append'
lista1.extend([9, 6, 3])
print(lista1)

#Inserir um valor em uma certa casa (não substitui o valor q a pertencia, mas sim a desloca para direita).
lista1.insert(3, 'Qualquer Tipo')
print(lista1)

#Adicionar uma lista a outa
#Modo 1
lista7 = lista1 + lista6

#Modo 2
lista1.extend(lista6)

print(lista7)
print(lista1)

#Inverter a sequência das listas
#EX 1
#lista6.reverse()

#EX 2
print(lista6[::-1])

print(lista6)

# Copiar lista para outra
lista6 = lista1.copy()
print(lista6)

# Quantos elementos dentro da lista
print(len(lista4))

# Podemos retirar elementos da lista com 'pop()', e especificar em qual casa retirar. EX: pop(4) vai retirar na casa 4
# OBS: o 'pop()' n somente retira o elemento como tbm o retorna
print(lista6)
lista6.pop() # Irá retiar o último elemento
print(lista6)

# Irá retirar o elemento da casa 7. OBS: Os elementos á direita deste indice serão deslocados para a esquerda.
# Mesmo eliminando o elemento da casa, outro irá para ela indo a esquerda o quanto puder.
# quando n houver mais a casa e pedir para retirar o elemento pertecendo-a, uma mensagem de erro aparecerá.
lista6.pop(7)
print(lista6)


# Podemos limpar por completo uma lista  com o 'clear()'
print(lista6)
lista6.clear()
print(lista6)

# Podemos multiplicar as listas, basta multiplica-las pelas vezes q desejar
lista1 = lista1 * 3
print(lista1)


# Podemos tranformar strings em listas com o 'split()'. O mesmo separa os elementos quando houver espaço por padrão
distrito = 'Várzea da Conceição'
print(f'Antes de virar uma lista:\n{distrito}')
distrito = distrito.split()
print(f'Após virar uma lista:\n{distrito}')

# Caso a string for separada por virgulas, etc é necessário especificar o requisito de separação. EX: split(',')
distrito = 'Várzea,da,Conceição'
print(f'Antes:\n{distrito}')
distrito = distrito.split(',')
print(f'Depois:\n{distrito}')


# Tranformar uma lista em uma string
listac = ['Juninho', 'Chato', 'Fofinho']
print(listac)

# Abaixo está dizendo: Pega a lista (listac), coloca ela em uma string 'cachorro' com a requisição de espçamento ' '.
cachorro = ' '.join(listac)
print(cachorro)

# Colocando '-' como requisição de espaçamento
cachorro = '-'.join(listac)
print(cachorro)


# Podemos colocar qualquer tipo de elemento dentro da lista
listavariada = [4, 'oi', 55.4, True, [4, 9, 'sou uma lista dentro de outra lista'], 54356433235]
print(listavariada)


# Interando listas
# EX 1 - FOR:
for lista1 in lista1:
    print(lista1, end= ' ')
print('\n')

# EX 2 - WHILE
trem = []
carga = ''
while carga != 'sair':
    carga = input('Digite o que deseja colocar na carga ou digite "sair" para sair: ')
    if carga != 'sair':
        trem.append(carga)
for trem in trem:
    print(trem, end= ' ')


# Utilizando variaveis em uma lista
num1 = 5
num2 = 12
nome = 'Luiza'
soma = num1 + num2

listatop = [num1, num2, nome, soma]
print(listatop, end= ' ')


# Acessar diretamente a um elemento
#             0         1         2        3
listaBR = ['Verde', 'Amarelo', 'azul', 'Branco']
print(listaBR[0]) # Verde
print(listaBR[2]) # Azul
# Brando, pois a lista é como um circulo, ou seja, antrs do 0 vem o 3, no caso, -1 (assim sucessivamente: -2, -3)
print(listaBR[-1]) # Branco

# Acrescentando por variavel contadora
cont = 0
while cont < len(listaBR):
    print(listaBR[cont])
    cont += 1

# Mostrando a numeração das casas junto com os elementos
for n, cor in enumerate(listaBR):
    print(n, cor)


# Listas aceitam repetição
listaRep = []
listaRep.append(3)
listaRep.append(3)
listaRep.append(3)

print(listaRep)


# Métodos n tão importantes mas úteis
# Encontrar em qual casa está um elemento
print(lista1.index(34)) # em qual casa está o valor 34? R: 4.

# OBS: Se o numero n estiver em nenhuma casa uma mensagem de erro aparecerá

# Range procurando casa, indicando de onde começar a procurar e até aonde
print(lista1.index(1, 1)) # Procurar valor 1 apartir da casa 1
print(lista1.index(756, 2, 4)) # Procure o valor 756 começando da casa 2 até a casa 4


# Trabalhando com slice de lista
#EX: lista[inicio:fim:passo:]

print(lista1[1:]) # Começando da casa 1 até o final (já q n foi especificado o fim e passo)
print(lista1[:4]) # Começando da casa 0 até a casa 4
print(lista1[::2]) # Começando da casa 0 até a casa o fim de 2 em 2

print(lista1[1:3]) # Começando da casa 1 até a casa 3-1
print(lista1[0:5:2]) # Começando da casa 0 até a 5 pulando de 2 em 2
print(lista1[5::-2]) # Começando da casa 5 indo até o início de 2 em 2 (pois o número negativo volta)


# Mudar elementos de uma casa para outra
nome = ['Pedro', 'Henrique']
print(nome)
nome[0], nome[1] = nome[1], nome[0]
print(nome)

#nome.reverse() Forma mais Pythonica


# Saber valor: maior, menor, soma, e o tamanho da lista
# OBS: Só funciona em valores inteiros ou reais
print(max(lista1)) # Maior
print(min(lista1)) # Menor
print(sum(lista1)) # Soma
print(len(lista1)) # Tamanho



# Transformar Lista em Tupla
print(lista1)
print(type(lista1))

tupla = tuple(lista1)
print(tupla)
print(type(tupla))


# Desempacotamento de listas.
# OBS: Para fazer isso o número de variáveis precisa ser igual ao número de elementos, e ao contrário.
num1, num2, num3, num4, num5, num6 = lista1
print(num1)
print(num2)
print(num3)


# Copiar uma lista para outra.
# EX 1 Deep Copy ou Cópia Profunda (A lista original n sofrerá alterações da nova lista).
print(lista1)
listaNEW = lista1.copy()
print(listaNEW)
listaNEW.append(5)

print(f'Original: {lista1}')
print(f'Nova já modificada: {listaNEW}')

# EX 2 Shallow Copy (A lista original sofre alteração junto com a nova
print(lista4)
listaNEW2 = lista4
print(listaNEW2)
listaNEW2.append('C')
print(f'Original sofre alteração: {lista4}')
print(f'Nova já alterada: {listaNEW2}')
"""
type([])

lista1 = [3, 23, 756, 1, 34, 23]

lista4 = ['P', 'e', 'd', 'r', 'o', ' ', 'H']

lista5 = list(range(1, 11))

lista6 = list('Pedro Henrique')
