"""
Para o conteúdo de um arquivo em Python, usamos uma função integrada open() (abrir).

open() -> Na forma mais simples de utilizá-la usamos apenas um parâmetro de entrada, que é o caminho do arquivo a ser lido.
Essa função retorna _io.TextIOWrapper e é com ele q será trabalhado.

docs.python.org/3/library/functions.html#open (explica os parâmetros da função open())

# OBS: Por padrão a função open() abre o arquivo para leitura. Este arquivo deve exixtir,
ou será apresentado um erro chamado FileNotFoundError.

<_io.TextIOWrapper name='aprendendo.txt' mode='r' encoding='cp1252'> # encoding deve ser UTF-8 por recomendação

mode r -> Modo de leitura (r -> read() -> ler)

"""

# EX - Abrindo o arquivo 'aprendendo.txt'
arquivo = open('aprendendo.txt', encoding= 'UTF-8') # Fiz a conversão do encoding para UTF-8 já q estava cp1253 (bugando nas acentuações)
#print(type(arquivo))
#print(arquivo)

# Após o arquivo ser aberto (open()) ele deve ser lido (read())
r = arquivo.read()
print(type(r))
print(r)
#print(arquivo.read())


# Em Python, é utilizado um cursor para leitura de arquivos, esse cursor funciona como o cursor quando estamos digitando.
# se for chamada mais uma vez a função read(), n irá acontecer nada, pois o cursor já leu tudo o q precisava ser lido na primeira vez.

#print(arquivo.read())