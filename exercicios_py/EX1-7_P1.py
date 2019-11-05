A = [1, 0, 5, -2, -5, 7]

nu = A[0] + A[1] + A[5]
print(f'SOMA: {nu}')

A[4] = 100

for i, _ in enumerate(A):
    print(A[i])