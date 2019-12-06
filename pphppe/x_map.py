"""
Com o map é feito mapeamento de valores para função.

import math

def area(r):
    #Calcular área de um circulo com raio r
    return math.pi * (r ** 2)

print(area(2))

# E se por acaso o argumento para a função por uma lista?
raios = [2, 4, 6.6, 8]
areas = []

# Forma 1
areas.append([area(x) for x in raios])
print(areas)

# Forma 2 - Map
# O map é uma função q recebe 2 parâmetros: uma função, e um interável. Ele pegará número por número do interável e colocar na função. Retorna um map object
areas = map(area, raios)

print(areas) # Assim ele irá imprimir como se fosse print(type(areas)) retornando ela como um objeto tipo map
print(list(areas)) # Assim um converterá de map->list, aparecendo então os valores já passados pela função (pode ser convertido pra outros interáveis)
# print(list(map(area, raios))) # forma mais simplificada de impressão dos valores. Isso excluíria a linha 24.

# Forma 3 - Map com Lambda
areas = map(lambda r: math.pi * (r ** 2), raios)
print(list(areas))

print(list(map(lambda r: math.pi * (r ** 2), raios))) # Forma mais reduzida

# OBS: Após a primeira utilização do resultado de um map(), ele zerará.
"""

# Outro exemplo

cidade = [('Cedro', 44), ('Iguatu', 40), ('Campinas', 22)]

# Pegar as temperaturas das cidades em graus C° e tranforma-las em F ((9/5) * C° + 32)
c_to_f = lambda valor: (valor[0], (9/5) * valor[1] + 32) # valor[0] = nome cidade e valor[1] C°

#print(list(map(c_to_f, cidade)))