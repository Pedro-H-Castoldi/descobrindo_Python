"""
Os filter servem para filtrar dados de uma determinada coleção


# Importar uma biblíoteca que trabalha com dados estatisticos.
import statistics

# Dados da média das notas de uma sala
medias = [9, 6, 3, 10, 5, 7]

# Obter a média da sala
media_sala = statistics.mean(medias)

print(media_sala)

# Filtrar as médias: Apresentar as médias dos alunos que forem maiores que a média da sala.
# Os valores que estão em médias serão passados pela lambda com a condição dessas médias serem maiores que a média da sala.
resultado = filter(lambda x: x > media_sala, medias) # Assim como em Map o Filters recebe uma função e um interável.
print(list(resultado))

# Assim como na função map(), os dados serão excluidos depois da sua primeira execução.
print(f'NOVAMENTE: {list(resultado)}')

# Filtrar espaços vazios em um interável
paises = ['', 'Brasil', 'Angola', '', '', '', 'EUA', 'Itália', 'Austrália', '', '', 'Japão']

# Obter apenas os nomes dos países e excluir as casas ''.
# Formas:
#countries = filter(lambda p: len(p) > 0, paises)
#countries = filter(lambda p: p != '', paises)
countries = filter(None, paises) # Forma Pythonica

print(list(countries))

# A diferença entre map() e filter():
# map() - Recebe dois parâmetros, uma função e um interável, cada elemento do interável será mapeada para a função;

# filter() - Recebe dois parâmetros, uma função e um interável, os elementos que serão retornados, serão aqueles que tiverem de acordo com a função.
"""

# Filtrar usuários
users = [
    {'username': 'motaromk3', 'tweets': []},
    {'username': 'sindel', 'tweets': ['Eu sou a rainha que mudará o destino dos reinos', 'Estou de volta próximo mês...']},
    {'username': 'joker', 'tweets': ['Quem quer dar uma gargalhada?']},
    {'username': 'mileena', 'tweets': []}
]
#print(users)

# Filotrar ativos:
# Pega os elementos do interável e passa pela condição de que o tamanho dos elementos terão que ser maior que 0 (especificando a chave 'tweets' do dicionário).
at = list(filter(lambda u: len(u['tweets']) > 0, users))
print('ATIVOS:')
[print(us['username']) for us in at]

# filtrar usuários inativos:
print('\nINATIVOS:')
# F 1
#pas = filter(lambda u: len(u['tweets']) == 0, users)

# F 2
pas = filter(lambda u: not u['tweets'], users) # Quando not list == vazia é retornado um True (quando nega uma lista vázia é dado como True).
[print(us['username']) for us in pas] # Não é obrigado a converter para uma lista pois o list comprehension já faz isso.



# Combinar map() e filter()
# Apresentar os nomes dos instrutores, no entanto, os nomes deles devem ter menos do que 5 caracteres
intrutores = ['Marcolino', 'Pedro', 'José', 'Caio', 'Alex', 'Ana', 'Eva']

# O map() é como o parâmetro função e o filter() como o interável.
# O filter() filtra a lambda com uma condição (o nome possuir menos q 5 caracteres) e então o map() pega esse filtro e o executa.
nomes = list(map(lambda n: f'Nome: {n}', filter(lambda n: len(n) < 5, intrutores))) # Note que o filter() está dentro do map()
print(nomes)