v = []
v1 = []
v2 = []
for i in range(10):
    n = int(input(f'Digite o {i+1}° número: '))
    v.append(n)

for i, _ in enumerate(v):
    if v[i]%2 == 0:
        v2.append(v[i])
    else:
        v1.append(v[i])

for i, _ in enumerate(v):
    print(f'|{v[i]}', end= '| ')
print('\n')

for i, _ in enumerate(v1):
    print(f'|{v1[i]}', end= '| ')
print('\n')
for i, _ in enumerate(v2):
    print(f'|{v2[i]}', end= '| ')
