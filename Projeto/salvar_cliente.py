from cliente import Cliente
import jsonpickle

def salvar_cliente():
    with open('clientes.json', 'w', encoding='UTF-8') as cli:
        dados = jsonpickle.encode(Cliente.l_clientes)
        cli.write(dados)