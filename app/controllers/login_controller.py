from models.usuario_model import verificar_usuario

def autenticar_usuario(login, senha):
    return verificar_usuario(login, senha)
