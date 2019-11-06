print('Bem-vindo a super promoção do Hipermercado Tabajara!')
print('Informe qual das opções você gostaria de levar:')
print('=*='*40)
print('                    Até 5kg                    Acima de 5kg')
print('1- Filé Duplo       R$ 4,90 por kg             R$ 5,80 por kg\n'
      '2- Alcatra          R$ 5,90 por kg             R$ 6,80 por kg\n'
      '3- Picanha          R$ 6,90 por kg             R$ 7,80 por kg')
print('=*='*40)

op = int(input('Quantos quilos? 1- Até 5kg | 2- Acima de 5Kg: '))
if op == 1:
    kg = 'Até 5kg'
    op2 = int(input('Qual produto vai querer levar? 1- Filé Duplo | 2- Alcatra | 3- Picanha: '))
    if op2 == 1:
        produto = 'Filé Duplo'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 4.90 * quant
    elif op2 == 2:
        produto = 'Alcatra'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 5.90 * quant
    else:
        produto = 'Picanha'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 6.90 * quant

elif op == 2:
    kg = 'Acima de 5kg'
    op2 = int(input('Qual produto vai querer levar? 1- Filé Duplo | 2- Alcatra | 3- Picanha: '))
    if op2 == 1:
        produto = 'Filé Duplo'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 5.80 * quant
    elif op2 == 2:
        produto = 'Alcatra'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 6.80 * quant
    else:
        produto = 'Picanha'
        quant = int(input(f'Informe a quantidade\n {produto} X : '))
        valor = 7.80 * quant

pg = int(input('Forma de pagamento 1- Cartão de Crédito | 2- Cartão de Débito | 3- Cartão Tabajara | 4- Dinheiro Vivo: '))
if pg == 1:
    while True:
        parce = int(input('Informe em quantas vezes será dividida a compra (MAX 5x sem juros): '))
        if parce >= 1 and parce <= 5:
            parcelas = valor / parce

            print('             Hipermercado Tabajara\n\n'
                  'Agradecemos sua compra!\n\n'
                  'DADOS DA COMPRA:\n'
                  f'PRDUTO: {produto}          KG: {kg}          QUANTIDADE: {quant}\n\n'
                  f'TIPO DE PAGAMENTO: Cartão de Crédito          PARCELA(S): {parce}\n'
                  f'VALOR TOTAL: {valor:.2f}          VALOR DA PARCELA: {parcelas:.2f}\n\n'
                  f'MUITO OBRIGADO.')
            break
        print('Não fazemos essa quantidade de parcelamento.')

elif pg == 2:
    print('             Hipermercado Tabajara\n\n'
          'Agradecemos sua compra!\n\n'
          'DADOS DA COMPRA:\n'
          f'PRDUTO: {produto}          KG: {kg}          QUANTIDADE: {quant}\n\n'
          f'TIPO DE PAGAMENTO: Cartão de Débito\n'
          f'VALOR TOTAL: {valor:.2f}\n\n'
          f'MUITO OBRIGADO.')

elif pg == 3:
    print('Com o Cartão Tabajara você terá 5% de descontos em suas compras!!!')
    while True:
        parce = int(input('Informe em quantas vezes será dividida a compra (MAX 5x sem juros): '))
        if parce >= 1 and parce <= 5:
            valortj = valor - (valor * 0.05)
            parcelas = valortj/parce

            print('             Hipermercado Tabajara\n\n'
                  'Agradecemos sua compra!\n\n'
                  'DADOS DA COMPRA:\n'
                  f'PRDUTO: {produto}          KG: {kg}          QUANTIDADE: {quant}\n\n'
                  f'TIPO DE PAGAMENTO: Cartão Tabajara          PARCELA(S): {parce}\n'
                  f'VALOR TOTAL: {valortj:.2f}          VALOR DA PARCELA: {parcelas:.2f}\n\n'
                  f'MUITO OBRIGADO.')
            break
        print('Não fazemos essa quantidade de parcelamento.')

else:
    print('             Hipermercado Tabajara\n\n'
          'Agradecemos sua compra!\n\n'
          'DADOS DA COMPRA:\n'
          f'PRDUTO: {produto}          KG: {kg}          QUANTIDADE: {quant}\n\n'
          f'TIPO DE PAGAMENTO: Dinheiro Vivo\n'
          f'VALOR TOTAL: {valor:.2f}\n\n'
          f'MUITO OBRIGADO.')