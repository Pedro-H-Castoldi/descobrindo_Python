"""
Modos de abertura de arquivos:
    - r -> Modo de abertura para leitura (padrão);
    - w -> Modo de abertura para escrita (sobrescreve caso o arquivo já exista);
    - x -> Modo de abertura para escrita (somente se o arquivo não existir), caso o arquivo já exista dará 'FileExistsError';
    - a -> Modo de abertura para escrita (adiciona o conteúdo ao final do arquivo caso já exista dados inseridos no mesmo).
        OBS: a (append), se o arquivo n existir será criado, caso exista o novo conteúdo será adicionado ao final.
    - + -> Modo de abertura para atualização: leitura e escrita (pode mover o cursor exceto com o +a. De toda forma é possível mover o cursor sem o +)


# Usando o modo de abertura 'x' e tratando erro.
try:
    with open('aula_de_arquivos.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('As férias estão chegandooo')
except FileExistsError:
    print('Esse arquivo já existe. Não será permitido sobrescrevê-lo.')


# Utilizando o modo de abertura 'a'
with open('escrevendo_em _loop.txt', 'a', encoding='UTF-8') as ar:
    while True:
        algo = str(input('Digite algo ou parar para sair: '))
        if algo != 'parar':
            ar.write(algo + '\n')
        else:
            break


# Com o 'a' n se pode mexer o cursor, o arquivo SEMPRE será adicionado ao final
with open('aula_de_arquivos.txt', 'a', encoding='UTF-8') as ar:
    ar.seek(0)
    ar.write('\nSEMPRE É')
    ar.seek(3)
    ar.write('palno terreno')
"""

# Utilizando o '+' (leitura e escrita)
with open('aula_de_arquivos.txt', 'r+', encoding='UTF-8') as ar:
    ar.write('Testando o ++++++++++++=')
    ar.seek(5)
    ar.write('olá? O seek dá pra ser usado mesmo sem o modo +')
    print(ar.read()) # N leu