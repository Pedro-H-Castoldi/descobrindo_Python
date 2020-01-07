"""
RECEBENDO DADOS DO USUÁRIO

"""
#Modo antigo
# print('Qual seu nome?')
# nome = input()

#Modo moderno
nome = input('Qual seu nome? ')

print(f'Seja bem vindo(a) {nome.lower().title()}')
anos = int(input(f'{nome.lower().title()} quantos anos você tem? '))
# Modo antigo
print('Então você se chama %s e possui %s anos!' %(nome.lower().title(), anos))

# Modo mais moderno de printar
print('Então você se chama {0} e possui {1} anos!' .format(nome.lower().title(), anos))

# Mais moderno q o já moderno
print(f'Então você se chama {nome.lower().title()} e possui {anos} anos!')

# Modo menos prático sem declarar o int no input
# print(f'{nome.lower().title()} nasceu no ano de {2018 - int(anos)} ou em {2019 - int(anos)}')
print(f'{nome.lower().title()} nasceu no ano de {2018 - anos} ou em {2019 - anos}.')