"""
RECAPTULANDO:
    dic = {'Curso': 'Python', 'Gosto': 'de fazer exercícios'}
    print(dic.get('Curso')) # N dá se colocar chave q n existe erro (valor None)
    print(dic['Gosto']) # Dá erro se colocar chave q n existe

Default Dict -> Ao criar um dicionário, utilizando o Default Dict, nos informamos um valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre quando n houver um valor definido.
Caso tente acessar uma chave q n existe, a chave será criada com o nome digitado e o valor default será colocado na mesma.

OBS: Lambdas são funções sem nome, q podem ou n receber parâmetro de entrada e retornar valores.
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario.update({'MK11': 'Mortal Kombat R$399'}) # Se colocar dicionario = {'MK11': 'Mortal Kombat R$399'} o defaultdict n funciona!
n = str(input('O que procura: '))
dicionario[n]
print(dicionario) # Se a chave n for "MK11", irá ser criada uma nova chave com o nome digitado e o valor será 0.
