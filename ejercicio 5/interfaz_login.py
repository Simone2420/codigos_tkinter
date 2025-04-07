import tkinter as tk
from tkinter import messagebox, ttk
from biblioteca_facade import *
from interfaz_biblioteca_facade import *
from interfaz_usuario import *
from modelos import excepciones,EmpleadoBiblioteca
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
        try:
            tipo_usuario = self.tipo_usuario.get()
            if tipo_usuario == "" or tipo_usuario not in ["empleado biblioteca","docente","estudiante"]:
                raise OpcionInvalida("Escoga un tipo de usuario adecuado")
            nombre = self.nombre.get().strip()
            if nombre == "":
                raise NombreVacio("El nombre no debe ser vacio")
            id_matricula = self.id_matricula.get().strip()
            if id_matricula == "":
                raise Id_MatriculaVacio("El numero de id profesional o numero de la matricula está vacio")
            identificacion = int(self.identificacion.get())
            if not identificacion:
                raise ValueError
            if tipo_usuario == "empleado biblioteca":
                logeador =BibliotecaFacade()
                bibliotecario = logeador.logear_usuario(tipo_usuario,nombre,id_matricula,identificacion)
                if bibliotecario == "Error en el id_profesional":
                    messagebox.showerror("Error en el id_profesional","El id profesional debe seguir este formato: P#####")
                elif bibliotecario == "Bibliotecario no encontrado" or bibliotecario == None:
                    messagebox.showwarning("Empleado no encontrado","Ingrese los datos del bibliotecario")
                else:
                    messagebox.showinfo("Empleado de la biblioteca encontrado exitosamente","Empleado de la biblioteca encontrado exitosamente")
                    self.ventana.withdraw()
                    nueva_ventana = tk.Toplevel()
                    InterfazBibliotecario(nueva_ventana, bibliotecario)
                nueva_ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_aplicacion(nueva_ventana))
            elif tipo_usuario == "docente" or tipo_usuario == "estudiante":
                logeador = BibliotecaFacade()
                if tipo_usuario == "docente":
                    docente = logeador.logear_usuario(tipo_usuario,nombre,id_matricula,identificacion)
                    if docente == "Error en el id_profesional":
                        messagebox.showerror("Error en el id_profesional","El id profesional debe seguir este formato: P#####")
                    elif docente == "Docente no encontrado" or docente == None:
                        messagebox.showwarning("Docente no encontrado","Ingrese los datos del docente")
                    else:
                        messagebox.showinfo("Docente encontrado exitosamente","Docente encontrado exitosamente")
                        self.ventana.withdraw()
                        nueva_ventana = tk.Toplevel()
                        InterfazUsuario(nueva_ventana, docente)
                    nueva_ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_aplicacion(nueva_ventana))
                elif tipo_usuario == "estudiante":
                    estudiante = logeador.logear_usuario(tipo_usuario,nombre,id_matricula,identificacion)
                    if estudiante == "Error en el número de matrícula":
                        messagebox.showerror("Error en el número de matricula","El numero de matrícula debe seguir este formato: M#####")
                    elif estudiante == "Estudiante no encontrado" or estudiante == None:
                        messagebox.showwarning("Estudiante no encontrado","Ingrese los datos del estudiante")
                    else:
                        messagebox.showinfo("Estudiante encontrado exitosamente","Estudiante encontrado exitosamente")
                        self.ventana.withdraw()
                        nueva_ventana = tk.Toplevel()
                        InterfazUsuario(nueva_ventana, estudiante)
                    nueva_ventana.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_aplicacion(nueva_ventana))
        except OpcionInvalida as e:
            messagebox.showerror("Error en tipo de usuario",e)
        except NombreVacio as e:
            messagebox.showerror("Error en ingreso del nombre del usuario",e)
        except Id_MatriculaVacio as e:
            messagebox.showerror("Error en ingreso del id o matriculo del usuario",e)
        # except ValueError:
        #     messagebox.showerror("Identificación invalida","El numero de la identificación debe ser numerico")
        # except Exception as e:
        #     messagebox.showerror("Error inesperado",e)
    def cerrar_aplicacion(self, ventana_secundaria):
        ventana_secundaria.destroy()
        self.ventana.destroy()