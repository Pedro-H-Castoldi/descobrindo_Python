from collections import namedtuple

gabarito = ('e', 'a', 'b', 'd', 'd', 'a', 'd', 'e', 'c', 'e')
informa = namedtuple('Alunos', ['Matricula', 'Respostas', 'Nota', 'Situacao'])
alunos = []
resp = []
rr = []
nota = 0

for i in range(3):
    matricula = int(input('Informe sua matrícula: '))
    print('Coloque no gabarito suas respostas: ')
    for j, _ in enumerate(gabarito):
        r = str(input(f'Q{j+1}: '))
        rr.append(r[0])
        if rr[j] == gabarito[j]:
            nota += 1
        if rr[j] not in 'abcde':
            rr[j] = '*'

    if nota > 6:
        s = '\033[4;36mAPROVADO\033[m'
    elif nota >= 3 and nota < 7:
        s = '\033[4;33mRECUPERAÇÃO\033[m'
    else:
        s = '\033[4;31mREPROVADO\033[m'

    resp = rr.copy()
    rr.clear()
    dados = informa(Matricula= matricula, Respostas= resp, Nota= nota, Situacao= s)
    alunos.append(dados)
    nota  = 0

print('=*' * 55)
print(f'\033[1;34m{"MATRÍCULA"}{"RESPOSTAS":>36}{"NOTA":>40}{"SITUAÇÃO":>15}')
for i, _ in enumerate(alunos):
    print(f'{"":<2}{alunos[i].Matricula:<16}{alunos[i].Respostas}   {alunos[i].Nota:>12}         {alunos[i].Situacao}\033[1;34m')
print('\033[m=*' * 55)