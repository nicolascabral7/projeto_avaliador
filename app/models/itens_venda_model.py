from models.conexao import conectar

def adicionar_item_venda(venda_id, produto_id, quantidade, preco_unitario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                   (venda_id, produto_id, quantidade, preco_unitario))
    cursor.execute("UPDATE produtos SET estoque = estoque - %s WHERE id = %s", (quantidade, produto_id))
    conn.commit()
    conn.close()