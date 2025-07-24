import tkinter as tk
from tkinter import messagebox
from controllers.produto_controller import cadastrar_produto

class ProdutoView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Produto")
        tk.Label(self.root, text="Nome").pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()
        tk.Label(self.root, text="Preço").pack()
        self.entry_preco = tk.Entry(self.root)
        self.entry_preco.pack()
        tk.Label(self.root, text="Estoque").pack()
        self.entry_estoque = tk.Entry(self.root)
        self.entry_estoque.pack()
        tk.Button(self.root, text="Salvar", command=self.salvar).pack()

    def salvar(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        estoque = int(self.entry_estoque.get())
        cadastrar_produto(nome, preco, estoque)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso")
        self.root.destroy()