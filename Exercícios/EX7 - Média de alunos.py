print(  '-Sistema de Notas Acadêmico-')
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    m = (n1+n2)/2
    print(f'NOME..: {nome.title()}\nNOTA 1: {n1}\nNOTA 2: {n2}\nMÉDIA.: {m:.1f}')
    if m < 7 and m > 4:
        print('Aluno em recuperação..')
    elif m < 4:
        print('Aluno reprovado..')
    else:
        print('Aluno aprovado!')
    res = str(input('Adicionar mais notas? S/N: '))
    if res in 'Nn':
        break

