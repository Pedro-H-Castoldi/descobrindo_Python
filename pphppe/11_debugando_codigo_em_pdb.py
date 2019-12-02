"""
Debugando com o Pycharm e o PDB (Python Debugger)


# Forma informal de debugar
def divisao(a, b):
    print(f'a={a} b={b}') # N recomendado
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


na = input('N1: ')
nb = input('N2: ')

print(divisao(na, nb))


# Fazendo o debugger de forma correta. Utilizando o Pycharm
def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print(divisao(3, 0))


# Forma correta do debugger com o PDB (forma 1)
# Para isso precisaremos da biblíoteca PDB e a função set_trace()
# COMANDOS BÁSICOS DO PDB:
# l (listar onde estamos no código);
# n (próxima linha);
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
import pdb

nome = 'Junior'
sobrenome = 'Castoldi Bezerra'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Latir'
final = nome_completo + ' faz o curso de ' + curso
print(final)


# Forma correta do debugger com o PDB (forma 2)
# Para isso precisaremos da biblíoteca PDB e a função set_trace()
# COMANDOS BÁSICOS DO PDB:
# l (listar onde estamos no código);
# n (próxima linha);
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Junior'
sobrenome = 'Castoldi Bezerra'
import pdb; pdb.set_trace() # Forma mais prática já q depois de debugar será excluída essa parte, é melhor alocar tudo em uma linha.
nome_completo = nome + ' ' + sobrenome
curso = 'Latir'
final = nome_completo + ' faz o curso de ' + curso
print(final)


# Forma correta do debugger com o PDB (forma 3)
# Para isso precisaremos da biblíoteca PDB e a função set_trace()
# COMANDOS BÁSICOS DO PDB:
# l (listar onde estamos no código);
# n (próxima linha);
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Junior'
sobrenome = 'Castoldi Bezerra'
breakpoint() # a partir da versão 3.7 a biblíoteca pdb virou uma função built-in chamada breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Latir'
final = nome_completo + ' faz o curso de ' + curso
print(final)
"""

# OBS: Cuidado com o conflito entre os comandos do PDB e o nome das variáveis
def numeros(l, n, p, c):
    breakpoint()
    return f'{l} {n} {p} {c}'

print(numeros(1, 3, 5, 2))

# Para solucuionar  os conflitos basta usar o comando p e depois o nomeda variável se quiser ver o valor da mesma.
# EX: p n = (3)

# SEMPRE OPTAR POR NOMES SIGNIFICATIVOS
