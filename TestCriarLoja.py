import unittest
from Loja import Loja

class TestLoja(unittest.TestCase):

    def testCriarLoja(self):
        loja = Loja()
        assert loja.nome != None

if __name__== "__main__":
    unittest.main()