"""
max()-> retorna o maior valor de um interável, ou o maior valor entre 2 ou mais valores.


# max() em lista:
lista = [3, 99, 43]
print(max(lista))

# max() em um dicionário:
dic = {'a': 22, 'b': 954, 'c': 787}
print(max(dic)) # Asim ele vai imprimir a letra mais à frente da ordem alfabética (c)

print(max(dic.values())) # Assim imprimirá o maior valor (954)

# Faça um programa q pegue 2  valores inseridos pelo usuário e imprima o maior deles:
v1 = int(input('Insira o valor 1: '))
v2 = int(input('Insira o valor 2: '))

print(f'O maior valor é: {max(v1, v2)}.')

print(max(3, 77, 54, 3))
print(max('a', 'f', 'ab', 'w', 'y'))
print(max('asq', 'abg', 'z', 'eio', 'Z')) # A primeira letra é a q conta. 'abc' será analisada o 'a', letras maiúsculas tem menos prioridade


min()-> É o contrário de max()

print(min(3, 77, 54, 3))
print(min('a', 'f', 'ab', 'w', 'y'))
print(min('asq', 'abg', 'z', 'eio', 'Z')) # Z maiúsculo
print(min('Mortal kombat 11')) # O menor valor é o espaço ' '


nomes = ['Rogério', 'Cristian', 'Bolsonaro', 'Noob Saibot']
print(max(nomes)) # Rogério (pela primeira letra com base em ordem alfabética)

print(min(nomes)) # Bolsonaro

# Alterar o comportamento de min() e max(). por meio da key q permite botar uma função em meio à min() e max():
# Pegar o maior e menor nome por base de seu tamanho (len())
print(max(nomes, key=lambda no: len(no)))

print(min(nomes, key=lambda n: len(n)))

"""

# Musica mais e menos tocadas
musicas = [
    {'nome': 'Bohemia Rhapsody', 'tocou': 10000000},
    {'nome': 'Espere não Vá', 'tocou': 30000},
    {'nome': 'Paz do Mundo', 'tocou': 500000},
]

print(max(musicas, key=lambda m: m['tocou']))
print(min(musicas, key=lambda m: m['tocou']))

# Imprimir só o nome da musica
print(max(musicas, key=lambda m: m['tocou'])['nome']) # Bota o nome da chave que se quer ver os valores fora da função max()/min()
print(min(musicas, key=lambda m: m['tocou'])['nome'])

# Fazer o mesmo sem usar max()/min() e lambda
menor = musicas[0]['tocou']
maior = musicas[0]['tocou']
maiorr = menorr = 'a'

for i, _, in enumerate(musicas):
    if maior <= musicas[i]['tocou']:
        maior = musicas[i]['tocou']
        maiorr = musicas[i]['nome']
print(f'O nome com maior valor de musicas tocadas é: {maiorr}.')

for i, _ in enumerate(musicas):
    if menor >+ musicas[i]['tocou']:
        menor = musicas[i]['tocou']
        menorr = musicas[i]['nome']
print(f'O nome com menor valor de musicas tocadas é: {menorr}.')

# Modo mais rápido
maior = 0
menor = 999999

for i in musicas:
    if i['tocou'] > maior:
        maior = i['tocou']
for i in musicas:
    if i['tocou'] == maior:
        print(f'Mais tocada: {i["nome"]}')

for i in musicas:
    if i['tocou'] < menor:
        menor = i['tocou']
for i in musicas:
    if i['tocou'] == menor:
        print(f'A menos tocada: {i["nome"]}')