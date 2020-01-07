idade = int(input('Por gentileza informe sua idade '))

if idade < 18:
    print(f'Você tem {idade}, logo é menor de idade!')
elif idade == 18:
    print('Você possui 18 anos') # Com o elif bota a condição (idade == 18), diferente do else q n precisa
else:
    print(f'Você possui {idade} anos, não é de menor')

