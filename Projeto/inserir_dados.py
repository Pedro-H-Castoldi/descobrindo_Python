from cliente import Cliente
from produto import Produto
from caderno_de_fiados import Fiado
from pagamento import Pagamento
from compra import Compra
import jsonpickle

def inserir_dados():
    with open('clientes.json', 'r', encoding='UTF-8') as clientes:
        dados = clientes.read()
        Cliente.l_clientes = jsonpickle.decode(dados)

    with open('produtos.json', 'r', encoding='UTF-8') as produtos:
        dados = produtos.read()
        Produto.l_produtos = jsonpickle.decode(dados)

    with open('fiados.json', 'r', encoding='UTF-8') as fiados:
        dados = fiados.read()
        Fiado.l_compras_fiadas = jsonpickle.decode(dados)

    with open('h_pagamentos.json', 'r', encoding='UTF-8') as pagamentos:
        dados = pagamentos.read()
        Pagamento.historico = jsonpickle.decode(dados)

    with open('h_compras.json', 'r', encoding='UTF-8') as compras:
        dados = compras.read()
        Compra.l_compras = jsonpickle.decode(dados)