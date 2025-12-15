class PontoDeColeta:
    def __init__(self, id_ponto: int, nome: str, endereco: str,
    horario_funcionamento: str, responsavel: str):
        self.id_ponto = id_ponto
        self.nome = nome
        self.endereco_completo = endereco
        self.horario_funcionamento = horario_funcionamento
        self.responsavel = responsavel
        self.itens = []


    def cadastrar_ponto(self):
        print(f"Ponto de coleta '{self.nome}' cadastrado")


    def receber_item(self, item):
        self.itens.append(item)
        print(f"Item '{item.titulo}' recebido no ponto de coleta")


    def entregar_item(self, item, solicitante):
        if item in self.itens:
            self.itens.remove(item)
            print(f"Item '{item.titulo}' entregue para {solicitante.nome}")