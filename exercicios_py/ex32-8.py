def simplifica(n=2, d=4):
    # nu = [x for x in range(1, d) if n % x == 0 and d % x == 0] Tentei usar List Comprehension..
    i =1
    m = max(n, d)
    while i < m:
        if n % i == 0 and d % i == 0:
            nu = i
        i = i + 1
    return f'{n/nu}/{d/nu} {nu}'

print(simplifica(36, 60))
print(simplifica(25, 5))
print(simplifica(36, 10))
print(simplifica())
