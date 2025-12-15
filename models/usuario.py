class Usuario:
    def __init__(self, id_usuario: int, nome: str, email: str, senha: str,
    telefone: str, endereco: str, tipo_usuario):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha # Em um sistema real, aqui seria um hash
        self.telefone = telefone
        self.endereco = endereco
        self.tipo_usuario = tipo_usuario


    def cadastrar(self):
        print(f"Usuário {self.nome} cadastrado com sucesso")


    def login(self, email: str, senha: str):
        if self.email == email and self.senha == senha:
            print("Login realizado com sucesso")
            return True
        print("Credenciais inválidas")
        return False


    def atualizar_perfil(self, nome=None, telefone=None, endereco=None):
        if nome:
            self.nome = nome
        if telefone:
            self.telefone = telefone
        if endereco:
            self.endereco = endereco
        print("Perfil atualizado")


    def solicitar_item(self, item):
        print(f"Solicitação iniciada para o item: {item.titulo}")