from ex25_13_variaveis import *

def inserir():
    while True:
        nome = str(input('NOME: '))

        print('Insira sua data de aniversário:')
        while True:
            try:
                dia = int(input('DIA: '))
                mes = int(input('MÊS: '))

                if dia < 1 or dia > 31:
                    raise ValueError
                elif mes < 1 or mes > 12:
                    raise ValueError
                else:
                    an = f'{dia}/{mes}'
                    break
            except ValueError:
                 print('ERRO. algo foi inserido de modo errado!.')

        while True:
            try:
                telefone = (input('TELEFONE: '))
                if len(telefone) != 11:
                    raise TypeError

                t = int(telefone)

                tel = f'({telefone[0:2]}){telefone[2]}{telefone[3:7]}-{telefone[7:]}'
                break
            except (TypeError, ValueError) as e:
                print(f'Algo deu errado! {e}')

        fun.append([nome, an, tel])

        op = str(input('Inserir mais funcionários? S- SIM | N- NÃO: '))
        if op in 'Nn':
            break