from variaveis_g import *

def compras():
    cliente = idc = idp = idcompra = erro = teve = 0
    opid = '*'

    idc = int(input('Insira o ID do cliente: '))

    while True:
        for i in clientes:
             if i == idc:
                 cliente = idc
                 break

        if cliente > 0:
            idp = int(input('Insira o ID do produto: '))
            for j in produtos:
                if j == idp:
                    comprado.append(f'{produtos[idp][0]} R${produtos[idp][1]}')
                    erro = teve = 1
                    break

            if erro == 0:
                print('ID do produto não se encontra no sistema.')

            erro = 0


        else:
            print('ID do cliente não se encontra no sistema.')
            opid = str(input('Tentar novamente? S / N: '))
            if opid in 'Nn':
                return 0
            else:
                idc = int(input('Insira o ID do cliente: '))

        if opid == 's':
            opid = '*'
        else:
            op = str(input('Continuar comprando? S / N: '))
            if op in 'Nn':
                break

    idcompra = 1 + idc
    c = comprado
    print(type(c))
    carrinho.update({idcompra: [cliente, clientes[cliente], comprado]})

    if teve > 0:
        op = str(input('Compra fiada?: '))
        if op in 'Ss':
            clientes[cliente][4] = False
            devendo.update(carrinho) # Corrigir {}
            print(devendo)
    else:
        print('Fim.')