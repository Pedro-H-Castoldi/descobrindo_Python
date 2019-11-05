m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
cont = 0

for i in range(0, 4):
    for j in range(0, 4):
        n = int(input(f'Digite o numero para [{i}]x[{j}]: '))
        m[i][j] = n
        if n > 10:
            cont += 1
for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{m[i][j]:^5}]', end='')
    print()

print(f'Existe(m) {cont} números maior(es) que 10.')