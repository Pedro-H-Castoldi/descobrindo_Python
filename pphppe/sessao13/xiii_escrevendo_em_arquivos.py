"""
Ao abrir um arquivo para leitura não podemos escrever nele, da mesma forma serve para a escrita.

OBS: Ao criarmos um arquivo para escrita, o mesmo é criado no SO.

Abrindo um arquivo no modo 'w', se o arquivo n existir, ele será criado, se já existir,
o anterior será apagado e inserido o novo. Com isso todo o arquivo antigo será perdido.


# Abrindo o arquivo no modo de escrita 'w' (write -> escrever)
# OBS: N pode inserir números como parâmetro na função write(), só é aceito strings.
with open('novo.txt', 'w', encoding='UTF-8') as ar:
    ar.write('Natal e ano novo está logo aí\n')
    ar.write('É muito fácil e simples\n')
    ar.write('Evoluindo sempre!\n')
    ar.write('Oi ' * 10)
"""

# Escrevendo dentro de um loop
with open('escrevendo_em_loop.txt', 'w') as es:
    while True:
        t = str(input('Escreva algo ou digite sair para sair: '))
        if t == 'sair':
            break
        else:
            es.write(t + '\n') # Adicionar quebra de linha