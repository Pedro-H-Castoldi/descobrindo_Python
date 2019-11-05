matriz = [[0,0,0], [0,0,0], [0,0,0]]
somam = []
s = 0

for i, _ in enumerate(matriz):
    for j, _ in enumerate(matriz):
        n = int(input(f'Insira [{i}]x[{j}]: '))
        matriz[i][j] = n

for i, _ in enumerate(matriz):
    for j, _ in enumerate(matriz):
        s += matriz[j][i]
    somam.append(s)
    s = 0

print(f'\033[1;32m{"MATRIZ":^15}')
for i, _ in enumerate(matriz):
    for j, _ in enumerate(matriz):
        print(f'{matriz[i][j]:^5}', end= '')
    print()
print(f'\033[1;36m{"SOMA":^10}')
for i, _ in enumerate(somam):
    print(somam[i], end=' ')