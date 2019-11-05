alunos = []
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2)/ 2

    alunos.append([nome.title(), [nota1, nota2], media])
    resp = input('Deseja colocar dados de outro aluno? S/N: ')
    if resp in 'Nn':
        break

print('-#' * 25)
print(f'{"N.":<7}{"NOME":<35}{"MÉDIA"}')
print('-' * 50)

for i, v in enumerate(alunos):
    print(f'{i:<7}{alunos[i][0]:<35}{alunos[i][2]}')

while True:
    al = int(input('Digite o número de um aluno para ver as notas ou digite "-1" para finalinar: '))
    if al == -1:
        break
    elif al <= len(alunos) - 1:
        print(f'        Notas do aluno {al}')
        print('-' * 50)
        print(f'{"NU.":<7}{"NOME":<35}{"NOTA 1":<21}{"NOTA 2":<21}{"MÉDIA"}')
        print(f'{al:<7}{alunos[al][0]:<35}{alunos[al][1][0]:<21}{alunos[al][1][1]:<21}{alunos[al][2]}')

print('Finalizado!')
