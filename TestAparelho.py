import unittest
from Aparelho import Aparelho
from Cliente import Cliente

class TestAparelho(unittest.TestCase):


    def setUp(self):
        self.cliente = Cliente()
        self.aparelho = Aparelho("sony", "vaio", 1040, '25/02/2011', self.cliente)

        self.cliente2 = Cliente()
        self.aparelho2 = Aparelho("Apple", "iPhone", 2050, '11/03/2011', self.cliente2)

    def testCriacaodeAparelho(self):
        
        
        self.assertEqual(self.aparelho.marca, 'sony')
        self.assertEqual(self.aparelho.modelo, 'vaio')
        self.assertEqual(self.aparelho.num_serie, 1040)
        self.assertEqual(self.aparelho.data_compra, '25/02/2011')
        self.assertEqual(self.aparelho.cliente, self.cliente)


    def testValidarTroca_data_ok(self):
        
        
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2011' # dentro do prazo

        # nao deve falhar, pois o aparelho esta sendo trocado dentro do prazo
        self.failUnless(self.aparelho.validarTroca(data_compra, data_troca, self.cliente, 'nao liga'))
        # o flag indicando que o aparelho foi trocado deve ser True, pois a troca foi validada
        self.assertEqual(self.aparelho.trocado, True)
        # verifica o registro do cliente que realizou a troca (neste caso foi o mesmo que cliente que comprou)
        self.assertEqual(self.aparelho.dados_troca['cliente'], self.cliente)
        # verificacao da data e do defeito dentro do dicionario dados_troca
        self.assertEqual(self.aparelho.dados_troca['data'], '25/11/2011')
        self.assertEqual(self.aparelho.dados_troca['defeito'], 'nao liga')

        
    def testValidarTroca_data_expirada(self):
        
        
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2015' # fora do prazo (mais de um ano)

        # a validacao deve falhar retornando False, pois a data da troca esta fora do prazo
        self.failUnless(self.aparelho.validarTroca(data_compra, data_troca, self.cliente, 'nao liga') == False)

        # o flag indicando que o aparelho foi trocado deve permanecer False
        self.assertEqual(self.aparelho.trocado, False)


    def testCadastrarAparelho1(self):
        
        
        Aparelho.cadastrarAparelho(self.aparelho) # metodo de classe para cadastrar aparelhos

        # verifica se o ultimo aparelho adicionado na lista de aparelhos
        # disponiveis eh igual ao aparelho que tentamos cadastrar:
        self.assertEqual(Aparelho.aparelhos_disponiveis[-1], self.aparelho)

        
    def testCadastrarAparelho2(self):
        """
            ao cadastrar um segundo aparelho, a lista de aparelhos disponiveis
            deve crescer para dois. Este teste verificara isso.
        """
        
        Aparelho.cadastrarAparelho(self.aparelho2)
        
        # verifica se o ultimo aparelho adicionado na lista de aparelhos
        # disponiveis eh igual ao aparelho que tentamos cadastrar:
        self.assertEqual(Aparelho.aparelhos_disponiveis[-1], self.aparelho2)

        # ao adicionar mais um aparelho, o tamaho da lista de aparelhos disponiveis deve ser 2
        tamanho = len(Aparelho.aparelhos_disponiveis)
        self.assertEqual(tamanho, 2)

        
    def testListarAparelhosDisponiveis(self):

        self.aparelho2.listarAparelhos()
        
        

if __name__== "__main__":
    unittest.main()
