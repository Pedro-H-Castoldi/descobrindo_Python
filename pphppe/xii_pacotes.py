"""
Diferença entre pacote e módulo:
    - Módulo -> Um arquivo Python q possui diversas funções para serem utilizadas;

    - Pacote -> Um diretório q possui diversos módulos (arquivos Python).

OBS: - Nas versões 2.x do Python, os pacotes deveriam ter um arquivo __init__.py dentro deles.
 - A partir das versões 3.x esse tipo de arquivo n é mais obrigatório, no entento, ainda se utiliza por rasões de compatibilidade.

Se usa pacotes para ORGANIZAR o código.


 # Importanto pacotes e seus módulos

from pacote import modulo_i, modulo_ii

print(modulo_i.player()) # Importando função do módulo modulo_i


print(modulo_ii.facaOCerto())

# Importando sub-pacote
from pacote.sub_pacote import modulo_iii, modulo_iv

print(modulo_iii.lin())

print(modulo_iv.soma(2, 4))

"""

# Passando apenas uma função do módulo
from pacote.modulo_ii import facaOCerto

print(facaOCerto())


from pacote.sub_pacote.modulo_iv import soma
print(soma(3, 3))