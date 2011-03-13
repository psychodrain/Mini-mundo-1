class Aparelho:

    #atributo de classe
    aparelhos_disponiveis = []
    
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

            return True
        
        else:
            return False


    def cadastrarAparelho(aparelho):
        Aparelho.aparelhos_disponiveis.append(aparelho)



    
