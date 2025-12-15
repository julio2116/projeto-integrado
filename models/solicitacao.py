from datetime import datetime


class Solicitacao:
    def __init__(self, id_solicitacao: int, item, solicitante, doador):
        self.id_solicitacao = id_solicitacao
        self.item = item
        self.solicitante = solicitante
        self.doador = doador
        self.status = "PENDENTE"
        self.data_solicitacao = datetime.now()


    def criar(self):
        print("Solicitação criada")


    def aceitar(self):
        self.status = "ACEITA"
        self.item.atualizar_status("RESERVADO")
        print("Solicitação aceita")


    def recusar(self):
        self.status = "RECUSADA"
        print("Solicitação recusada")


    def finalizar(self):
        self.status = "FINALIZADA"
        self.item.atualizar_status("DOADO")
        print("Solicitação finalizada")