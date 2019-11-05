while True:
    v = int(input('Digite a velocidade: '))
    if v >= 0:
        if v <= 80:
            print('Velocidade permitida.\nDIRIJA COM SEGURANÇA!')
            break
        else:
            multa = (v - 80)*7
            print(f'Velocidade acima de 80km/h. O Sr(a) terá que pagar uma multa de R${multa} reais.\nDIRIJA COM CUIDADO!')
            break

