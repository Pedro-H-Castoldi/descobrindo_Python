"""
FUNÇÕES
    - São pequenas partes de código que realizam funções especificas;
    - Pode ou n receber entradas de dados ou retornar uma saida de dados;
    - Muito úteis para executar procedimentos similares por repetidas vezes.

    OBS: Se fizer uma função q realiza várias tarefas dentro dela,
    é bom fazer uma verificação, para que a função seja simplificada.

    Já foram utilizadas várias funções desde o inicio do curso:
        - print()
        - len()
        - max()
        - min()
        - count()
        - * entre outras.

    A Forma geral de definir funções em Python é:
        def nome_da_função(parametro_de_entrada):
            bloco_da_função

    onde:
        nome_da_função -> SEMPRE com letras minúsculas, se for um nome composto, separa-se por underline (snake case) '_';

        parametros_de_entrada -> Opicional, se tiver mais de um, a separação é feita por vírgula, podendo ser opcional ou n;

        bloco_da_função -> tbm chamado de corpo da função ou implementação, é onde o processamento da função acontece.
        Nesse bloco, pode ter ou não retorno da função.


    OBS: Veja q para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que estamos definindo uma função.
    Tbm  abrimos o bloco de código com o já conhecido dois pontos ':', que é utilizado em Python para definir blocos.


#EX 1
def diz_oi():
    print('OI! Sou sua primeira função.')

# Chamando função (é necessário colocar parênteses no final)
diz_oi()

OBS:
    1- Dentro de uma função é possível utilizar outras funções;
    2- A função 'diz_oi()' só executa uma tarefa;
    3- Essa função n retorna nada;
    4- Ela n possui parâmetro de entrada.

#EX 2
def cantar_parabens(nome):
    print(f'Parabéns pra você!\nNessa data querida!!\nMuitas felicidades!!!\nMuitos anos de vida!!!!\nParabéns {nome.title()}!!!!!')

nome = str(input('Quem é o aniversáriante???: '))
cantar_parabens(nome)

Para repetir a função 5x
for i in range(5):
    cantar_parabens(nome)
"""

# Recursividade
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

nu = int(input('Digite um número para saber o fatorial: '))
fatorial(nu)

print(f'O fatorial de {nu} é: {fatorial(nu)}')

# Em Python é possível inclusive criar váriaveis do tipo de uma função e então executar essa função pela variável
def cor_da_casa():
    print('Casa amarela.')

residência = cor_da_casa
residência()