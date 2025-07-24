import tkinter as tk

class MenuView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu Principal")
        tk.Button(self.root, text="Clientes", command=self.clientes).pack()
        tk.Button(self.root, text="Produtos", command=self.produtos).pack()
        tk.Button(self.root, text="Vendas", command=self.vendas).pack()
        self.root.mainloop()

    def clientes(self):
        from views.cliente_view import ClienteView
        ClienteView()

    def produtos(self):
        from views.produto_view import ProdutoView
        ProdutoView()

    def vendas(self):
        from views.venda_view import VendaView
        VendaView()
