dados = []
maiorr = ''
m = c = 0
with open('alunos.txt', 'w+', encoding='UTF-8') as al:
    n = int(input('Insira o número de alunos: '))
    for i in range(n):
        while True:
            nome = str(input(f'Insira o nome do aluno {i+1}: '))
            if len(nome) > 40:
                print('ERRO: O nome deve conter no máximo 40 caracteres!')
            else:
                break
        nota = float(input(f'Insira a nota final do aluno {i+1}: '))
        notaa = f' - {nota:.2f}'
        dados.append([nome.title(), notaa])

        if nota > m:
            m = nota
            maior = dados[i]

    for i in range(len(dados)):
        if maior[1] == dados[i][1]:
            maiorr += f'{dados[i][0]}{dados[i][1]}\n'
            c += 1


    for i in range(len(dados)):
        for j in range(len(dados[i])):
            al.write(dados[i][j])
        al.write('\n')

    if c == 1:
        al.write(f'\nA maior nota final foi de: {maior[0]}{maior[1]}.')
    else:
        al.write(f'\nOs alunos com as maiores notas foram:\n{maiorr}')
    al.seek(0)
    print(al.read())