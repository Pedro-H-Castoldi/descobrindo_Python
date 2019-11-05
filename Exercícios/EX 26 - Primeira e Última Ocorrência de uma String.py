"""
# Ex 1
n = str(input('Digite seu nome: ')).strip()
l = str(input('Digite a letra que deseja procurar no nome: '))
n = n.lower()
l = l[0].lower()
r = []

print(f'A letra "{l}" se repete {n.count(l)} veze(s) no nome {n.title()}.')

for i, _ in enumerate(n):
    if n[i] == l:
        r.append([i])
        c = i
if len(r) > 1:
    print(f'A letra "{l}" está presente nas casa {r[0][0]} e na casa {c}.')
elif len(r) == 1:
    print(f'A letra "{l}" está presente na casa {r[0][0]}.')
else:
    print('Finalizado!')


# EX 2
nome = str(input('Digite um nome/palavra: ')).lower().strip()
le = str(input('Digite a letra que deseja procurar no nome/palavra: ')).lower()
le = le[0]
print(f'A letra "{le}" se revete {nome.count(le)}x no nome/palavra: {nome.title()}')
if nome.count(le) > 1:
    print(f'A letra "{le}" está presente primeiramente na casa {nome.find(le)} e por último na casa {nome.rfind(le)}.')
elif nome.count(le) == 1:
    print(f'A letra "{le}" está presente somente na casa {nome.find(le)}.')
else:
    print('Finalizado!')
"""

"""
# Aula 27 - Primeiro e Último Nome de uma Pessoa
#EX 1
no = str(input('Digite o nome: ')).strip().title().split()
n2 = no.copy()
n2.reverse()
print(f'O primeiro nome é {no[0]} e o último é {n2[0]}.')

# EX 2
nom = str(input('Digite o nome: ')).strip().title().split()
print(f'O primeiro nome é {nom[0]} e o último é {nom[len(nom)-1]}.')

"""