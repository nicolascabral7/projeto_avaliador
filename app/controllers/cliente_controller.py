import re
from models.cliente_model import inserir_cliente, listar_clientes

def validar_cpf(cpf):
    return re.fullmatch(r"\d{11}", cpf) is not None

def validar_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

def cadastrar_cliente(nome, cpf, email):
    if not validar_cpf(cpf):
        return "CPF inválido (deve conter 11 dígitos)"
    if not validar_email(email):
        return "E-mail inválido"
    inserir_cliente(nome, cpf, email)
    return "Cliente cadastrado com sucesso"

def obter_clientes():
    return listar_clientes()
