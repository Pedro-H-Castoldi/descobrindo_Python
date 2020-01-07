"""
RECAPTULANDO:
    tupla = (1, 2, 3)
    print(tupla[2])

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome e parâmetros.


from collections import namedtuple
# Nomeando Nome e Parâmetros
# Forma 1
cachrro = namedtuple('Cachorro', 'Nome Idade Raça')

# Forma 2
cachrro = namedtuple('Cachorro', 'Nome, Idade, Raça')

# Forma 3 (recomendada)
cachorro = namedtuple('Cachorro', ['Nome', 'Idade', 'Raça'])

juninho = cachrro(Nome= 'Juninho', Idade= 3, Raça= 'Piri')

# printando
# Forma 1
print(juninho)
print(juninho[2]) # acessando só um dado

# Forma 2
print(juninho.Nome)
print(juninho.Raça)

print(juninho.index('Piri')) # Em qual casa está indexada a palavra 'Piri' na tupla juninho
print(juninho.count(3)) # Quantas vezes o número 3 está presente na tupla juninho
"""
from collections import namedtuple
cachorro = namedtuple('Cachorro', ['Nome', 'Idade', 'Raça'])
dogs = []
while True:
    n = str(input('NOME: '))
    i = int(input('IDADE: '))
    r = str(input('RAÇA: '))
    pets = cachorro(Nome= n.title(), Idade= i, Raça= r.title())
    dogs.append(pets)
    res = str(input('Continuar inserindo dados? S/N '))
    if res in 'Nn':
        break
print('-=-'*18)
print(f'{"NU.":<7}{"NOME":<14}{"IDADE":<18}{"RAÇA"}')
print('-=-'*18)

for i, _ in enumerate(dogs):
    print(f'{i:<7}{dogs[i].Nome:<14}{dogs[i].Idade:<18}{dogs[i].Raça}')

nu = int(input('Digite o número do cachorro para ver suas informações ou -1 para finalizar: '))
if nu == -1:
    print('Finalizador!')
else:
    print(f'NÚMERO: {nu}\nNOME: {dogs[nu].Nome}\nIDADE: {dogs[nu].Idade}\nRAÇA: {dogs[nu].Raça}')

