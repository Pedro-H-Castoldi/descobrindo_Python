"""
bloco with -> O arquivo só será trabalhado dentro desse bloco, se tentar acessá-lo fora desse bloco, dará um erro,
pois o mesmo estará fechado.
"""

# O bloco with é a forma Pythônica de se trabalhar com arquivos.

with open('aprendendo.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())
    print(arquivo.closed) # False

#print(arquivo.readlines()) # Erro, fora do bloco with o arquivo n está aberto.
print(arquivo.closed) # True