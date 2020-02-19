"""
POO - Classes

Em POO classes nada mais são do q modelos do mundo real representados computacionalmente.

Imagine q vc queira fazer um sistema para automatizar o controle das lampadas da sua casa:
    - Nas classes podem conter:
        * Atributos -> Representam as características do objeto. Ou seja, pelo atributos podemos
        representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
        iremos querer saber: se a mesma é 110v ou 220v, se ela é branca, amarela, ou qualquer outra cor,
        qual é a iluminosidade, etc;

        * Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que esse objeto pode
        realizar no seu sistema. No caso da lâmpada, um comportamento q será desejado representar no sistema é o de
        ligar e desligar a lampada.

Em Python para definirmos uma classe, utilizamos a palavra reservada "class"

OBS: Quando nomeamos nossas classe em Python, por ética usamos a inicial do nome em maiúsculo. Se o nome for composto
cada inicial do nome será em maiúsculo sem espaço.

OBS: Quando estamos planejando um software e definindo quais classes teremos q ter no sistema, chamamos esses objetos
q serão mapeados para classes de entidade (por exemplo lampada e conta corrente são entidades). 

"""

# EX
class Lampada:
    pass

lamp = Lampada()

print(lamp)
print(type(lamp))

class ContaCorrente:
    pass