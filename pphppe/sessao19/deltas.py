"""
Trabalhando com deltas de data e hora

data_inicial = 24/09/1996 15:30:22
data_final = 24/09/1996 15:55:21

delta = data_final - data_inicial


import datetime

hoje = datetime.datetime.now()

evento_futuro = datetime.datetime(2020, 9, 24)

tempo_para_evento = evento_futuro - hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds // 60 // 60} horas.') # Divisão com // retorna um número inteiro e n um flutuante.
"""

import datetime

# delta para pagamento de boleto
dia_pagamento = datetime.datetime.now()

regra_boleto = datetime.timedelta(days=3) # 3 dias (levam até 3 dias para o pagamento do boleto vingar).

vencimento_boleto = dia_pagamento + regra_boleto

print(vencimento_boleto) # 3 dias a mais da data de hoje.

