class Pessoa:
    cont = 0
    def __init__(self,nome, sobrenome, idade, cpf, endereco):
        self.__id = Pessoa.cont
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__cpf = cpf
        self.__endereco = endereco
        Pessoa.cont += 1

    def alterar_dados(self):
        op = int(input('1- NOME | 2- SOBRENOME | 3- IDADE | 4- CPF | 5- ENDEREÇO | 0- SAIR: '))
        if op == 1:
            muda = str(input(f'{self.__nome}: '))
            self.__nome = muda
        if op == 2:
            muda = str(input(f'{self.sobrenome}: '))
            self.__sobrenome = muda
        if op == 3:
            muda = int(input(f'{self.__idade}: '))
            self.__idade = muda
        if op == 4:
            muda = str(input(f'{self.__cpf}: '))
            self.__cpf = muda
        if op == 5:
            muda = str(input(f'{self.endereco}: '))
            self.__endereco = muda
        else:
            print('Ok!')

    def imprimir_dados(self):
        return f'NOME: {self.__nome}\nSOBRENOME: {self.__sobrenome}\nIDADE: {self.__idade}\nCPF: {self.__cpf}\nENDEREÇO: {self.__endereco}'


def menu():
    op = int(input('1- Adicionar usuário | 2- Editar | 3- Imprimir dados'))

    if op == 1:
        nome =