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
        op = 1
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
        if op < 1 or op > 5:
            print('Ok!')

    def imprimir_dados(self):
        return f'NOME: {self.__nome}\nSOBRENOME: {self.__sobrenome}\nIDADE: {self.__idade}\nCPF: {self.__cpf}\nENDEREÇO: {self.__endereco}'

p1 = Pessoa('Pedro Henrique', 'Castoldi Bezerra', 22, '111.111.111.11', 'vc')

p2 = Pessoa('Juninho', 'Castoldi Bezerra', 3, '222.222.222.22', 'vc')

print(p1.imprimir_dados())
print()
print(p2.imprimir_dados())

p1.alterar_dados()
p2.alterar_dados()

print(p1.imprimir_dados())
print()
print(p2.imprimir_dados())