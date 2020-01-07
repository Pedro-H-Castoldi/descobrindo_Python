'''
# Forma comum de 0 a 10
for i in range(11):
    print(i)

# Forma especificando o primeiro valor, ou seja 1. Assim vai de 1 até 10
for i in range(1, 11):
    print(i)
'''

# Forma q espefifica o início e o final com pulos. Nesse exemplo de 2 em 2
for i in range(0, 11, 2):
    print(i, end= ' ')

print('\n')

# Forma inversa
for i in range(10, 0, -1):
    print(i, end= ' ')