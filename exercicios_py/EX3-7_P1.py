c1 = []
c2 = []
for i in range(10):
    n = float(input(f'Digite o {i+1}° número: '))
    c1.append(n)
    nq = n**2
    c2.append(nq)

print('CONJUNTO 1  |  CONJUNTO 2')
for i, _ in enumerate(c1):
    print(f'     {c1[i]}    |    {c2[i]}')


