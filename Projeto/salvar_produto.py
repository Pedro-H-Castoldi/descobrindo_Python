from produto import Produto
import jsonpickle

def salvar_produto():
    with open('produtos.json', 'w', encoding='UTF-8') as pro:
        dados = jsonpickle.encode(Produto.l_produtos)
        pro.write(dados)