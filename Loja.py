class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.aparelhos_disponiveis = []


    def cadastrarAparelho(self, aparelho):
        self.aparelhos_disponiveis.append(self.aparelho)


    def listarAparelho(self):
        if self.aparelhos_disponiveis != []:
            print self.loja.aparelhos_disponiveis
        else:
            print 'Sem aparelhos'
