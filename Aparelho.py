class Aparelho:

    def __init__(self, marca, modelo, num_serie, data_compra, cliente):
        self.marca = marca
        self.modelo = modelo 
        self.num_serie = num_serie
        self.data_compra = data_compra
        self.cliente = cliente
        self.trocado = False


    def validarTroca(self, data_compra, data_troca):

        dia_compra = int(data_compra[0:2])
        mes_compra = int(data_compra[3:5])
        ano_compra = int(data_compra[6:])

        dia_troca = int(data_troca[0:2])
        mes_troca = int(data_troca[3:5])
        ano_troca = int(data_troca[6:])

        
        if ((dia_troca - dia_compra) + (mes_troca - mes_compra)*30 +
            (ano_troca - ano_compra)*360) <= 360:

            self.trocado = True

            return True
        
        else:
            return False



    
