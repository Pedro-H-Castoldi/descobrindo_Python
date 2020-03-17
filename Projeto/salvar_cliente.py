from cliente import Cliente

def salvar_cliente():
    with open('clientes.txt', 'w+', encoding='UTF-8') as cli:
        for cliente in Cliente.l_clientes:
            cli.write(f'\n{cliente.id}--{cliente.nome}--{cliente.idade}--{cliente.cpf}--{cliente.endereco}--{cliente.devendo}\n')