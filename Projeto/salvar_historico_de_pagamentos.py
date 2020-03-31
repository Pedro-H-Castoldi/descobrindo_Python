import jsonpickle
import pagamento

def salver_pagamentos():
    with open('h_pagamentos.json', 'w', encoding='UTF-8') as pag:
        dados = jsonpickle.encode(pagamento.Pagamento.historico)
        pag.write(dados)
