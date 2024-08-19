import tkinter as tk
from tkinter import messagebox
from .generator import PasswordGenerator

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas Seguras")

        self.length_var = tk.IntVar(value=12)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        tk.Label(root, text="Comprimento da Senha:").grid(row=0, column=0, sticky="e")
        tk.Entry(root, textvariable=self.length_var).grid(row=0, column=1)

        tk.Checkbutton(root, text="Incluir Letras Maiúsculas", variable=self.uppercase_var).grid(row=1, column=0, columnspan=2)
        tk.Checkbutton(root, text="Incluir Números", variable=self.numbers_var).grid(row=2, column=0, columnspan=2)
        tk.Checkbutton(root, text="Incluir Caracteres Especiais", variable=self.special_var).grid(row=3, column=0, columnspan=2)

        tk.Button(root, text="Gerar Senha", command=self.generate_password).grid(row=4, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def generate_password(self):
        generator = PasswordGenerator(
            length=self.length_var.get(),
            use_uppercase=self.uppercase_var.get(),
            use_numbers=self.numbers_var.get(),
            use_special=self.special_var.get()
        )
        password = generator.generate()
        self.result_label.config(text=password)
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Senha Gerada", "Sua senha foi copiada para a área de transferência!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
