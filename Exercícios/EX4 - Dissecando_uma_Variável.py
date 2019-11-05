v = input('Digite algo: ')
print(f'Essa variável é do tipo.....: {type(v)}')
print(f'A variável só possui espaços? {v.isspace()}')
print(f'É um número.................? {v.isnumeric()}')
print(f'É alfabetico................? {v.isalpha()}')
print(f'É alfanumerico..............? {v.isalnum()}')
print(f'Está em maiúsculo...........? {v.isupper()}')
print(f'Está em minúsculo...........? {v.islower()}')
print(f'Está capitalizado...........? {v.istitle()}') # Capitalizada é quando se está em titlo. EX: Pedro Henrique.
