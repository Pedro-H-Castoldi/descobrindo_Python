"""
Módulos Python nada mais são q arquivos Python, então podemos importar esses arquivos
 para nosso programa (arquivos incluvive, q nós criamos)


# Importanto uma função customizada do módulo args
from args import multiplica
print(multiplica(1, 3, 3, 3, 2))


# Importando tudo de um módulo. Quando se diz tudo é TUDO mesmo, incluindo variáveis, etc
import args

print(args.multiplica(3, 3)) # Usando uma função

print(args.numeros) # Imprimindo a lista q foi importada de args

print(args.multiplica(*args.numeros)) # utilizando a função importada na lista tbm importada
# OBS: O '*' é para descompactar a lista e inseri-la como argumento já q na função 'multiplica' o parametro é um *args
"""

from x_map import c_to_f, cidade
print(cidade)
print(list(map(c_to_f, cidade)))

# OBS: Se no módulo existe um print, o print será executado quando o módulo for importado;
# Arquivos com números em seu nome n serão importados.
