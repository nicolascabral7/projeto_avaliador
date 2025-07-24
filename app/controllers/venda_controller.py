from models.venda_model import registrar_venda
from models.itens_venda_model import adicionar_item_venda

def realizar_venda(cliente_id, usuario_id, itens):
    total = sum(item['quantidade'] * item['preco'] for item in itens)
    venda_id = registrar_venda(cliente_id, usuario_id, total)
    for item in itens:
        adicionar_item_venda(venda_id, item['produto_id'], item['quantidade'], item['preco'])
    return venda_id