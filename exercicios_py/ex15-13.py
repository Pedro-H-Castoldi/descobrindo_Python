#Q15:
nivers = []
d = 0
with open('2020.txt', encoding='UTF-8') as ar:
    arq = list(ar)

    for i in range(len(arq)):
        nivers.append(arq[i].split())
        d = int(nivers[i][1])
        d = 2020 - d
        nivers[i][1] = d

    for i in range(len(nivers)):
        if nivers[i][1] < 18:
            nivers[i][1] = f' - IDADE: {nivers[i][1]} (menor de idade).'
        elif nivers[i][1] == 18:
            nivers[i][1] = f' - IDADE: {nivers[i][1]} (entrando na maior idade).'
        elif nivers[i][1] > 18:
            nivers[i][1] = f' - IDADE: {nivers[i][1]} (maior de idade).'

    with open('idades.txt', 'w+', encoding='UTF-8') as idade:
        for i in range(len(nivers)):
            for j in range(len(nivers[i])):
                idade.write(nivers[i][j])
            idade.write('\n\n')

        idade.seek(0)
        print(idade.read())
