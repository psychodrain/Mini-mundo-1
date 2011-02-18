import unittest
from Aparelho import Aparelho
from Termo import Termo
from Cliente import Cliente

class TestAparelho(unittest.TestCase):

    def testCriacaodeAparelho(self):
        termo = Termo()
        cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, termo, cliente)
        self.assertEqual(self.aparelho.marca, 'sony')
        self.assertEqual(self.aparelho.modelo, 'vaio')
        self.assertEqual(self.aparelho.num_serie, 1040)
        self.assertEqual(self.aparelho.termo_garantia, termo)
        self.assertEqual(self.aparelho.cliente, cliente)
            

if __name__== "__main__":
    unittest.main()
