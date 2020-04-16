"""
Introdução ao Módulo Unittest

Unittest -> Testes Unitários

O q são testes unitários?
    - Testes é a forma de se testar unidades individuais de código fonte;
    - Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

OBS: Testes Unitários n é algo específico da linguagem Python.

Para criar nossos testes, criamos classes q herdam de unittest.TestCase,
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main().

Test Case -> Casos de testes para sua unidade.

# Conhecendo as assertions
Método                                 Checa se
assertEqual(a, b)                      a == b
assertNotEqual(a, b)                   a != b
assertTrue(x)                          x é True
assertFalse(x)                         x é False
assertIs(a, b)                         a é b
assertNotIs(a, b)                      a n é b
assertIfNone(x)                        x é None
assertIsNotNone(x)                     x n é None
assertIn(a, b)                         a in b
assertNotIn(a, b)                      a not in b
assertIsInstance(a, b)                 a é instância de b
assertNotIsInstance(a, b)              a n é instância de b


# Para executar os testes com unittest
python arq.py (terminal - no meu n deu certo, fui pelo run).

# Para executar os testes com unittest no modo verbose
python arq.py -v


OBS: É recomendado usar docstrings nos testes.
"""