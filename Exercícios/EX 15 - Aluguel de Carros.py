carros = []

while True:
    d = int(input('Insira a quantidade de dias que o carro foi alugado: '))
    km = float(input('Insira a quantidade de Km percorrido: '))
    valor = (d * 60) + (km * 0.15)
    carros.append([d, km, valor])
    res = str(input('Insirir mais alugueis? S/N: '))
    if res in 'Nn':
        break
print('-'*48)
print(f'{"ALUGUEL":>27}')
print('-'*48)
print(f'N.{"QUANT. DIAS":>16}{"QUANT. KM":>15}{"VALOR":>15}')
print('-'*48)
for i, v in enumerate(carros):
    print(f'{i:<7}{carros[i][0]:<17}{carros[i][1]:<19}{carros[i][2]}')

