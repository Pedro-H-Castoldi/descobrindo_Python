def salvar_cliente(cliente):
    with open('clientes.txt', 'a+', encoding='UTF-8') as cli:
        cli.write(f'\n{cliente.id}--{cliente.nome}--{cliente.idade}--{cliente.cpf}--{cliente.endereco}--{cliente.devendo}\n')