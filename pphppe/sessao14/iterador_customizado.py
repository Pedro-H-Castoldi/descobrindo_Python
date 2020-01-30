class Contador:
    # Fazendo construtor da classe
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self): # Transforma a classe Contador em iterator
        return self

    def __next__(self): # Faz o processo da função next() de retornar um caractere por vez do iterator
        if self.menor < self.maior:
            n = self.menor # n = 1
            self.menor = self.menor + 1 # menor = menor + 1 (2) # Isso até chegar ao 5, passando de 1 por 1 nos caracteres
            return n
        raise StopIteration # se menor > maior esse erro faz parar, n deixando o loop em um modo infinito

nn = Contador(1, 6)

print(next(nn)) # 1
print(next(nn)) # 2

# Outra forma
for nnn in Contador(1, 6): # Substitui o range com a classe Contador já tranformada em iterator
    print(nnn)