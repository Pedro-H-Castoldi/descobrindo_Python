"""
Mapas são conhecidos em Python como Dicionários, ou seja:
    Mapa = Dicionário


    # Interando em mapas
for chave in receitas:
    print(chave) # Imprimindo as chaves do mapa

for chave in receitas:
    print(receitas[chave]) # Imprimindo os valores do mapa

for chave in receitas:
    print(f'No mes de {chave} foi apurado {receitas[chave]}') # Imprimindo chave e valor com texto



# Acessando as chaves
print(receitas.keys())

for chave in receitas.keys(): # Esse é o modo Pythonico de se fazer
    print(receitas[chave])




# Acessando os valores
print(receitas.values())

for valores in receitas.values(): # Modo Pythonico
    print(valores)


# Desempacotamento de dicionários
print(receitas.items())

for chave, valor in receitas.items():
    print(f'Chave {chave} e valor {valor}')



# Saber o valor: Maior, menor, soma e tamanho (Só funciona em numeros inteiros ou reais)
print(max(receitas.values())) # Saber o maior valor, por isso a função 'values()'
print(min(receitas.values())) # '''
print(sum(receitas.values())) # '''
print(len(receitas))      # Saber o tamanho do dicionario, n precisa da 'values.()' já q irá buscar o tamanho do mesmo
"""

receitas = {'JAN': 3000, 'FEV': 3444, 'MAR': 5999}
print(receitas)
