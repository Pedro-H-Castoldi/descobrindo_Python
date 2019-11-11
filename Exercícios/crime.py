perguntas = [
    'Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? '
]

resultado = 0

print('Bem-vindo à investigação criminal! Responda as perguntas com S (para sim) ou N (para não).')
for i, _ in enumerate(perguntas):
    resp = str(input(perguntas[i]))
    if resp in 'SsNn':
        if resp in 'Ss':
            resultado += 1
    else:
        print('Erro. Insira as respostas corretamente!')
        resultado = 0
        break

if resultado > 0:
    if resultado == 1:
        print('\n RESULTADO: Inocente.')
    elif resultado == 2:
        print('Suspeito.')
    elif resultado > 2 and resultado < 5:
        print('RESULTADO: Cumplece.')
    else:
        print('RESULTADO: Assassino!')
