"""
Manipulando Data e Hora

Python tem um módulo biult-in (integrado), dessa forma é possível trabalhar com data e hora,
esse módulo é o datetime.


import datetime

print(datetime.MAXYEAR) # Máximo tempo suportado.

print(datetime.MINYEAR) # Menor tempo suportado.

# Retornar data e hora corrente
print(datetime.datetime.now()) # 2020-04-06 10:32:40.589137 BR: 06-04-2020

# datetime.datetime.now() - (year, month, day, hour, minute, second, microsecond).
print(repr(datetime.datetime.now()))

# replace() para fazer alteração na data
agora = datetime.datetime.now()

print(agora) # Antes.
agora = agora.replace(hour= 15, minute= 0, second= 0, microsecond= 0)
print(agora) # depois.

"""

import datetime

# Criando data
data = datetime.datetime(2022, 9, 24)
print(type(data)) # Note q a data tem seu próprio timo: class 'dattime.datetime'.
print(data)

# Tranformar em data a 'str' q o usuário informa
nascimento = str(input('Informe sua data de nascimento (dd/mm/yyyy): '))
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(type(nascimento))
print(nascimento)

# Acesso individual dos elementos de data e hora
print(nascimento.year)
print(nascimento.month)
print(nascimento.day)
print(nascimento.hour)
print(nascimento.minute)
print(nascimento.second)
print(nascimento.microsecond)

print(dir(nascimento))