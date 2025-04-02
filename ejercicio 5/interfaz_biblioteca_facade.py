import tkinter as tk
from tkinter import messagebox, ttk
class InterfazGeneral:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("1000x600")
        self.ventana.config(background="#EDEAE0")
        self.divisor_principal = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_principal.grid(row=0, column=0)
        self.divisor_secundario = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_secundario.grid(row=0, column=1)
class InterfazBibliotecario(InterfazGeneral):
    def __init__(self, ventana,bibliotecario):
        super().__init__(ventana)
        self.ventana.title("Gestor de Bibliotecas")
        self.bibliotecario = bibliotecario
class InterfazUsuario(InterfazGeneral):
    def __init__(self,ventana,usuario):
        super().__init__(ventana)
        self.ventana.title("Ventana del usuario")
        self.usuario = usuario