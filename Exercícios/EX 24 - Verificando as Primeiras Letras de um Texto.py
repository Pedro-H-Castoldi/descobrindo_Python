"""
EX 24
c = str(input('Digite o nome da cidade onde vc nasceu: ')).strip()
cn = c
cn = cn.title()
cn = cn.split()
cr = 'Cedro'

if cn[0] == cr:
    print(f'Correto! Você nasceu na cidade {c} que começa com {cn[0]}.')
else:
    print(f'Errado! Você não nasceu nessa cidade.')


# EX 25 - Procurar uma String Dentro de Outra
# EX 1
nome = str(input('Digite seu nome completo para saber se no mesmo possui o nome "Castoldi": ')).strip()
nomec = nome.title().split()
tem = False

for i, _ in enumerate(nomec):
    if nomec[i] == 'Castoldi':
        tem = True

if tem:
    print(f'Seu nome é {nome.title()} e possui o nome "Castoldi".')
else:
    print(f'Seu nome é {nome.title()} e não possui o nome "Castoldi".')
"""

#EX 2
nome = str(input('Digite seu nome para saber se tem o nome "Castoldi" nele: ')).strip()
nome = nome.title()
if 'Castoldi' in nome:
    print(f'Seu nome é {nome} e possui o nome "Castoldi"')
else:
    print(F'Seu nome é {nome} e não possui o nome Castoldi')

