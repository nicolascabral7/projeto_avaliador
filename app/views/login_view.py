import tkinter as tk
from tkinter import messagebox
from controllers.login_controller import autenticar_usuario

class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        tk.Label(self.root, text="Usuário").pack()
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()
        tk.Label(self.root, text="Senha").pack()
        self.entry_pass = tk.Entry(self.root, show="*")
        self.entry_pass.pack()
        tk.Button(self.root, text="Entrar", command=self.login).pack()
        self.root.mainloop()

    def login(self):
        user = self.entry_user.get()
        senha = self.entry_pass.get()
        if autenticar_usuario(user, senha):
            messagebox.showinfo("Sucesso", "Login realizado")
            self.root.destroy()
            from views.menu_view import MenuView
            MenuView()
        else:
            messagebox.showerror("Erro", "Login inválido")
