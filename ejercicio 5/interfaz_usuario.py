import tkinter as tk
from tkinter import messagebox, ttk
from biblioteca_facade import BibliotecaFacade
from modelos.excepciones import *
class InterfazUsuario:
    def __init__(self,ventana,usuario):
        self.biblioteca_facade = BibliotecaFacade()
        self.ventana = ventana
        self.ventana.geometry("1400x700")
        self.ventana.config(background="#EDEAE0")
        self.divisor_principal = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_principal.grid(row=0, column=0)
        self.divisor_secundario = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_secundario.grid(row=0, column=1)
        self.ventana.title("Menu Usuario")
        self.usuario = usuario
        self.seccion_informacion = tk.Frame(self.divisor_principal, background="#EDEAE0")
        self.seccion_informacion.grid(row=0, column=0, sticky="nsew")
        self.seccion_usuarios = tk.Frame(self.divisor_principal, background="#EDEAE0")
        self.seccion_usuarios.grid(row=1, column=0, sticky="nsew")
        self.interfaz_grafica()
    def interfaz_grafica(self):
        tk.Label(
            self.seccion_informacion,
            text="Menu Usuario",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack()
        tk.Label(
            self.seccion_informacion,
            text="Informacion del usuario",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack()
        self.informacion = tk.Label(
            self.seccion_informacion,
            text=self.biblioteca_facade.obtener_informacion_usuario(self.usuario),
            font=("Helvetica", 9),
            background="#EDEAE0"
        )
        self.informacion.pack()
        