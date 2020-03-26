import jsonpickle
from caderno_de_fiados import Fiado

def salvar_fiados():
    with open('fiados.json', 'w', encoding='UTF-8') as fi:
        dados = jsonpickle.encode(Fiado.l_compras_fiadas)
        fi.write(dados)