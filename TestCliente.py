import unittest
from Cliente import Cliente

class TestCliente(unittest.TestCase):


    def setUp(self):

        self.cliente = Cliente('Joao Ernesto', '(22) 22763091', 11302766802, False)
        

    def testConstrutorCliente(self):

        self.assertEqual(self.cliente.nome, 'Joao Ernesto')
        self.assertEqual(self.cliente.telefone, '(22) 22763091')
        self.assertEqual(self.cliente.cpf, 11302766802)
        self.assertEqual(self.cliente.reclamacao, False)


    def test_relatorio_clientes_satisfeitos(self):
        lista_clientes = []
        lista_clientes.append(self.cliente)

        cliente2 = Cliente('Maria Maria', '(22) 66554423', 11402766802, True)
        cliente3 = Cliente('Manuel Silveira', '(22) 89765432', 11502766802, False)

        lista_clientes.append(cliente2)
        lista_clientes.append(cliente3)

        Cliente.clientesSatisfeitos(lista_clientes)


if __name__== "__main__":
    unittest.main()
