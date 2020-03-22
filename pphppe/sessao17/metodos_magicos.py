"""
POO - Métodos Mágicos

São todos os métodos que utilizam dunder.

# Dunder init -> __init__():
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

Dunder -> Double Underscore.

# Dunder repr -> Representação do objeto (em vez de retornar a localização da memória, é possível representar o objeto):
    def __repr__(self):
    return f'Livro {self.__titulo} escrito por {self.__autor}' # Dessa forma i´ra retornar essa representação em vez do endereço de memória.

"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'Livro {self.__titulo} escrito por {self.__autor}' # Dessa forma i´ra retornar essa representação em vez do endereço de memória.

    def __str__(self):
        return self.__titulo # Faz a mesma coisa q o__repr__ mas retorna uma string. Tem prioridade sobre o __repr__, ou seja, é executado e o __repr__ n.

    def __len__(self):
        return self.__paginas # Isso faz com q o tamanho da classe Livro seja do tamnho da quantidade de páginas. (no meu n funciona com strings)

    #def __del__(self):
     #   print('Um objeto do tipo Livro foi excluido.') # faz com q quando um objeto for excluído aparecer essa mensagem.

    def __add__(self, outro):
        return f'{self} - {outro}' # Faz a junção da representação de mais de 1 objeto

    def __mul__(self, outro): # Faz a multiplicação da representação de um objeto por um número.
        if isinstance(outro, int): # Se a instância 'outro' for do tipo int
            msg = ''
            for i in range(outro):
                msg += '  ' + str(self)
            return msg
        return 'Não posso multiplicar..'


livro1 = Livro('Tiro no Coração', 'Gilmore', 500)
livro2 = Livro('Harry Poteer', 'Não sei', 344)

print(livro1)
print(len(livro1))
#del livro1 # Sempre q o programa encerrar a mensagem q um objeto foi excluído aparecerá, pois quando o programa encerra os objetos são deletados da memória.

print(livro1 + livro2)
print(livro2 * 5)