zeron = []
i = 0
for i in range(15):
    n = int(input(f'Digite o {i+1}° número: '))
    zeron.append(n)

for i, _ in enumerate(zeron):
    if zeron[i] == 0:
        zeron.pop(i)

for i, _ in enumerate(zeron):
    print(zeron[i])

print(f'\n\n{zeron[0]}')