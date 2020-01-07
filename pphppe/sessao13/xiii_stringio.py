"""
Para ler ou escrever dados em arquivos, é preciso q o sftware tenha permissão do sistema operacional.

StringIO -> Utilizado para ler e criar arquivos na memória.
"""

# Primeiro é preciso importar
from io import StringIO
mensagem = 'É necessário ser duro as vezes..'

# Podemos criar um arquivo em memória já com uma string inserida ou vazia.
arquivo = StringIO(mensagem) # Isso equivale à: arquivo = open('um_arquivo_txt.txt', 'w')

# Com isso, agora podemos utilizar tudo o que já foi aprendido
print(arquivo.read())

# Escrevendo outro texto
arquivo.write('Não deixe os outros abusarem de você.')

# Mover o cursor para o início, assim podendo ver o q foi inserido no texto.
arquivo.seek(0)
print(arquivo.read())