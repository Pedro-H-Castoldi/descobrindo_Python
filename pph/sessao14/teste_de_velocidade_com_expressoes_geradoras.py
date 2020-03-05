"""
Generators
def numeros():
    for i in range(5, 11):
        yield i

gene = numeros() # Se botar print(next(numedos()) sempre irá aparecer o primeiro número retornado (5), mesmo se chame outras vezes

# Passando a função para uma variável (gene()), cada vez q a chama, retorna o próximo número.
print(gene) # Generator
print(next(gene)) # 5
print(next(gene)) # 6

# Generator Expression

gene2 = (gg for gg in range(5, 11))

print(gene2) # Generation Expression
print(next(gene2)) # 5
print(next(gene2)) # 6


"""

# Teste de valocidade
import time

# Generator Expression
temp_g = time.time()
print(sum(gg for gg in range(10000000)))
temp_gene = time.time() - temp_g

# List Comprehension
temp_l = time.time()
print(sum([ll for ll in range(10000000)]))
temp_list = time.time() - temp_l

print(f'O tempo de execução do Generator Expression foi: {temp_gene}.')
print(f'O tempo de execução do List Comprehension foi .: {temp_list}.')