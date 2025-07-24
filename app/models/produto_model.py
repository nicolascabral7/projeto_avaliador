from models.conexao import conectar

def inserir_produto(nome, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", (nome, preco, estoque))
    conn.commit()
    conn.close()