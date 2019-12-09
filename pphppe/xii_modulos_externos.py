"""
Utilizamos o gerenciador de pacotes Python Python Installer Packager (Pip)

Para acessar os pacotes externos oficiais acesse: pypi.org

Utilizando o colorama
    - Para instalar o colorama: pip install colorama
    - O colorama é um módulo externo para colorir textos na impressão no terminal.


# Utilizando o colorama na IDE
from colorama import init, Fore
init() # mesmo sem usar essa função já funcionou

print(Fore.CYAN + 'O Plano Terreno será protegido!')
"""

import pydf # Erro. Parece q n é um arquivo compatível com o Windowa 32bits

pdf = pydf.generate_pdf('<h1>Python Projeto de Vida</h1>')
with open('projeto_de_vida.pdf', 'wb') as f:
    f.write(pdf)