import tkinter as tk
from tkinter import messagebox
from controllers.venda_controller import realizar_venda

class VendaView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Registrar Venda")

        tk.Label(self.root, text="ID do Cliente:").pack()
        self.entry_cliente = tk.Entry(self.root)
        self.entry_cliente.pack()

        tk.Label(self.root, text="ID do Usuário:").pack()
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack()

        tk.Label(self.root, text="ID do Produto:").pack()
        self.entry_produto = tk.Entry(self.root)
        self.entry_produto.pack()

        tk.Label(self.root, text="Quantidade:").pack()
        self.entry_quantidade = tk.Entry(self.root)
        self.entry_quantidade.pack()

        tk.Label(self.root, text="Preço Unitário:").pack()
        self.entry_preco = tk.Entry(self.root)
        self.entry_preco.pack()

        tk.Button(self.root, text="Adicionar Item", command=self.adicionar_item).pack()
        tk.Button(self.root, text="Finalizar Venda", command=self.finalizar_venda).pack()

        self.itens = []

    def adicionar_item(self):
        produto_id = int(self.entry_produto.get())
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())
        self.itens.append({
            'produto_id': produto_id,
            'quantidade': quantidade,
            'preco': preco
        })
        messagebox.showinfo("Item", "Item adicionado")

    def finalizar_venda(self):
        cliente_id = int(self.entry_cliente.get())
        usuario_id = int(self.entry_usuario.get())
        venda_id = realizar_venda(cliente_id, usuario_id, self.itens)
        messagebox.showinfo("Venda", f"Venda registrada com ID {venda_id}")
        self.root.destroy()