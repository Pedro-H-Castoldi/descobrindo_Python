"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python

import this

A idéia de PEP8 é q possamos escrever códigos python de forma pythónica.

[1] Utiliza Camel case para nomes de classes:

    class Calcularora:
        pass


    class CalculadoraCientifica:
        pass


[2] Utilize nomes em minúsculo, separada por anderline para funções ou variáveis:

    def soma();
    pass

    def soma_dois();
    pass

    numero = 4

    numero_impar = 5


[3] Utilizar 4 espaços para identação (n utilizar o tab):

    if 'a' in 'ban':
        print ('tem')
    else:
        print ('Nao tem')


[4] Linhas em branco:
        Para separar funções e definições de classes é necessário 2 linhas em branco;
        Métados dentro de uma classe basta apenas 1 linha em branco.


[5] Sobre Imports:
        Imports devem ser sempre feitos em linhas separadas;
        ERRADO:
            import sys, os

        CERTO:
            import sys
            import os

        N HÁ PROBLEMAS EM:
            from types import StringType, ListType

        CASO TENHA MUITO IMPORTS DE UM MESMO PACOTE, RECOMENDA-SE:
            from types import{
            StringType,
            ListType,
            SetType,
            OutraType
        }
        IMPORTS DEVEM SER COLOCADOS NO TOPO DO ARQUIVO, LOGO DEPOIS DE QUALQUER COMENTÁRIO OU DOCSTRINGS E
        ANTES DE CONSTANTES E VARIÁVEIS!


    [6] Espaços em expressões e instruções
        ERRADO:
            funcao{ algo[ 7 ], { outro: 8 }}
            algo [ 5 ]
            x               =3
            numero_variavel =5

        CERTO:
            funcao{algo[7], {outro: 8}}
            algo[5]
            x = 3
            numero_variavel = 5


    [7] Termine sempre uma instrução com uma nova linha:

"""
import this
