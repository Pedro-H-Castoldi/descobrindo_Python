class Televisao:

    canais = 30
    v_max = 50

    def __init__(self):
        self.__volume = 25
        self.__canal = 1


class Controle:
    def __init__(self, controle_tv):
        self.__controle_tv = controle_tv

    def aumentar_v(self):
        if self.__controle_tv._Televisao__volume < Televisao.v_max:
            self.__controle_tv._Televisao__volume += 1
            print(f'Aumentar volume: {self.__controle_tv._Televisao__volume}.')

        else:
            print(f'Volume já no máximo: {Televisao.v_max}.')

    def diminuir_v(self):
        if self.__controle_tv._Televisao__volume > 0:
            self.__controle_tv._Televisao__volume -= 1
            print(f'Diminuir volume: {self.__controle_tv._Televisao__volume}.')

        else:
            print('Volume já no minimo: 0.')

    def canal_f(self):
        if self.__controle_tv._Televisao__canal < Televisao.canais:
            self.__controle_tv._Televisao__canal += 1
            print(f'Canal: {self.__controle_tv._Televisao__canal}.')

        else:
            self.__controle_tv._Televisao__canal = 1
            print('Canal: 1')

    def canal_t(self):
        if self.__controle_tv._Televisao__canal > 0:
            self.__controle_tv._Televisao__canal -= 1

            if self.__controle_tv._Televisao__canal == 0:
                self.__controle_tv._Televisao__canal = Televisao.canais
                print(f'Canal: {self.__controle_tv._Televisao__canal}.')

            else:
                print(f'Canal: {self.__controle_tv._Televisao__canal}.')

    def escolha(self, numero):
        if numero > 0 and numero <= Televisao.canais:
            self.__controle_tv._Televisao__canal = numero
            print(f'Canal: {self.__controle_tv._Televisao__canal}.')

        else:
            print('Canal não existe.')

tv = Televisao()
remoto = Controle(tv)

def menu():
    while True:
        op = int(input('1- Aumentar volume | 2- Diminuir volume | 3- Mudar canal frente | 4- Mudar canal trás | 5- Escolha o canal | 6- Desligar TV: '))
        if op == 1:
            remoto.aumentar_v()

        elif op == 2:
            remoto.diminuir_v()

        elif op == 3:
            remoto.canal_f()

        elif op == 4:
            remoto.canal_t()
        
        elif op == 5:
            numero = int(input('Insira o canal: '))
            remoto.escolha(numero)

        else:
            print('Desligando. Até mais.')
            break

menu()