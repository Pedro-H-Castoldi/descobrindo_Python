
nome = 'Pedro Henrique'

lista = {1, 6, 4, 9, 3}

numeros = range(8, 11) #Temos q transformar em uma lista

'''
# Exemplo de um FOR em uma string
for letra in nome:
    print(letra)

print('\n')

# Exemplo de um FOR em uma lista
for n in lista:
    print(n)

print('\n')

# Exemplo de um FOR em um range
# Com o range irá a sequência do primeiro numero q foi dito até o segundo número -1 (nesse ex do 1 até o 9)
for n in range(1, 10):
    print(n)

# enumerate: i = indice e v = valor (letra nesse caso). {(0, 'P'), (1, 'e'), ..., (13, 'e')}
for i, v in enumerate(nome): # Pode colocar um '_' caso n queira especificar um valor. EX: for _, v in enumerate(nome)
    print(i, v) # Pode ser tbm print(i) ou print(v)


# Assim aparece tanto o i como o v juntos, sem precisar de print(i, v).
Caso queira printar só o i faça: valor[0], v faça valor[1].
for valor in enumerate(nome):
    print(valor)
    
        
# Quantas vezes o FOR deve rodar
q = int(input('Quantas vezes o loop deve rodar? '))
soma = 0

for i in range(1, q+1): #Acrescenta 1 pq senão fica faltando um. EX: q = 4 será imprimido até 3
    num = int(input(f'informe o {i}/{q} valor: '))
    soma+= num
print(f'a soma é: {soma}')

# Em vez de pular linhas bota espaços no print. EX: P e d r o ou print(i, end='') espaço so entre os 2 nomes
for l in nome:
    print(l, end= ' ') 



#Imprime em modo de "triângulo" o nome
for i in range(1, 11):
    print(f'{nome * i}')
  

emoji = 'U0001F60E'
for _ in range(3):
    for i in range(1, 11):
        print('\U0001F60E' * i)


for i in range(3): # Assim vai do 0 até o 2. range(1, 3) vai do 1 até o 2
    print(i, end= ' ')
    
'''

for i in nome:
    print(i, end= '')