from random import randint
l = [0]*20
m = [l] *20
maior = []

for i, _ in enumerate(m):
    for j, _ in enumerate(m):
        m[i][j] = randint(0,100)

for i, _ in enumerate(m):
    for j, _ in enumerate(m):
        if i < 3 and j < 3:
            pd = m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3]
            pb = m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j]
            pdi = m[i][j] * m[i+1][j+1] * m[i+2][j+2] * m[i+3][j+3]
        maior.append(max(pd, pb, pdi))
        pd = pb = pdi = 0
        if i < 3 and j >= 3:
            pd = m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3]
            pe = m[i][j] * m[i][j-1] * m[i][j-2] * m[i][j-3]
            pb = m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j]
            pdi = m[i][j] * m[i+1][j+1] * m[i+2][j+2] * m[i+3][j+3]
        maior.append(max(pd, pb, pdi))


        if i >= 3 and j < 3:
            pd = m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3]
            pb = m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j]
            pdi = m[i][j] * m[i+1][j+1] * m[i+2][j+2] * m[i+3][j+3]
        maior.append(max(pd, pb, pdi))

        if i >= 3 and j >= 3:
            pd = m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3]
            pe = m[i][j] * m[i][j-1] * m[i][j-2] * m[i][j-3]
            pb = m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j]
            pdi = m[i][j] * m[i+1][j+1] * m[i+2][j+2] * m[i+3][j+3]
        maior.append(max(pd, pb, pdi))

    print(max(maior))
