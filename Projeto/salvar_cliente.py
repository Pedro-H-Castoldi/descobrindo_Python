import cliente
import jsonpickle

def salvar_cliente():
    with open('clientes.json', 'w', encoding='UTF-8') as cli:
        dados = jsonpickle.encode(cliente.Cliente.l_clientes)
        cli.write(dados)