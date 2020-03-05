class Elevador:

    pessoa = 0
    andar = 0

    def __init__(self, total_andares, capacidade):
        self.__total_andares = total_andares
        self.__capacidade = capacidade

    def inicia(self, andar):
        if Elevador.pessoa > 0:
            if self.__total_andares >= andar and andar != 0:
                Elevador.andar = andar
                print(f'Indo para o andar {Elevador.andar}.')

            elif andar == 0:
                self.descer()

            else:
                print('Esse andar não existe.')
        else:
            print('Não existe ninguém no elevador para iniciar.')

    def entrar(self):
        if self.__capacidade > Elevador.pessoa:
            Elevador.pessoa += 1
            print('Pessoa entrando no elevador.')
            print(f'Total de pessoas: {Elevador.pessoa}')
        else:
            print('ENTRADA NÃO AUTORIZADA!')
            print('Elevador com pessoas demais. O máximo suportado são 8 pessoas.')
            print(f'Total de pessoas: {Elevador.pessoa}')

    def sair(self):
        if Elevador.pessoa > 0:
            Elevador.pessoa -= 1
            print('Pessoa saindo do elevador.')
            print(f'Total de pessoas: {Elevador.pessoa}')

    def descer(self):
        if Elevador.andar != 0:
            print('Elevador descendo para o térreo.')
            Elevador.andar = 0
        else:
            print('Elevador está no térreo.')

    @classmethod
    def status(cls):
        return Elevador.andar

elevador1 = Elevador(10, 8)

def sistema_elevador():
    while True:
        op = int(input('1- Entrar | 2- Iniciar | 3- Sair | 4- Descer | 5- Sair: '))
        if op == 1:
            elevador1.entrar()

        elif op == 2:
            print(f'Status: ANDAR {elevador1.status()}')
            andar = int(input('Insira o andar de destino (1 à 10): '))
            elevador1.inicia(andar)

        elif op == 3:
            elevador1.sair()

        elif op == 4:
            elevador1.descer()

        else:
            print('Fim.')
            break

sistema_elevador()