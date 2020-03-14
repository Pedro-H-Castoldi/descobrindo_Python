class Cliente:

    l_clientes = []
    cont = 0

    def __init__(self, nome, idade, cpf, endereco):
        self.__id = Cliente.cont + 1
        self.__nome = nome.title().strip()
        self.__idade = idade
        self.__cpf = cpf.strip()
        self.__endereco = endereco.title().strip()
        Cliente.cont = self.__id

    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf
    @property
    def endereco(self):
        return self.__endereco

    def add(self):
        Cliente.l_clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        for cliente in Cliente.l_clientes:
            print(f'Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco}')

    @classmethod
    def listar_clientes_nome(cls, nome):
        encontrado = False
        for cliente in Cliente.l_clientes:
            if(cliente.nome == nome):
                encontrado = True
                print(f'Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco}')
                return cliente
        if not encontrado:
            print('Cliente não encontrado.')
            return False


"""
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
"""