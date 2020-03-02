class Pessoa:
    cont = 0
    def __init__(self, nome, idade, altura):
        self.__id = Pessoa.cont + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

        Pessoa.cont = self.__id

class Agenda:
    def __init__(self):
        self.__pessoas = []

    def add_pessoa(self, pessoa):
        self.__pessoas.append(pessoa)

    def remover_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if(nome == pessoa._Pessoa__nome):
                pessoa._Pessoa__nome = ''

    def buscar_pessoa(self, nome):
        cont = 0
        for pessoa in self.__pessoas:
            cont += 1
            if (nome == pessoa._Pessoa__nome.split(' ')[0]):
                print(
                    f'Posição: {cont}\n'
                    f'ID: {pessoa._Pessoa__id}\n'
                    f'NOME: {pessoa._Pessoa__nome}\n'
                    f'IDADE: {pessoa._Pessoa__idade}\n'
                    f'ALTURA: {pessoa._Pessoa__altura}')
            print()

    def listar(self):
        cont = 0
        for pessoa in self.__pessoas:
            cont += 1
            if pessoa._Pessoa__nome != '':
                print(
                    f'Posição: {cont}\n'
                    f'ID: {pessoa._Pessoa__id}\n'
                    f'NOME: {pessoa._Pessoa__nome}\n'
                    f'IDADE: {pessoa._Pessoa__idade}\n'
                    f'ALTURA: {pessoa._Pessoa__altura}')
            print()

p1 = Pessoa("Maria", 26, 1.67)
p2 = Pessoa("Mecias", 45, 1.90)
p3 = Pessoa("Bruno", 27, 1.88)
p4 = Pessoa("Maria Alves", 17, 1.55)
p5 = Pessoa("Luiza Maria", 87, 1.52)
p6 = Pessoa("Gonsalves", 27, 1.88)

agenda_contatos = Agenda()
agenda_contatos.add_pessoa(p1)
agenda_contatos.add_pessoa(p2)
agenda_contatos.add_pessoa(p3)
agenda_contatos.add_pessoa(p4)
agenda_contatos.add_pessoa(p5)
agenda_contatos.add_pessoa(p6)


agenda_contatos.remover_pessoa('Mecias')
agenda_contatos.buscar_pessoa('Gonsalves')
agenda_contatos.listar()