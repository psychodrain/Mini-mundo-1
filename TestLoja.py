import unittest
import Loja
import Aparelho

class TestLoja(unittest.TestCase):

    def setUp(self):
        self.loja = Loja.Loja("Lopes")
        self.aparelho = Aparelho.Aparelho()
        
    def testCriarLoja(self):
        assert self.loja.nome != None

    
    def testCadastrarAparelho(self):
        
        self.loja.aparelhos_disponiveis.append(self.aparelho)
        self.assertEqual(loja.aparelhos_disponiveis[-1], aparelho)


if __name__== "__main__":
    unittest.main()
