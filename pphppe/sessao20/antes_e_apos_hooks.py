"""
Unittest - Antes e Após Hooks

----
hooks - São os testes em si, ou seja, a execução dos testes.
----

setUp() -> É executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown() -> É Executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados.
"""

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        # Configurações do setup().
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass
    def test_segundo(self):
        # setUp() vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown().
