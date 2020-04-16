import unittest

from .atividades import comer, dormir, eh_engracada

# Sempre botar o nome do arquivo e depois a palavra 'Testes'. EX: arquivoTestes(unittest.TestCase)
class AtividadesTestes(unittest.TestCase):
    # Sempre colocar 'test_' nos métodos de testes.
    def test_comer_saudavel(self):
        """Testando comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Comi quiabo para manter a forma.'
        )

    def test_comer_gostoso(self):
        """Testando comida não saudável."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Comi pizza pois só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando dormir pouco."""
        self.assertEqual(
            dormir(3),
            'Continuo cansado após dormir por 3 horas..'
        )
    def test_dormir_muito(self):
        """Testando dormir muito."""
        self.assertEqual(
            dormir(12),
            'Dormir demais! Perdi a hora.'
        )

    def test_eh_engracada(self):
        """Testando se a pessoa é engraçada."""
        #self.assertEqual(eh_engracado('Sérgio Malandro'), False) # É recomendado usar isso quando a função/método estiver vazio, ou seja, retornar None.
        self.assertFalse(eh_engracada('Sérgio Malandro'), 'essa pessoa não é engraçado.') # Esse segundo argumento é retornado se caso n der False.
        self.assertTrue(eh_engracada('Tatá'), 'Essa pessoa deveria ser engraçada.')



if __name__ == '__main__':
    unittest.main()