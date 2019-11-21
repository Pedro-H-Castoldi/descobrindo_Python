algo = str(input('Digite o que quiser: '))
tradutor = []

for i in range(len(algo)):
    if algo[i] in 'Aa':
        tradutor.append('4')
    elif algo[i] in 'Bb':
        tradutor.append('8')
    elif algo[i] in 'Cc':
        tradutor.append('[')
    elif algo[i] in 'Dd':
        tradutor.append('|))')
    elif algo[i] in 'Ee':
        tradutor.append('&')
    elif algo[i] in 'Ff':
        tradutor.append('|=')
    elif algo[i] in 'Gg':
        tradutor.append('3')
    elif algo[i] in 'Hh':
        tradutor.append('#')
    elif algo[i] in 'Ii':
        tradutor.append('1')
    elif algo[i] in 'Jj':
        tradutor.append('j')
    elif algo[i] in 'Kk':
        tradutor.append('X')
    elif algo[i] in 'Ll':
        tradutor.append('1_')
    elif algo[i] in 'Mm':
        tradutor.append('//.')
    elif algo[i] in 'Nn':
        tradutor.append('//')
    elif algo[i] in 'Oo':
        tradutor.append('0')
    elif algo[i] in 'Pp':
        tradutor.append('|^')
    elif algo[i] in 'Qq':
        tradutor.append('q')
    elif algo[i] in 'Rr':
        tradutor.append('|2')
    elif algo[i] in 'Ss':
        tradutor.append('5')
    elif algo[i] in 'Tt':
        tradutor.append('7')
    elif algo[i] in 'Uu':
        tradutor.append('(_)')
    elif algo[i] in 'Vv':
        tradutor.append('V')
    elif algo[i] in 'Ww':
        tradutor.append('W')
    elif algo[i] in 'Xx':
        tradutor.append('><')
    elif algo[i] in 'Yy':
        tradutor.append('Y')
    elif algo[i] in 'Zz':
        tradutor.append('2')
    else:
        tradutor.append(algo[i])

for i in range(len(tradutor)):
    print(tradutor[i], end='')