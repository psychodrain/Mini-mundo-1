import unittest
from Aparelho import Aparelho
from Cliente import Cliente

class TestAparelho(unittest.TestCase):


    def setUp(self):
        """
            Este metodo inicia as variaveis que serao usadas ao longo do teste
        """

        self.cliente = Cliente()
        self.aparelho = Aparelho("Sony", "Vaio", 1040, '25/02/2011', self.cliente)

        self.cliente2 = Cliente()
        self.aparelho2 = Aparelho("Apple", "iPhone", 2050, '11/03/2011', self.cliente2)
        

    def testCriacaodeAparelho(self):
        """
            Teste para verificar se o aparelho esta sendo criado com
            os parametros pretendidos
        """
        
        self.assertEqual(self.aparelho.marca, 'Sony')
        self.assertEqual(self.aparelho.modelo, 'Vaio')
        self.assertEqual(self.aparelho.num_serie, 1040)
        self.assertEqual(self.aparelho.data_compra, '25/02/2011')
        self.assertEqual(self.aparelho.cliente, self.cliente)

        self.assertEqual(self.aparelho2.marca, 'Apple')
        self.assertEqual(self.aparelho2.modelo, 'iPhone')
        self.assertEqual(self.aparelho2.num_serie, 2050)
        self.assertEqual(self.aparelho2.data_compra, '11/03/2011')
        self.assertEqual(self.aparelho2.cliente, self.cliente2)


                
    def testValidarTroca_data_expirada(self):
        """
            Teste que deve verificar se o metodo validarTroca do apareho realmente
            NAO valida as trocas no caso em que a data da troca esta fora do prazo
        """
        
        
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2015' # fora do prazo (mais de um ano)

        # a validacao deve falhar retornando False, pois a data da troca esta fora do prazo
        self.failUnless(self.aparelho.validarTroca(data_compra, data_troca, self.cliente, 'nao liga') == False)

        # o flag indicando que o aparelho foi trocado deve permanecer False
        self.assertEqual(self.aparelho.trocado, False)


    def testValidarTroca_data_ok(self):
        """
            Teste que deve verificar se o metodo validarTroca do apareho realmente
            valida as trocas no caso em que a data da troca esta dentro do prazo
        """
        
        
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

        

    def testCadastrarAparelho1(self):
        """
            Teste que deve verificar se o metodo cadastrarAparelho realmente
            esta adicionando o aparelho criado na lista de aparelhos disponiveis
        """
             

        Aparelho.cadastrarAparelho(self.aparelho) # metodo de classe para cadastrar aparelhos

        # verifica se o ultimo aparelho adicionado na lista de aparelhos
        # disponiveis eh igual ao aparelho que tentamos cadastrar:
        self.assertEqual(Aparelho.aparelhos_disponiveis[-1], self.aparelho)

        
    def testCadastrarAparelho2(self):
        """
            Ao cadastrar um segundo aparelho, a lista de aparelhos disponiveis
            deve crescer para dois. Este teste verificara isso.
        """

        #tamanho da lista de aparelhos disponiveis antes de adicionar um novo aparelho
        tamanho_anterior = len(Aparelho.aparelhos_disponiveis)
        
        Aparelho.cadastrarAparelho(self.aparelho2)
        
        # verifica se o ultimo aparelho adicionado na lista de aparelhos
        # disponiveis eh igual ao aparelho que tentamos cadastrar:
        self.assertEqual(Aparelho.aparelhos_disponiveis[-1], self.aparelho2)

        # ao adicionar mais um aparelho, o tamaho da lista de aparelhos disponiveis deve crescer em uma unidade
        tamanho = len(Aparelho.aparelhos_disponiveis)
        self.assertEqual(tamanho - tamanho_anterior , 1)


        
    def testListarAparelhosDisponiveis(self):
        """
            Teste simples para verificar se os aparelhos estao sendo listados corretamente
        """

        self.aparelho.listarAparelhos()
                
    def testAparelhosTrocados(self):
        """
            Deve listar todos os aparelhos que ja foram trocados (atributo 'trocado' == True)
        """
        cliente = 'Juana'
        # cria um novo aparelho
        self.aparelho3 = Aparelho("Apple", "iPad", 2040, '25/12/2011', cliente)
        
        # dados para popular o dicionario chamado dados_troca
        data_compra = self.aparelho.data_compra
        data_troca = '25/11/2011'
        # o comando abaixo significa que este aparelho ja foi trocado
        self.aparelho3.trocado = True
        # popula o dicionario chamado dados_troca
        self.aparelho3.dados_troca['cliente'] = cliente
        self.aparelho3.dados_troca['data'] = data_troca
        self.aparelho3.dados_troca['defeito'] = 'nao liga'
        
        # cadastra o novo aparelho criado
        Aparelho.cadastrarAparelho(self.aparelho3)
        
        self.aparelho.aparelhosTrocados()
        
if __name__== "__main__":
    unittest.main()
