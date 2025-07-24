from models.conexao import conectar

def registrar_venda(cliente_id, usuario_id, total):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas (cliente_id, usuario_id, data, total) VALUES (%s, %s, NOW(), %s)",
                   (cliente_id, usuario_id, total))
    venda_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return venda_id