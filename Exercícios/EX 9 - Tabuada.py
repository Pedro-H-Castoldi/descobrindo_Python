"""
        TABUADA

n = int(input('Digite o número: '))
for i in range(1,11):
    print(f'{n} * {i:<2} = {n * i}')

print('FIM!')



# CALCULADORA
n1 = float(input('N1: '))
o = str(input())
n2 = float(input('N2: '))

if o == '+':
    print(f'RESULTADO: {n1+n2}')

if o == '-':
    print(f'RESULTADO:{n1-n2}')

if o == '*':
    print(f'RESULTADO:{n1*n2}')

if o == '/':
    print(f'RESULTADO:{n1/n2}')

"""

n = int(input('Digite o número: '))
print('-' * 15)
for i in range(1,11):
    print(f'  {n} * {i:2} = {n * i}')
print('-' * 15)
print('           FIM!')