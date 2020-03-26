class Cliente:

    l_clientes = []
    cont = 0

    def __init__(self, nome, idade, cpf, endereco):
        self.__id = Cliente.cont + 1
        self.__nome = nome.title().strip()
        self.__idade = idade
        self.__cpf = cpf.strip()
        self.__endereco = endereco.title().strip()
        self.__estado = False
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
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, novo):
        self.__estado = bool(novo)

    def add(self):
        Cliente.l_clientes.append(self)

    @classmethod
    def cliente_devendo(cls, cli):
        for cliente in Cliente.l_clientes:
            if cli.id == cliente.id:
                cliente.estado = True
    @classmethod
    def listar_clientes(cls):
        for cliente in Cliente.l_clientes:
            print(f'ID Cliente: {cliente.id} - Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco} - Status: {cliente.estado}')

    @classmethod
    def listar_clientes_nome(cls, nome):
        encontrado = False
        for cliente in Cliente.l_clientes:
            if(cliente.nome == nome):
                encontrado = True
                print(f'ID Cliente: {cliente.id} - Nome: {cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf} - Endereço: {cliente.endereco} - Status: {cliente.estado}')
                return cliente
        if not encontrado:
            print('Cliente não encontrado.')
            return False