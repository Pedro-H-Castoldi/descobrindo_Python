# Variável global (escopo global)
n = 5
print(n)

# Variável local (escopo local)
if n < 10:
    novo = n +10
    print(novo) # A variável só passará existir agora, se o if n rodar a variável n será reconhecida