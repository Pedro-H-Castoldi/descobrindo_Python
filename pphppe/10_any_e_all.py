"""
all() - Retorna True se todos os elementos do interável for verdadeiros ou se o interável estiver vazio.

print(all([0, 1, 5, 7])) # Retorna False pq o 0 é False;
print(all({1, 7, 5, 3})) # Retorna True já q n tem nenhum False;
print(all(())) # Retorna True já q o interável está vazio;
print(all('Skarlat')) # True.

# Verificar se em uma lista todos os nomes começam com a letra 'A'/'a':
nomes = ['Adriano', 'Ave', 'Amélia', 'Adão']
print(all([nome[0] in 'Aa' for nome in nomes]))

# OBS: Um interável vazio em boolean é False, mas em all() é True.

any() - Retorna True se pelo menos 1 dos elementos do interável for True, Reforna False se o interável estiver vazio.
"""
print(any({0, 1, 4})) # retorna True, só de ter 1 True é o sufuciente;
print(any([])) # Retorna False, pois o interável está vazio;

nomes = ['Adriano', 'Ave', 'Amélia', 'Adão', 'Bruno']
print(any([nome[0] in 'Aa' for nome in nomes])) # Retorna True

print(any([n for n in [1, 3, 5, 2, 4] if n % 2 == 0])) # Retorna True
