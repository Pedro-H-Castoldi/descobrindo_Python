algo = str(input('Digite uma frase: '))
vogais = espacos = 0

for i in range(len(algo)):
    if algo[i] in 'AaEeIiOoUu':
        vogais += 1
    if algo[i] in ' ' * 9999:
        espacos += 1

print(f'{algo}\n'
      f'Quantidade de vogais: {vogais}\n'
      f'Quantidade de espeços: {espacos}')