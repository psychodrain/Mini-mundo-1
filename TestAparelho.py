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



    def testValidarTroca(self):
        cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', cliente)
        data_compra = self.aparelho.data_compra
        data_troca = '25/03/2011'
        self.aparelho.validarTroca(data_compra, data_troca)



        
##        self.assertEqual(data_compra, self.aparelho.data_compra)
##
##        dia = int(data_compra[0:2])
##        mes = int(data_compra[3:5])
##        ano = int(data_compra[6:])
##
##        self.assertEqual(dia, 25)
##        self.assertEqual(mes, 02)
##        self.assertEqual(ano, 2011)



if __name__== "__main__":
    unittest.main()
