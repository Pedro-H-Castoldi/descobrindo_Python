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
                del pessoa._Pessoa__nome

    def buscar_pessoa(self, nome):
        for pessoa in self.__pessoas:
            if(nome == pessoa._Pessoa__nome.split(' ')[0]):
                print(f'ID: {pessoa._Pessoa__id}\nNOME: {pessoa._Pessoa__nome}\nIDADE: {pessoa._Pessoa__idade}\nALTURA: {pessoa._Pessoa__altura}')

p1 = Pessoa("Maria", 26, 1.67)
p2 = Pessoa("Mecias", 45, 1.90)
p3 = Pessoa("Bruno", 27, 1.88)
p4 = Pessoa("Maria Alves", 17, 1.55)
p5 = Pessoa("Luiza Maria", 87, 1.52)

agenda_contatos = Agenda()
agenda_contatos.add_pessoa(p1)
agenda_contatos.add_pessoa(p2)
agenda_contatos.add_pessoa(p3)
agenda_contatos.add_pessoa(p4)
agenda_contatos.add_pessoa(p5)


#agenda_contatos.remover_pessoa('Mecias')
agenda_contatos.buscar_pessoa('Mecias')

print('teste')