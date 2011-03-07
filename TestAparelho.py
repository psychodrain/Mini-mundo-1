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



    def testValidarTroca_data_ok(self):
        cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', cliente)
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2011' # dentro do prazo
        self.failUnless(self.aparelho.validarTroca(data_compra, data_troca))

        # o flag indicando que o aparelho foi trocado deve ser True
        self.assertEqual(self.aparelho.trocado, True)

        
    def testValidarTroca_data_expirada(self):
        cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', cliente)
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2015' # mais de um ano
        self.failUnless(self.aparelho.validarTroca(data_compra, data_troca) == False)

        # o flag indicando que o aparelho foi trocado deve permanecer False
        self.assertEqual(self.aparelho.trocado, False)
            
        
        

if __name__== "__main__":
    unittest.main()
