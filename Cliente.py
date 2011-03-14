class Cliente():

    def __init__(self, nome="nao informado", telefone="nao informado", cpf="nao informado", reclamacao=False):

        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.reclamacao = reclamacao

    @staticmethod
    def clientesSatisfeitos(lista_clientes):

        satisfeitos = [cliente.nome for cliente in lista_clientes if cliente.reclamacao == False]

        return satisfeitos
        
