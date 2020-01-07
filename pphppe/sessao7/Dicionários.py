"""
OBS: Em algumas linguagens de programação o dicinários Python são conhecidos como mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves '{}'

OBS: Sobre Dicionários:
    - chave e valor são separados por dois pontos (Chave : Valor);
    - Tanto as chaves quanto os valores podem ser de qualquer tipo;
    - Podemos misturar tipos de dados.

print(type({}))

# Modos de usar o dicionário
#Forma 1 (mais comum)
paises = {'BR' : 'Brasil', 'EUA' : 'Estados Unidos', 'JP' : 'Japão'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)
estados = dict(CE= 'Ceará', SP= 'São Paulo', MT= 'Mato Grosso')
print(estados)
print(type(estados))


# Acessar elementos
# Forma 1 - Acessando via chave
# OBS: Quando tenta acessar uma chave q n existe um erro aparece
print(paises['BR'])
print(estados['CE'])

# Forma 2 - Acessando via get (mais recomendado)
# OBS: Quando tenta acessar algo q n existe n dá erro, irá aparecer o tipo de dado None (tipo de dado sem tipo)
print(paises.get('BR'))
print(paises.get('RSS')) # None

# None é sempre tratado como falso (False) em Python
pa = input('Digite a sigla do país que vai ser procurado no dicionário: ')
if pa in paises:
    print(f'Pais encontrado: {paises.get(pa)}.')
else:
    print('País não encontrado.')

# Outra forma
#Se for achado inprime: a sigla, se n for achado imprime: 'Não foi encontrado'
pa2 = paises.get('RSS', 'Não foi encontrado.')
print(f'Pais: {pa2} ')


# Saber se uma chave está no dicionário
print('BR' in paises)
print('RSS' in paises)
print('Japão' in paises) # 'Japão' n é uma chave e sim um valor. 'JP' q é uma chave


# É possivel colocar qualquer valor nos dicionários, até mesmos listas e tuplas
# Tuplas são recomendadas para serem chaves, pois são imutáveis:
localidades = {
    (35.774, 35.775): 'Escritório em Tókio',
    (11.433, 11.434): 'Escritório em Nova York',
    (33.544, 33.545): 'Escritório em São Paulo'
}
print(localidades)
print(localidades[35.774, 35.775])
print(localidades.get(35.774, 35.775)) # Pelo q parece n dá pra imprimir quando se tem dois valores
print(type(localidades))


# Adicionando dados em um dicionário
receita = {'JAN': 300, 'FEV': 330, 'MAR': 450}
# Forma 1 - mais comum
receita['ABR'] = 1000
print(receita)

# Forma 2
novo_dado = {'MAI': 448}
receita.update(novo_dado) # Tbm é possível fazer assim: receita.update({'MAI': 448})
print(receita)


# Atualizar elementos em um dicionário
# Forma 1
receita['ABR'] = 220
print(receita)

# Forma 2
receita.update({'MAI': 1200})
print(receita)

# Com isso:
    # - É notado q o modo para adicionar elementos é o mesmo de atualizar os dados
    # - As chaves NÃO podem se repetir!


# Remover elementos de um dicionário. Caso n exista o elemento a ser retirado uma mensagem de erro é apresentada
# Forma 1 - Mais comum
print(paises)
ret = paises.pop('EUA') # Desse modo o elemento retirado é armazenado em uma variável (tbm pode ser: paises.pop('EUA')
print(paises)
print(ret)

# Forma 2
del paises['BR'] #Desse modo n dá para armazenar o elemento eliminado em uma variável
print(paises)


# Quando utilizar dicionários?
# Imagine em um sistemas de compra online, onde no carrinho cada produto tem suas especificações:
    # - Nome:
    # - Preço:
    # - Quantidade:

# Para isso podemos usar listas? Sim
carrinho = []
produto1 = ['Plastation 4', 1800.00, 2]
produto2 = ['Notebook', 3000.00, 1]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Para isso podemos usar tuplas? Sim
produto1 = ('Plastatio4', 1800.00, 2)
produto2 = ('Notebook', 3000.00, 1)

carrinho = (produto1, produto2)
print(carrinho)

# Para isso podemos usar dicionários? SIM!
carrinho = []
produto1 = {'Nome': 'Plastation 4', 'Preço': 1800.00, 'Quantidade': 2}
produto2 = {'Nome': 'Notebook', 'Preço': 3000.00, 'Quantidade': 1}

carrinho.append(produto1) # Dicionário dentro de uma lista
carrinho.append(produto2)
print(carrinho)

# É notado q o dicionário é a melhor solução para isso, pois ele apresenta informações mais detalhadas por meio de
# suas chaves, como o Nome, Preço e Quantidade.


# Limpar dados do dicionário
print(paises)
paises.clear()
print(paises)


# Copiar dicionário
# Forma 1 - Deep Copy
print(paises)
novo.txt = paises.copy() # Deep Copy
novo.txt['AUS'] = 'Australha'

print(paises)
print(novo.txt)

# Forma 2 - Shallow Copy
print(estados)
new = estados # Shallow Copy (a mudança na cópia afetará o original)
new['PB'] = 'Paraíba'

print(estados)
print(new)
"""



localidades = {
    (35.774, 35.775): 'Escritório em Tókio',
    (11.433, 11.434): 'Escritório em Nova York',
    (33.544, 33.545): 'Escritório em São Paulo'
}
print(localidades)
print(localidades[35.774, 35.775])
print(localidades.get(35.774, 35.775)) # Pelo q parece n dá pra imprimir quando se tem dois valores
print(type(localidades))