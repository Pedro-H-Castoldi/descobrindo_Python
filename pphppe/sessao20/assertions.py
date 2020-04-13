"""
Assertions (afirmações/checagens/questionamentos)

Em Python, utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' para checar se uma expressão é válida ou n.
Se a expressão for verdadeira, retorna None, senão, levanta um erro do tipo AssertionError.

# OBS:
    - Nós podemos especificar, opicionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada;
    - A palavra reservada assert pode ser usada em qualquer função ou código nosso (n precisa ser utilizada apenas em testes).
"""
def somente_numeros_positivos(n1, n2):
    assert n1 > 0 and n2 > 0, 'ERRO: os números devem ser positivos.'
    return n1, n2

#print(somente_numeros_positivos(6, -8))

def comer_fast_food(comida):
    assert comida in ['pizza', 'pastel', 'coxinha', 'enroladinho'], 'A comida deve ser fast food.'
    return f'comendo {comida}.'

print(comer_fast_food('cenoura'))

# CUIDADO: Ao utilizar o assert, se executarmos um programa Python com o parâmetro -O, todas as restrições serão desconsideradas. Isso pode ser muito ruim,
#já que dá acesso a algo q normalmente n deveria dar, por exemplo, funções q estão restritas apenas para administradores,
#podem ter acesso por usuários comuns, podendo trazer sérios problemas para o sistema.
