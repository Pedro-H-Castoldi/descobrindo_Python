m = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
media = []
mm1 = []
mm0 = []
im = m1 = m2 = imp = 0
for i, _ in enumerate(m):
    for j in range(6):
        n = float(input(f'[{i}]x[{j}]: '))
        m[i][j] = n


for i in range(6):
    for j in range(3):
        if i == 1:
            m1 += m[j][1]

        if i == 3:
            m2 += m[j][3]

        if i == 5:
            m[j][5] = m[j][0] + m[j][1]

        if m[j][i]%2 != 0:
            imp += m[j][i]

media.append([m1/3, m2/3])

for i, _ in enumerate(m):
    for j in range(6):
        print(f'[{m[i][j]:^5}]', end= '')
    print()

print(f'MEDIA:\n    -COLUNA 2: {media[0][0]:.2f}\n    -COLUNA 4: {media[0][1]:.2f}')
print(f'SOMA DOS NÚMEROS IMPARES: {imp:.2f}')