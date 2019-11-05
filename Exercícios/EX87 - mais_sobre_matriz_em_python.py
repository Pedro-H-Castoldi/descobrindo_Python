m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = sc3 = mc2 = 0
for i, _ in enumerate(m):
    for j, _ in enumerate(m):
        n = int(input(f'Insira [{i}]x[{j}]: '))
        m[i][j] = n
        if n%2 == 0:
            par+= n

for i, _ in enumerate(m):
    for j, _ in enumerate(m):
        print(f'[{m[i][j]:^5}]', end='')
    print()

print(f'A soma dos valores pares é: {par}')
for i, _ in enumerate(m):
    sc3 += m[i][2]
print(f'A soma dos números da 3° coluna é: {sc3}')
print(f'O maior valor da 2° linha é: {max(m[1])}')