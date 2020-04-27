"""
Podemos fazer do Python uma linguagem estaticamente tipada.


# No parâmetro nome após os ':' indica qual tipo de argumento a função aceitará,
# e após o '->' indica qual tipo de dado a mesma retornará.
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}.'


print(cumprimentar('Farid'))

"""

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    return f' {texto.title()} '.center(50, '#')

print(cabecalho('Python é minha linguagem'))
print(cabecalho('python é minha linguagem', False))


# OBS: Mesmo especificando os tipos dos parâmetros e retorno,
# o Python n apresenta erro se colocar um tipo diferente do especificado.

# Para o Python apresentar erro ao inserir um tipo inválido de variável ou retorno, usamos a extensão Mypy.
# O Mypy trabalha em conjunto com o type hinting.
# Para usar o mypy é necessário acessar o terminal. Exemplo: mypy arq.py