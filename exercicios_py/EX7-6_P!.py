numeros = []
index = []
for i in range(10):
    n = int(input(f'Digite o {i+1}° número: '))
    numeros.append(n)

r = max(numeros)

for i, _ in enumerate(numeros):
    if numeros[i] == r:
        index.append(i)
    print(f'|{numeros[i]}', end= '| ')

print(f'\nMAIOR NÚMERO:\n{r}')
print('CASA(S):')
for i, _ in enumerate(index):
    print(f'|{index[i]}', end= '| ')


