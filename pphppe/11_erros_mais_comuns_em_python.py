"""
SyntaxError -> O corre quando algo no código não é reconhecido como parte da linguagem.
    EX:
        A)
            def funcao: # SyntaxError: é necessário os parentes para definir uma função.
                print('Ser terreno')

        B)
            def = 1
            None = 43

NameError-> Ocorre quando uma função ou variável não foi definida.
    EX:
        print(pp)

        pp()

        a = 9
        if a < 7:
            menor7 = 'É menor que 7.'
        print(menor7) # Se a for maior q 7 a variável "menor7" nunca será declarada, gerando assim o NameError

TypeError-> Ocorre quando uma função/operação/ação é dada a um tipo não compatível.
    EX:
        print(len(3)) # Erro pois um int n é compatível com a função len().

        print('Sindel' + 6) # N se soma string com numericos.

IndexError-> Ocorre quando tentamos acessar um indice em uma lista ou outro tipo de dado de forma inválida.
    EX:
        lista = ['Juninho']
        print(lista[1]) # Erro. Pois a lista só tem um elemento (0)

ValueError-> O corre quando uma função/operação built-in (integrada) recebe um argumento do tipo correto mas valor inapropriado.
    EX:
        print(int('asas')) # Erro. A função int() esperava uma string, no entanto, a string 'asas' n pode ser convertida para um inteiro.

KeyError-> Ocorre quando buscamos acessar uma chave em um dic q n existe.
    EX:
        dicionario = {}
        print(dicionario['nome']) # Erro. Pois a chave 'nome' n existe.

AtributeError-> Ocorre quando uma variável não tem um atributo/função.
    EX:
        tupla = 54, 4, 43, 2, 3
        print(tupla.sort()) # Erro. Pois a Função sort() n foi feita para tuplas e sim para listas.

IdentationError-> Ocorre quando n é respeitada a identação do Python (4 espaços).
    EX:
        def fun():
        print('FUNNN') # Erro. Pois falta os 4 espaços.


OBS:
    Exceptions e erros são sinônimos na programação;
    Importante ler e entender a saida de erro.

"""

