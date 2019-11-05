"""
Funções com parâmetros (de entrada)
    - Funções q recebem entrada(s) para serem processadas dentro da mesma;

    - Se pensarmos em um programa qualquer, geralmente se tem:
        ENTRADA -> PROCESSAMENTO -> SAIDA

    - Existem funções q:
        . N possuem entrada;
        . N possuem saida;
        . Possuem saida mas n possuem entrada;
        . N possuem saida mas possuem entrada;
        . Possuem entrada e saida.



# Função q recebe parâmetro
def quadrado(numero):
    return numero ** 2

while True:
    n = int(input('Digite o número pra elevar ao quadrado: '))
    print(quadrado(n))
    res = str(input('Continuar? S/N: '))
    if res in 'Nn':
        break
print('Finalizado!')



# Funções com mais de 1 parâmetro
def media_if(n1, n2, n3, n4):
    N1 = ((n1 + n2)/2) * 2
    N2 = ((n3 + n4)/2) * 3
    m = (N1 + N2)/5
    return m

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

if media_if(n1, n2, n3, n4) >= 7:
    print(f'Aprovado média {media_if(n1, n2, n3, n4):.2f}.')
elif media_if(n1, n2, n3, n4) >= 3 and media_if(n1, n2, n3, n4) < 7:
    print(f'Prova final. Média {media_if(n1, n2, n3, n4):.2f}.')
else:
    print(f'REPROVADO. Média {media_if(n1, n2, n3, n4):.2f}.')



# Nomeando parâmetros - é viável colocar nomes indicativos nos parâmetros para o bom entendimento do código.
# EX def nome_completo(str1, str2) n é recomendado, o certo seria: def nome_completo(nome, sobrenome).
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}.'

print(nome_completo('Wallyson', 'Leite'))

# Diferença entre parâmetro e argumento
    # Parâmetros são variáveis declaradas na definição de uma função;
    # argumentos dados passados durante a execução de uma função.

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos utilizar em qualquer ordem
# (se colocarmos o nobrenome astes do nome, ainda assim será retornado primeiro o nome e depois o sobrenome)
print(nome_completo(sobrenome= 'Leite', nome= 'Wallyson'))

"""

