"""
seek() -> É utilizado para mover o cursor pelo arquivo. Essa função recebe como parâmetro um número
para indicar onde o cursor deve ser movido.


arquivo = open('aprendendo.txt')
print(arquivo.read())

# Limitando a quantidade de caractéries q serão lidos no arquivo
print(arquivo.read(20)) # Serão lidos 20 caracteres - 1

# seek significa procurar
arquivo.seek(0) # Movimenta o cursor pra casa 0. Dessa forma será exibido o texto novamente se usar a função read()

print(arquivo.read())

# Movimentando para a casa 10 o cursor
arquivo.seek(10)

print(arquivo.read())


# readline() -> imprime linha a linha
print(arquivo.readline())
print(arquivo.readline()) # O cursor será mandado para próxima linha, desse modo se chamar a função novamente, será lida a segunda linha.

rl = arquivo.readline() # É sempre bom saber o q uma função nos retorna
print(type(rl))
print(rl)
print(rl.split(' '))



# readlines() -> Cria uma lista onde cada linha é um elemento dessa lista.
linhas = arquivo.readlines()
print(linhas)
print(len(linhas))



# OBS: Quando utilizamos a função open(), se inicia uma conexão entre o arquivo no disco do computador e o programa,
# essa conexão é chamada de streaming. Ao finalizar os trabalhos, é importante finalizar a conxão, fazemos isso
utilizando a função close().

Passos para se trabalhar com arquivos:
    1 - Abrir o arquivo;
    2 - Trabalhar o arquivo;
    3 - Fechar o arquivo.

"""
# 1 - Abrir o arquivo
arquivo = open('aprendendo.txt')

# 2 - Trabalhar o arquivo
print(arquivo.readline())

# closed -> Verifica se o arquivo foi fechado ou n (sim/True, n/False)
print(arquivo.closed) # False

# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed) # True

print(arquivo.read()) # Gerará um erro. Pois depois de fechado n se pode mais manipular o arquivo, só se o mesmo for aberto novamente.