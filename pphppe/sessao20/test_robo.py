"""
Unittest - Antes e Após Hooks

----
hooks - São os testes em si, ou seja, a execução dos testes.
----

setUp() -> É executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown() -> É Executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados.



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


# Sem hooks
import unittest

from .robo import Robo
class RoboTestes(unittest.TestCase):
    def test_bateria(self):
        megaman = Robo('Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)

    def test_dizer_nome(self):
        megaman = Robo('Mega Man', bateria=50)
        self.assertEqual(megaman.dizer_nome(), 'Meu nome é MEGA MAN.')
        self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%.')



"""
import unittest

# Usando hooks
from .robo import Robo
class RoboTestes(unittest.TestCase):
    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado.')

    def test_bateria(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), 'Meu nome é MEGA MAN.')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%.')

    def tearDown(self):
        print('tearDown() sendo executado.')

if __name__ == '__main__':
    unittest.main()