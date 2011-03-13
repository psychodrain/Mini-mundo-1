class Aparelho:

    #atributo de classe
    aparelhos_disponiveis = []
    
    def cadastrarAparelho(aparelho):
        Aparelho.aparelhos_disponiveis.append(aparelho)

    
    def __init__(self, marca, modelo, num_serie, data_compra, cliente):
        self.marca = marca
        self.modelo = modelo 
        self.num_serie = num_serie
        self.data_compra = data_compra
        self.cliente = cliente
        self.trocado = False
        self.dados_troca = {'cliente': None, 'data': None, 'defeito': None}


    def validarTroca(self, data_compra, data_troca, cliente, defeito):

        dia_compra = int(data_compra[0:2])
        mes_compra = int(data_compra[3:5])
        ano_compra = int(data_compra[6:])

        dia_troca = int(data_troca[0:2])
        mes_troca = int(data_troca[3:5])
        ano_troca = int(data_troca[6:])

        
        if ((dia_troca - dia_compra) + (mes_troca - mes_compra)*30 +
            (ano_troca - ano_compra)*360) <= 360:

            self.trocado = True
            self.dados_troca['cliente'] = cliente
            self.dados_troca['data'] = data_troca
            self.dados_troca['defeito'] = defeito

            return self.trocado
        
        else:
            return self.trocado


    def listarAparelhos(self):
        print 'Aparelhos disponiveis:'
        for aparelho in Aparelho.aparelhos_disponiveis:
            print 'marca: %s, modelo: %s, trocado? %s' % (aparelho.marca, aparelho.modelo, aparelho.trocado)

    

    def aparelhosTrocados(self):
        trocados = [aparelho for aparelho in Aparelho.aparelhos_disponiveis if aparelho.trocado == True]

        print 'trocados: '

        for aparelho in trocados:
            print 'Um %s (num de serie: %s) foi trocado por %s no dia %s com o seguinte defeito declarado: ''%s''' % (aparelho.modelo, aparelho.num_serie, aparelho.dados_troca['cliente'], aparelho.dados_troca['data'], aparelho.dados_troca['defeito'])
