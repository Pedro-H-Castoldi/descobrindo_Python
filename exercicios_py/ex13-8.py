def calcular(n1, s, n2):
    if s in '+-Xx*/':
        if s == '+':
            return n1 + n2
        elif s == '-':
            return n1 - n2
        elif s in 'Xx*':
            return n1 * n2
        return n1 / n2
    return 'ERRO NA OPERAÇÃO!'

print('Digite a operação:\n')
nu1 = int(input())
si = str(input())
nu2 = int(input())

print(calcular(nu1, si, nu2))