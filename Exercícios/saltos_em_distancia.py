import statistics
nome = 'default'
dados = {}
while nome:
    nome = str(input('Insira o nome do atleta: '))
    if nome in '                                                            ':
        break
    salto1 = float(input('Insira o valor do primeiro salto: '))
    salto2 = float(input('Insira o valor do segundo salto: '))
    salto3 = float(input('Insira o valor do terceiro salto: '))
    salto4 = float(input('Insira o valor do quarto salto: '))
    salto5 = float(input('Insira o valor do quinto salto: '))


    dados.update({nome.title(): [salto1, salto2, salto3, salto4, salto5]})

for i in dados:
    print(f'Atleta: {i}\n')
    print(f'Salto 1: {dados[i][0]:.2}m')
    print(f'Salto 2: {dados[i][1]:.2}m')
    print(f'Salto 3: {dados[i][2]:.2}m')
    print(f'Salto 4: {dados[i][3]:.2}m')
    print(f'Salto 5: {dados[i][4]:.2}m')

    print('Resultado final:')
    print(f'Atleta: {i}')
    print(f'Saltos: {dados[i][0]:.2f}m - {dados[i][1]:.2f}m - {dados[i][2]:.2}m - {dados[i][3]:.2}m - {dados[i][4]:.2}m')
    print(f'Média dos saltos: {statistics.mean(dados[i]):.2f}m')

    print()