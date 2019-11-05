def quadrado_perfeito(n):
    for i in range(1, n+1):
        if i**2 == n:
            return f'{n} é um quadrado perfeito de {i}'
    return f'{n} não é um quadrado perfeito..'


nu = int(input("Digite um número: "))
print(quadrado_perfeito(nu))
