print('\033[1;35;41mCores em Python\033[m\n')
print('\033[1;35mPedro\033[4;36m Henrique\033[7;34;41m Castoldi\033[0;33;40m Bezerra\033[m\n\n')
n = 'Olá'
c = 'cores!'
print(f'\033[0;31m{n} \033[0;34;40m{c}\033[m eie')


# Utilizando dicionário
cores = {'branco': '\033[0;30m', 'vermelhor': '\033[0;31m', 'verde': '\033[0;32m', 'amarelo': '\033[0;33m', 'azul': '\033[0;34m', 'roxo': '\033[0;35m'}
print(f'{cores["roxo"]}{n} {cores["amarelo"]}TESTE!!!\033[m')