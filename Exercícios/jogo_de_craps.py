from random import randrange

def crapsGame():
    i = 0
    dda = 0
    while True:
        dado1 = randrange(1, 7)
        dados2 = randrange(1, 7)
        dd = dado1 + dados2

        print(f'Os dados são: {dado1} e {dados2} = {dd}')

        if i == 0 and dd == 7 or dd == 11:
            return f'O valor dos dados é {dd}: Natural.\nParabéns você ganhou!!!!'

        elif i == 0 and dd == 2 or dd == 3 or dd == 12:
            return f'O valor dos dados é {dd}: Craps!\nQue pena, você perdeu..'

        elif i == 0 and dd >= 4 and dd <= 10:
            dda = dd
            i = 1
            print(f'Nova jogada! você terá que repetir o valor: {dda}')

        elif dd == dda:
            return f'Você conseguiu! repetiur o valor {dda}!\nVocê venceu!!!'

print(crapsGame())