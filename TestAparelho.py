import unittest
from Aparelho import Aparelho
from Termo import Termo

class TestAparelho(unittest.TestCase):

    def testCriacaodeAparelho(self):
        termo = Termo()
        self.aparelho = Aparelho("sony", "vaio", 1040, termo, cliente)
        self.assertEqual(self.aparelho.marca, 'sony')
        self.assertEqual(self.aparelho.modelo, 'sony')
        self.assertEqual(self.aparelho.num_serie, 'sony')
        self.assertEqual(self.aparelho.termo_garantia, 'sony')
        self.assertEqual(self.aparelho.cliente, 'sony')
            

if __name__== "__main__":
    unittest.main()
