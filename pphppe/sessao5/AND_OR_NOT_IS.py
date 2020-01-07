"""
Operadores unários: NOT;

Operadores binários: AND, OR, IS;

O NOT inverte o valor, ou seja, tudo q for True é False e tudo q for False vira true.
"""

ativo = True
logado = True

if ativo == True and logado == True:
    print('Seja bem vindo!')
else:
    print('Logue no sistema!')

if not ativo: #Se o ativo n estiver ativo (false) será imprimida essa condição
    print('Logue no sistema!!!')
else:
    print('Bem vindo!!!')

if ativo: #Sempre essa condição será ativada com True
    print('Bem-vindo!!!')
else: #E essa com o False
    print('Logue no sistema!!!')

#ativo é true? (se for True ele falará verdade, ou seja, True)
print(ativo is True)