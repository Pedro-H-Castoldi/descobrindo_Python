from variaveis_g import *

def cadastrarCliente():
    while True:
        id = int(input('ID: '))
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cpf = str(input('CPF: '))
        endereco = str(input('Endereço: '))
        status = True
        clientes.update({id: [nome.title(), idade, cpf, endereco, status]})

        op = str(input('Cadastrar outro cliente? 1- S 2- N '))
        if op in 'Nn':
            print(clientes)
            break