with open('arq.txt', 'a+', encoding='UTF-8') as arq:
    while True:
        op = str(input('Digite algo ou "0" para encerrar: '))
        if op != '0':
            arq.write(op + '\n')
        else:
            arq.seek(0)
            print(arq.read())
            break

