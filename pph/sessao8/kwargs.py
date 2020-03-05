"""
**kwargs
Pode ser chamado de **qualquer_coisa desde q tenha os 2 asteriscos, mas por convenção chamamos esse parâmetro de **kwargs

- É só mais um parâmetro, mas diferentemente do *args q bota os argumentos em uma túpla, o **kwargs exige q utilizemos parâmetros nomeados,
e transforma esses parâmetros extras em um dicionário.



# EX
def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f'A cor favorita de {nome.title()} é {cor}.')

cores_favoritas(pedro='roxo', wallyson='verde', darlison='vermelho')
cores_favoritas() # N ocasionará erro n botar nenhum argumento, pois n é obrigatório
cores_favoritas(juliana='amarelo')



def identificar_user(**kwargs):
    if 'usuário' in kwargs and kwargs['usuário'] == 'pedro' or 'usuário' in kwargs and kwargs['usuário'] == 'Pedro':
        return f"Olá Pedro! Seja bem-vindo."
    elif 'usuário' in kwargs:
        return f"Seja bem-vindo {kwargs['usuário']}!"
    return 'Não conseguimos encontrar sua identificação.. Tenten logar novamente.'

print(identificar_user(usuário='Pedro'))
print(identificar_user(usuário='boruto'))
print(identificar_user())



# Em nossas funções podemos ter os parâmetros (NESSA ORDEM!):
    # parâmetros oprigatórios;
    # *args;
    # parâmetro default (não obrigatório);
    # **kwargs.

def tipos_de_parametros(nome, *args, solteiro=False, **kwargs):
    if solteiro:
        return f'{nome} | {args} | solteiro | {kwargs}'
    return f'{nome} | {args} | casado | {kwargs}'

print(tipos_de_parametros('Pedro', 24, 9, 1996, sobrenome='Castoldi', sobrenome2='Bezerra'))

# Se n seguir essa sequência certos parâmetros ficarão sem argumentos e/ou argumentos entrarão em parâmetros indesejados
#EX
def tipos_de_parametros_erro(nome, nacionalidade='BR', *args, **kwargs):
    return f'{nome} | {nacionalidade} | {args} | {kwargs}'

# Nesse exemplo foi tentado colocar no 'args' os numeros (24, 9, 1996), mas isso n ocorreu! o número 24 foi para nacionalidade!
# Isso ocorre pois como nacionalidade vem antes de *args, o primeiro número vai para nacionalidade e o resto para *args.
# Se *args viesse antes, todos os números iriam para esse parâmetro, e nada iria para nacionalidade, já q ele é default.
# Isso pq o próximo argumento é um elemento de dicionário (q possui chave e valor), logo, n irá para o parâmetro 'nacionalidade',
# deixando-o com o argumento padrão, q é o 'BR'.
print(tipos_de_parametros_erro('Pedro', 24, 9, 1996, sobrenome='Castoldi', sobrenome2='Bezerra'))
"""

# Desempacotar com **kwargs
def soma_pacote(a, b, c):
    return a + b + c

print(soma_pacote(1, 2, 3))

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

dicionario = dict(a= 1, b= 2, c= 3) # Para o desempacotamento as chaves precisam ser iguais aos parâmetros

# Desempacotando como vimos na aula passada com *args
#print(soma_pacote(lista)) # Dará um erro, pois o pacote n foi desempacotado
print(soma_pacote(*lista))
print(soma_pacote(*tupla))
print(soma_pacote(*conjunto))

print(soma_pacote(*dicionario)) # N funcionará pois assim o parâmetro só irá receber a b c como argumento
print(soma_pacote(a=1, b=2, c=3)) # Isso n é desempacotar, nem mesmo se está usando o pacote 'dicionario'
print(soma_pacote(**dicionario)) # Dessa forma será feito o desempacotamento do dicionário, no entando, as chaves precisam ser iguais aos parâmetros

# Se na função botassemos um parâmetro **kwargs (def soma_pacote(a, b, c, **kwargs)) seria possível colocar mais argumentos, exemplo:
# print(soma_pacote(**dicionario, lang='pt-br'))