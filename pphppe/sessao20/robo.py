class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome
    @property
    def bateria(self):
        return self.__bateria
    @bateria.setter
    def bateria(self, carga):
        self.__bateria = carga
    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.bateria = 100

    def dizer_nome(self):
        if self.bateria > 0:
            self.bateria = self.bateria - 1
            return f'Meu nome é {self.nome.upper()}.'
        return 'Descarregado. Carregue a bateria.'

    def aprender_algo(self, habilidade, custo):
        if self.bateria <= custo:
            self.bateria -= custo
            self.habilidades.append(habilidade)
            return f'Uau! Aprendi a {habilidade}!'
        return 'Bateria insufuciente.'
