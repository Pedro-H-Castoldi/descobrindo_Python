A = []
A1 = []
A2 = []

for i in range(11):
    a = int(input(f'Adicione o {i+1}° número: '))
    if i < 11/2:
        A1.append(a)
    else:
        A2.append(a)

A1.sort()
A2.sort()
A2.reverse()
A = [A1, A2].copy()

for i in range(6):
    print(A[0][i])
for j in range(5):
    print(A[1][j])
