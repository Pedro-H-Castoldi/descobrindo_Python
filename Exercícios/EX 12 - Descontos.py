"""
#       Descontos

print(' -SEJA BEM-VINDO A LOJA DESCONTO JA!-')
pre = float(input(f'Digite o preço: '))
print(f'Com os 5% de desconto da nossa loja seu produto de {pre :.2f} sairá por: {pre - (pre*0.05) :.2f}')
"""

# EX 13 - Reajuste salárial
sa = float(input('Digite o salário: '))
ap = float(input(f'Qual será a porcentagem de aumento do salario de {sa}: '))
print(f'Com o aumento de {ap}% o salário aumentará de {sa} para {sa + (sa * ap/100):.2f}')
