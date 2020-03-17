from produto import Produto

def salvar_produto():
    with open('produtos.txt', 'w+', encoding='UTF-8') as pro:
        for produto in Produto.l_produtos:
            pro.write(f'\n{produto.id}--{produto.nome}--{produto.tipo}--{produto.preco}--{produto.quant}--{produto.estoque}\n')