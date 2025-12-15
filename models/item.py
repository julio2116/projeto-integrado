from datetime import datetime


class Item:
    def __init__(self, id_item: int, titulo: str, descricao: str, categoria: str,
    estado_conservacao: str, doador):
        self.id_item = id_item
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.estado_conservacao = estado_conservacao
        self.fotos = []
        self.status = None
        self.doador = doador
        self.data_cadastro = datetime.now()


    def cadastrar_item(self):
        self.status = "DISPONIVEL"
        print(f"Item '{self.titulo}' cadastrado para doação")


    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do item atualizado para {self.status}")


    def adicionar_foto(self, foto_url: str):
        self.fotos.append(foto_url)
        print("Foto adicionada ao item")