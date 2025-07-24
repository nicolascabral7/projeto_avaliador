import tkinter as tk
from tkinter import messagebox
from controllers.cliente_controller import cadastrar_cliente, obter_clientes

class ClienteView:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Cadastro de Cliente")

        tk.Label(self.root, text="Nome").pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        tk.Label(self.root, text="CPF (somente números)").pack()
        self.entry_cpf = tk.Entry(self.root)
        self.entry_cpf.pack()

        tk.Label(self.root, text="E-mail").pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()

        tk.Button(self.root, text="Salvar", command=self.salvar).pack()
        tk.Button(self.root, text="Listar Clientes", command=self.listar).pack()

        self.listbox = tk.Listbox(self.root, width=60)
        self.listbox.pack()

    def salvar(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        msg = cadastrar_cliente(nome, cpf, email)
        messagebox.showinfo("Resultado", msg)
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def listar(self):
        self.listbox.delete(0, tk.END)
        clientes = obter_clientes()
        for c in clientes:
            self.listbox.insert(tk.END, f"ID: {c[0]} | Nome: {c[1]} | CPF: {c[2]} | E-mail: {c[3]}")
