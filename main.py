from models.usuario import Usuario
from models.item import Item
from models.solicitacao import Solicitacao
from models.ponto_coleta import PontoDeColeta
from enums.tipo_usuario import TipoUsuario


# Criação de usuários
doador = Usuario(1, "Carlos", "c@email.com", "123", "9999", "Centro", TipoUsuario.DOADOR)
receptor = Usuario(2, "Ana", "a@email.com", "456", "8888", "Bairro", TipoUsuario.RECEPTOR)


# Cadastro de item
item = Item(1, "Mochila Azul", "Mochila usada", "Mochila", "Usado", doador)
item.cadastrar_item()


# Solicitação
sol = Solicitacao(1, item, receptor, doador)
sol.criar()
sol.aceitar()
sol.finalizar()