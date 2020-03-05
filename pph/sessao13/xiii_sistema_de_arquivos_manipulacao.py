"""
Manipulação de Arquivos

import os

# Identificar se o arquivo existe
print(os.path.exists('aula_de_arquivos.txt')) # True

# Identificar se o diretório existe
# Path Relativos
print(os.path.exists('pacote')) # True
print(os.path.exists('arquivos')) # False
print(os.path.exists('pacote\\sub_pacote'))
print(os.path.exists('pacote\\sub_pacote\\__init__.py'))

# Path Absolutos
print(os.path.exists('C:\\Users\\PH\\Desktop\\P.H\\estudo_1\\next.jpg'))



# Criando arquivos (forma não indicada mas para o Windows é a única forma de utilização)
# Forma 1
open('testando_arquivo.txt', 'a', encoding='UTF-8').close() # Pode tbm fazer no modo 'x', 'w', etc.

# Forma 2
with open('testando_arquivo2.txt', 'w', encoding='UTF-8') as ar:
    pass # Isso indica q dentro do escopo n será feito nada, assim, logo encerra o mesmo.



# Criando arquivo (forma Pythônica) - Com o mknod tbm pode ser feita a operação de modo absoluto.
os.mknod('arquivo_test.txt') # O Windows n suporta essa funcionalidade..

# OBS:
# - Essa função n poderá funcionar dependendo do SO;
# - Se o arquivo já existir teremos o seguinte erro: 'FileExistsError'.



# Criando diretório (de modo único, 1 por 1)
os.mkdir('sessao1') # Tbm pode ser feito de modo absoluto
os.mkdir('sessao2')
os.mkdir('sessao3')
os.mkdir('sessao4')
os.mkdir('sessao5')
os.mkdir('sessao6')
os.mkdir('sessao7')
os.mkdir('sessao8')
os.mkdir('sessao9')
os.mkdir('sessao10')
os.mkdir('sessao11')
os.mkdir('sessao12')
os.mkdir('sessao13')

# Para criar diretórios dentro de outro diretório, é necessário criar um de cada vez mostrando o caminho
#os.mkdir('sessao1') # Usei o '#' pq o diretório já foi criado anteriormente
os.mkdir('sessao1\\descobrindoPython')


# Criando múltiplos diretórios (arvore de diretórios)
os.makedirs('sessao14\\interadoresEGeradores')

# Para ignorar o erro caso o diretório já existir
os.makedirs('sessao14\\interadoresEGeradores', exist_ok=True)

# OBS:
# - Se for executado o mkdir() ou o makedirs() e o diretório já existir aparecerá o seguinte erro: 'FileExistsError'
# - Se pelo menos um dos diretórios do caminho n existirem utilizando o makedirs(), n haverá erro e o diretório novo será criado

# Renomear diretórios
#os.rename('sessao14\\interadoresEGeradores', 'sessao14\\podeExcluir') # Deve indicar o caminho na parte de renomeação

# OBS: se o diretório n estiver vazio teremos o seguinte erro: 'OSError'

# Renomear arquivos
os.rename('aula_de_arquivos.txt', 'aula_de_arqs.txt')

# - Se o arquivo já existir aparecerá o seguinte erro: 'FileExistsError'



# Removendo arquivos
# CUIDADO! Arquivos removidos por meio de comando de deleção serão excluídos sem irem para a lixeira.
os.remove('novo.txt')

# OBS:
# - Se o arquivo n existir aparecerá o erro: 'FileNotFoundError';
# - No Windows um arquivo só poderá ser excluído se n estiver aberto ou em uso;
# - Se for excluir um diretório aparecerá o erro: 'IsADirectoryError'.



# Removendo diretórios vazios (se o diretório tiver conteúdo n será excluído)
os.rmdir('sessao14\\podeExcluir')



# Remover uma arvore de arquivos
for ar in os.scandir('geek3'):
    if ar.is_file():
        os.remove(ar.path)



os.makedirs('excluir\\remover\\tudo')
# Removendo uma árvore de diretórios vazia
os.removedirs('excluir\\remover\\tudo')



# Para q os arquivos/diretórios excluídos no Python vão para a lixeira, devemos instalar a biblioteca send2trash
# pip install send2trash
# Caso dê algum problema, execute esse comando antes: sudo apt-get install lsb-core
from send2trash import send2trash

# Criando 2 arquivos para ver a diferença de usar o send2trash
open('lixeira1.txt', 'w').close()
open('lixeira2.txt', 'w').close()

os.remove('lixeira1.txt') # N vai pra lixeira
send2trash('lixeira2.txt') # Vai pra lixeira



# Criando 2 diretórios para ver a diferença de usar o send2trash
os.mkdir('lixeira1')
os.mkdir('lixeira2')

os.removedirs('lixeira1') # N vai pra lixeira
send2trash('lixeira2') # Vai pra lixeira



# Criando arquivo e diretório temporário (q é excluído depois de um tempo)
import tempfile

# Criando diretório temporário
with tempfile.TemporaryDirectory() as temp:
    print(f'Criei o diretório temporário em {temp}')
    with open(os.path.join(temp, 'arquivo_temporario.txt'), 'a') as arq:
        arq.write('Esse arquivo é temporário!\n') # N escreveu
        input()

# Estamos criando um diretório temporário e abrindo o mesmo, dentro dele criamos um arquivo
# para então encrever nele. O input() é usado para manter os arquivos vivos dentro do with.

# OBS: Esse método n funcionará no Windows, pois esse SO trabalha de modo diferente com arquivos temporários.
"""

import os
from send2trash import send2trash
import tempfile

# Criando arquivo temporário
with tempfile.TemporaryFile() as arq:
    arq.write(b'Arquivo temporário') # Utilizamos a letra 'b' pois o arquivo temporário só aceita binários
    arq.seek(0)
    print(arq.read())

# Sem o bloco with
arqtemp = tempfile.TemporaryFile()
arqtemp.write(b'Arquivo temporário\n')
arqtemp.seek(0)
print(arqtemp.read())
arqtemp.close()

# Outra forma
ar = tempfile.NamedTemporaryFile()
ar.write(b'Temporário')
print(ar.name)
print(ar.read())
input()
ar.close()

# NÃO ESTÁ RODANDO OS ARQUIVOS TEMPORÁRIOS: SyntaxError: bytes can only contain ASCII literal characters.