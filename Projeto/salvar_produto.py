def salvar_produto(produto):
    with open('produtos.txt', 'a+', encoding='UTF-8') as pro:
        pro.write(f'\n{produto.id}--{produto.nome}--{produto.tipo}--{produto.preco}--{produto.quant}--{produto.estoque}\n')