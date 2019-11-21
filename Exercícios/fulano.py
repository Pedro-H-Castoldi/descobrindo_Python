def letraPorLetra(nome):
    if nome in ' ' * 1000:
        print('ERRO!')
    else:
        nome = nome.title()
        for i in range(len(nome)):
            print(nome[i])


def nomeEscada(nome):
    if nome in ' ' * 1000:
        print('ERRO!')
    else:
        l = 1
        nome = nome.title()

        for i in range(len(nome)):
            for j in range(l):
                print(nome[j], end='')
            print()
            l += 1

def escadaInversa(nome):
    if nome in ' ' * 1000:
        print('ERRO!')
    else:
        nome = nome.title()
        l = len(nome)

        for i in range(len(nome)):
            for j in range(l):
                print(nome[j], end='')
            print()
            l -= 1

nome = str(input('Nome: '))

#letraPorLetra(nome)

#nomeEscada(nome)

escadaInversa(nome)