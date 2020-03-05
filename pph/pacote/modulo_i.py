jogo = 'Mortal Kombat 11'

def player():
    op = str(input('Qual melhor jogo de luta do mundo? '))
    op = op.title()
    if op == 'Mortal Kombat 11':
        return f'Você está correto! {jogo} é o melhor jogo de luta de todos os tempo. {op} é Kampeão!!!'
    return 'Essa é sua opinião...'