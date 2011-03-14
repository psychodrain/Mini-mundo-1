# -*- coding: cp1252 -*-
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

        #criacao de novos clientes
        cliente2 = Cliente('Maria Maria', '(22) 66554423', 11402766802, True)
        cliente3 = Cliente('Manuel Silveira', '(22) 89765432', 11502766802, False)

        # adicionando novos clientes na lista de clientes
        lista_clientes.append(cliente2)
        lista_clientes.append(cliente3)
        
        # clientesSatisfeitos é um metodo estatíco da classe Cliente
        satisteitos = Cliente.clientesSatisfeitos(lista_clientes)
        devem_estar_satisfeitos = [cliente.nome for cliente in lista_clientes if cliente.reclamacao == False]

        self.assertEqual(satisteitos, devem_estar_satisfeitos)

        # apenas para visualizar no Console o que esta ocorrendo
        print Cliente.clientesSatisfeitos(lista_clientes)
        

if __name__== "__main__":
    unittest.main()
