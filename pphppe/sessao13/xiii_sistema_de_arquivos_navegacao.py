"""
Para se fazer uso de manipulação de arquivos do sistema operacional, é necessário importar o módulo os.

os -> Operating system - Sistema Operacional



# Importando os
import os

# getcwd() -> current work directory (diretório de trabalho corrente).
# Retorna o path (caminho absoluto).
print(os.getcwd()) # C:\\Users\\PH\\PycharmProjects\\descobrindo_Python\\pphppe

# Para mudar o diretório utilizamos o chdir() (Para ir mudando o diretório basta repetir a operação)
os.chdir('..') # C:\\Users\\PH\\PycharmProjects\\descobrindo_Python

print(os.getcwd())

# Para verificar se o diretório é absoluto (True/False)
print(os.path.isabs('/home/PH/')) # True

# Se o usuário estiver no SO Windows
print(os.path.isabs('C:\\Users\\PH\\')) # Se utiliza duas '\' pq a barra invertida é usada para quebra de linha na programação

# Para saber qual SO se está usando - posix (Linux e Mec) / nt (Windows)
print(os.name)

# Para ter mais detalhes sobre o SO (n dá para executar essa operação no Windows)
print(os.uname())

# No Windows no máximo podemos fazer isso
import sys
print(sys.platform) # Dirá se o Windows é 32 ou 64 bits

"""

import os

# Criando uma pasta pelo Python
#print(os.getcwd()) # C:\\Users\\PH\\PycharmProjects\\descobrindo_Python\\pphppe

#res = os.path.join(os.getcwd(), 'pythonTest')

#os.chdir(res)

#print(os.getcwd()) # Deu erro..

# Note q o os.path.join() recebe dois parâmetros (ou mais), sendo o primeiro o diretório atual
# e o segundo o diretório q será juntado ao diretório atual.

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())

# Listas da pasta raiz e ver o temanho da lista
print(os.listdir('C:\\'))
print(len(os.listdir('C:\\')))

# Podemos listar os arquivos e diretórios com mais detalhe usando o sacndir()
print(list(os.scandir('C:\\'))) # Temos q converter para lista já q ele retorna um generator

# Dessa forma podemos trabalhor com ele já q agora o mesmo é uma lista
scan = os.scandir('C:\\')
arq = list(scan)

print(dir(arq[0]))

print(arq[0].name) # Nome do arquivo.
print(arq[0].inode()) # ID do arquivo.
print(arq[0].is_dir()) # É um diretório?
print(arq[0].is_file) # É um arquivo?
print(arq[0].is_symlink()) # É um link simbólico?
print(arq[0].path) # Caminho do arquivo.
print(arq[0].stat()) # Diz várias informações sobre o arquivo (estatísticas).

# Devemos fechar o scandir sempre depois de utilizá-lo!
scan.close()

