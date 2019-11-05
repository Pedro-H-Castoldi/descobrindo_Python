v1 = []
v2 = []
vu = {}
for i in range(10):
    n1 = int(input(f'\033[1;36mDigite o {i+1}° número do vetor 1: '))
    v1.append(n1)

for i in range(10):
    n2 = int(input(f'\033[1;32mDigite o {i+1}° número do vetor 2: '))
    v2.append(n2)

v1 = set(v1.copy())
v2 = set(v2.copy())

vu = v1.union(v2)

print(f'\033[1;31m{vu}')