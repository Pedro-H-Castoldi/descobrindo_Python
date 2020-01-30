def meu_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration: # Quando der esse erro, significa q n tem mais caracteres para percorrer. Assim será encaminhado para o break.
            break


n = [1, 2, 3]
meu_for(n)