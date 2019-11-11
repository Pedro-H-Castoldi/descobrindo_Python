meses = {
    '1- Janeiro': 'Temperatura de janeiro: ', '2- Fevereiro': 'Temperatura de fevereiro: ', '3- Março': 'Temperatura de março: ',
    '4- Abril': 'Temperatura de abri: ', '5- Maio': 'Temperatura de maio: ', '6- Junho': 'Temperatura de junho: ',
    '7- Julho': 'Temperatura de julho: ', '8- Agosto: ': 'Temperatura de agosto: ', '9- Setembro': 'Temperatura de setembro: ',
    '10- Outubro': 'Temperatura de outubro: ', '11- Novembro': 'Temperatura de novembro: ', '12- Dezembro': 'Temperatura de dezembro: '
}

mes_temp = {chave: int(input(valor)) for chave, valor in meses.items()}

{print({chave: valor}) for chave, valor in mes_temp.items()}

import statistics

media = statistics.mean(mes_temp.values())
print(f'A Média foi: {round(media, 2)}')

acima = {chave: valor for chave, valor in mes_temp.items() if valor > media}

print(f'Os meses com temperatura acima da média são:\n{acima}')





# Forma 2
#for i, _ in enumerate(meses):
   # t = int(input(f'Temperatura do mes de {meses[i]}: ' ))
   # meses_temp.update({meses[i]: t})
