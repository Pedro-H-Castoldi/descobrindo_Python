import jsonpickle
import compra

def salvar_comprar():
    with open('h_compras.json', 'w', encoding='UTF-8') as com:
        dados = jsonpickle.encode(compra.Compra.l_compras)
        com.write(dados)