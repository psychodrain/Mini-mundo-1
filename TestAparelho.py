import unittest
from Aparelho import Aparelho
from Cliente import Cliente

class TestAparelho(unittest.TestCase):

    def testCriacaodeAparelho(self):
        cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', cliente)
        self.assertEqual(self.aparelho.marca, 'sony')
        self.assertEqual(self.aparelho.modelo, 'vaio')
        self.assertEqual(self.aparelho.num_serie, 1040)
        self.assertEqual(self.aparelho.data_compra, '25/02/2011')
        self.assertEqual(self.aparelho.cliente, cliente)

    def validarTroca(self):
        cliente = Cliente()
        troca = {'data_troca': '25/03/2011', 'cliente':cliente}
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', cliente)

                

if __name__== "__main__":
    unittest.main()
