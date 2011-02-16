import unittest
from Loja import Loja
from Aparelho import Aparelho

class TestLoja(unittest.TestCase):

    def testCriarLoja(self):
        loja = Loja("Lopes")
        assert loja.nome != None

    aparelho = Aparelho()
    def testCadastrarAparelho(self, aparelho):
        loja.aparelhos_disponiveis.append(aparelho)
        self.assertEqual(loja.aparelhos_disponiveis[-1], aparelho)


testCadas
##if __name__== "__main__":
##    unittest.main()
