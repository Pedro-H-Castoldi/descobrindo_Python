"""
Métodos com Data e Hora

import datetime

# Com o método now() é possível trabalhar com o timezone (fuso horário), já com o today() n.
agora = datetime.datetime.now() # now == agora.
print(agora)

hoje = datetime.datetime.today() # today == hoje.
print(hoje)


# EX: Manutenção para meia-noite (usando o método combine())

# Com isso a manutenção será feita no próximo dia da data de hoje ás 0h
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time()) # o time() == 0h 0s 0ms
print(type(manutencao))
print(repr(manutencao))
print(manutencao)


# Encontrar o dia da semana - weekday()
# Os dias da semana são representados por números:
   # 0 - Segunda (monday);
   # 1 - Terça (tuesday);
   # 2 - Quarta (wednesday);
   # 3 - Quinta (thursday);
   # 4 - Sexta (friday);
   # 5 - Sábado (saturday);
   # 6 - Domingo (sunday).

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(manutencao.weekday()) # Hoje é segundo, logo um dia depois é terça, desse modo o q será retornado será: 1 (terça).

# Descobrir em qual dia da semana nasceu

nascimento = str(input('Insira sua data de nascimento dd/mm/yyyy: '))
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

if nascimento.weekday() == 0:
    print('Você nasceu em uma segunda-feira.')
elif nascimento.weekday() == 1:
    print('Você nasceu em uma terça-feira.')
elif nascimento.weekday() == 2:
    print('Você nasceu em uma quarta-feira.')
elif nascimento.weekday() == 3:
    print('Você nasceu em uma quinta-feira.')
elif nascimento.weekday() == 4:
    print('Você nasceu em uma sexta-feira.')
elif nascimento.weekday() == 5:
    print('Você nasceu em um sábado.')
elif nascimento.weekday() == 6:
    print('Você nasceu em um domingo.')

"""

import datetime

# Formatando data/hora com strftime() (String Format Time)
# Modelo BR: dd/mm/yyyy hora:minuto

agora = datetime.datetime.today()

formatado = agora.strftime('%d/%m/%Y') # Com %B no em vez de %m, mostra o mês pelo nome. %y em vez de %Y, mostra só 2 digitos (ex: 20), entre outros modos.

print(formatado)