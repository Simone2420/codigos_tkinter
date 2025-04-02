import tkinter as tk
from tkinter import messagebox, ttk
class LoginBiblioteca:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("1000x600")
        self.ventana.title("Gestor de Bibliotecas")
        self.ventana.config(background="#EDEAE0")
        
        # Configurar el grid principal para expandirse
        self.ventana.grid_rowconfigure(0, weight=3)  
        self.ventana.grid_rowconfigure(1, weight=5)  
        self.ventana.grid_rowconfigure(2, weight=1)  
        self.ventana.grid_columnconfigure(0, weight=1)
        
        # Divisores principales
        self.divisor_principal = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_principal.grid(row=0, column=0, sticky="nsew")
        
        self.divisor_secundario = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_secundario.grid(row=1, column=0, sticky="n")
        
        # Espacio inferior (vacío)
        self.espacio_inferior = tk.Frame(self.ventana, background="#EDEAE0")
        self.espacio_inferior.grid(row=2, column=0, sticky="nsew")
        
        # Configurar el grid dentro de los divisores
        self.divisor_principal.grid_rowconfigure(0, weight=1)
        self.divisor_principal.grid_columnconfigure(0, weight=1)
        
        self.divisor_secundario.grid_rowconfigure(0, weight=1)
        self.divisor_secundario.grid_columnconfigure(0, weight=1)
        
        self.menu_login()
        
    def menu_login(self):
        tk.Label(
            self.divisor_principal,
            text="Menu login",
            font=("Helvetica", 24),
            background="#EDEAE0"
        ).grid(row=0, column=0, sticky="n", pady=2)
        
        tk.Label(
            self.divisor_secundario,
            text="Tipo de usuario",
            font=("Helvetica", 18),
            background="#EDEAE0"
        ).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        
        self.tipo_usuario = ttk.Combobox(self.divisor_secundario,
            values=["empleado biblioteca","docente","estudiante"])
        self.tipo_usuario.grid(row=0,column=2,sticky="w",padx=10,pady=10)
        
        tk.Label(
            self.divisor_secundario,
            text="Nombre:",
            font=("Helvetica", 18),
            background="#EDEAE0"
        ).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        
        self.nombre = tk.Entry(
            self.divisor_secundario,
            font=("Helvetica", 18),
            width=20
        )
        self.nombre.grid(row=1, column=2, sticky="w", padx=10, pady=10)
        
        tk.Label(
            self.divisor_secundario,
            text="Numero de ID/Matricula:",
            font=("Helvetica", 18),
            background="#EDEAE0"
        ).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        
        self.id_matricula = tk.Entry(
            self.divisor_secundario,
            font=("Helvetica", 18),
            width=20
        )
        self.id_matricula.grid(row=2, column=2, sticky="w", padx=10, pady=10)
        
        tk.Label(
            self.divisor_secundario,
            text="Numero de identificaciòn:",
            font=("Helvetica", 18),
            background="#EDEAE0"
        ).grid(row=3, column=0, sticky="e", padx=10, pady=10)
        
        self.identificacion = tk.Entry(
            self.divisor_secundario,
            font=("Helvetica", 18),
            width=20
        )
        self.identificacion.grid(row=3, column=2, sticky="w", padx=10, pady=10)
        
        self.boton_login = tk.Button(
            self.divisor_secundario,
            text="Ingresar",
            command=self.realizar_login)
        self.boton_login.grid(row=4, column=1, pady=20)
        
    def realizar_login(self): 
        pass