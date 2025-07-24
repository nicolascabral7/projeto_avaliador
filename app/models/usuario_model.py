from models.conexao import conectar

def verificar_usuario(login, senha):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)  # ← Retorna como dicionário (melhor pra view)
    cursor.execute("SELECT * FROM usuarios WHERE login=%s AND senha=%s", (login, senha))
    usuario = cursor.fetchone()
    cursor.close()  # ← Boa prática: fecha o cursor
    conn.close()
    return usuario
