"""
Conhecidaas por expressões lambdas ou simplesmente lambdas. São funções sem nome, ou seja, funções anônimas.

# Função Python comum
def soma(x):
    return x + 2

print(soma(3))
print(soma(10))

# Utilizando lambda
lambda x: x + 2

# Colocar a lambda em uma variável para então chama-la
fun = lambda x: x + 2

print(fun(3))
print(fun(10))


nome_completo = lambda nome, sobrenome: nome.title().strip() + ' ' + sobrenome.title().strip()

print(nome_completo('  pedrO', 'castoldi    '))

# Em Python podemos ter nenhuma ou várias entradas, em lambda tbm.
love = lambda: 'Espero que em algum dia eu encontre um amor verdadeiro..'
um = lambda x: x + 1
dois = lambda x, y: (x + 2) * (y + 3)
tres = lambda x, y, z: x + 1 + y + 3 + z + 2

# nn = lambda n1, n2, n3, ... , nn: n1 + n2 + n3 + ... + nn

print(love())
print(um(2))
print(dois(6, 8))
print(tres(4, 3, 2))

# Dará erro se for botado mais argumento do que parâmetros esperados



# Ordenando nomes pelo sobrenome utilizando a função sort() e lambda
nomes = ['Pedro Henrique Castoldi Bezerra', 'Ser Terreno', 'Cicero Darlison Ferreira da Silva', 'Pessoa Sobrenome', 'Bruno Costa']
# Pega o nome(nome, n. meio, sobrenome) e separa por espaços (split(' ')), aí pega o último nome (-1) deixando-o minusculo(lower)(para q fiquem todos iguais)
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # n entendi o pq do lower()
print(nomes)
"""
# Função quadrática
def f_qua(a, b, c):
    return lambda x: a * x ** 2 + b + x + c # A função f_qua retorna uma lambda

n = f_qua(1, 2, 3) # Definindo os argumentos da f_qua

print(n(0)) # Definindo o valor do parâmetro x da lambda
print(n(7))

# Inserindo os argumentos da f_qua e da lambda de uma só vez
print(f_qua(1, 2, 3)(0))