produtos = {1:['Arroz', 5], 2: ['Feijao', 3], 3: ['Carne de boi', 10], 4: ['Batata', 0.5]}

clientes = {}

devendo = {}

carrinho = {}
comprado = []


def cadastrarCliente():
    while True:
        id = int(input('ID: '))
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cpf = str(input('CPF: '))
        endereco = str(input('Endereço: '))
        clientes.update({id: [nome.title(), idade, cpf, endereco]})

        op = str(input('Cadastrar outro cliente? 1- S 2- N '))
        if op in 'Nn':
            print(clientes)
            break
    menu()


def compras():
    cliente = idc = idp = idcompra = erro = teve = 0

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
                    print(f'i: {idp} j: {j}')
                    comprado.append(f'{produtos[idp][0]} R${produtos[idp][1]}')
                    erro = teve = 1
                    break
            if erro == 0:
                print('ID do produto não se encontra no sistema.')
            erro = 0
        else:
            print('ID do cliente não se encontra no sistema.')
            break
        op = str(input('Continuar comprando? S / N: '))
        if op in 'Nn':
            break

    idcompra = 11 + idc
    carrinho.update({idcompra: [cliente, clientes[cliente], comprado]})

    if teve > 0:
        op = str(input('Compra fiada?: '))
        if op in 'Ss':
            devendo.update(carrinho) # Corrigir {}
            print(devendo)
    else:
        print('Fim.')

def devedores():
    print('ID Compra         ID Cliente         Nome            Produto(s)')
    for i in devendo:
        print(f'{i}          {devendo[i][0]}    {devendo[i][1][0]}            {devendo[i][2]}')




def menu():
    while True:
        op = int(input('Escola uma opção: 1- Cadastrar Cliente, 2- Devendo, 3- Compras, 4- Pesquisar Produto, 5- Listar clientes,  - Encerrar: '))

        if op == 1:
            cadastrarCliente()
        elif op == 2:
            devedores()
        elif op == 3:
            compras()
        elif op == 4:
            pesquisarProduto()
        elif op == 5:
            print(clientes)
        else:
            break

menu()