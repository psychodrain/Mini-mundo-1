import unittest
from Cliente import Cliente

class TestCliente(unittest.TestCase):


    def setUp(self):

        self.cliente = Cliente('Joao Ernesto', '(22) 22763091', 11302766802, False)
        

    def testCriacaodeNovoCliente(self):

        self.assertEqual(self.cliente.nome, 'Joao Ernesto')
        self.assertEqual(self.cliente.telefone, '(22) 22763091')
        self.assertEqual(self.cliente.cpf, 11302766802)
        self.assertEqual(self.cliente.reclamacao, False)


if __name__== "__main__":
    unittest.main()
