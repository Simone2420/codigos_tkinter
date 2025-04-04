import tkinter as tk
from tkinter import messagebox, ttk
from biblioteca_facade import BibliotecaFacade
class InterfazGeneral:
    def __init__(self,ventana):
        self.biblioteca_facade = BibliotecaFacade()
        self.ventana = ventana
        self.ventana.geometry("1200x700")
        self.ventana.config(background="#EDEAE0")
        self.divisor_principal = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_principal.grid(row=0, column=0)
        self.divisor_secundario = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_secundario.grid(row=0, column=1)
        self.interfaz_grafica()
    def interfaz_grafica(self):
        pass
class InterfazBibliotecario(InterfazGeneral):
    def __init__(self, ventana, bibliotecario):
        self.biblioteca_facade = BibliotecaFacade()
        self.ventana = ventana
        self.ventana.geometry("1200x700")
        self.ventana.config(background="#EDEAE0")
        self.divisor_principal = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_principal.grid(row=0, column=0)
        self.divisor_secundario = tk.Frame(self.ventana, background="#EDEAE0")
        self.divisor_secundario.grid(row=0, column=1)
        self.ventana.title("Gestor de Bibliotecas")
        self.bibliotecario = bibliotecario
        self.seccion_informacion = tk.Frame(self.divisor_principal, background="#EDEAE0")
        self.seccion_informacion.grid(row=0, column=0, sticky="nsew")
        self.seccion_usuarios = tk.Frame(self.divisor_principal, background="#EDEAE0")
        self.seccion_usuarios.grid(row=1, column=0, sticky="nsew")
        self.interfaz_grafica()
    def interfaz_grafica(self):
        tk.Label(
            self.seccion_informacion,
            text="Menu Bibliotecario",
            font=("Helvetica", 24),
            background="#EDEAE0"
        ).pack()
        tk.Label(
            self.seccion_informacion,
            text="Informacion del usuario",
            font=("Helvetica", 24),
            background="#EDEAE0"
        ).pack()
        self.informacion = tk.Label(
            self.seccion_informacion,
            text=self.biblioteca_facade.obtener_informacion_usuario(self.bibliotecario),
            font=("Helvetica", 12),
            background="#EDEAE0"
        )
        self.informacion.pack()
        tk.Label(
            self.seccion_usuarios,
            text="Seccion de usuarios",
            font=("Helvetica", 24), 
            background="#EDEAE0"
        ).grid(row=0, column=0, sticky="nsew")

        # Frame for teachers
        self.frame_docentes = tk.Frame(self.seccion_usuarios, background="#EDEAE0")
        self.frame_docentes.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        
        tk.Label(
            self.frame_docentes,
            text="Lista de Docentes",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        # Teachers Treeview with height limit
        self.treeview_docentes = ttk.Treeview(
            self.frame_docentes,
            columns=("id", "nombre", "identificacion", "id_profesional", "salario", "horario", "funciones", "limite", "multa"),
            show="headings",
            height=3  # Limit visible rows
        )
        
        # Configure teachers columns
        self.treeview_docentes.heading("id", text="ID")
        self.treeview_docentes.heading("nombre", text="Nombre")
        self.treeview_docentes.heading("identificacion", text="Identificación")
        self.treeview_docentes.heading("id_profesional", text="ID Profesional")
        self.treeview_docentes.heading("salario", text="Salario")
        self.treeview_docentes.heading("horario", text="Horario")
        self.treeview_docentes.heading("funciones", text="Funciones")
        self.treeview_docentes.heading("limite", text="Límite Préstamos")
        self.treeview_docentes.heading("multa", text="Tiene Multa")
        
        self.treeview_docentes.column("id", width=50)
        self.treeview_docentes.column("nombre", width=150)
        self.treeview_docentes.column("identificacion", width=100)
        self.treeview_docentes.column("id_profesional", width=100)
        self.treeview_docentes.column("salario", width=100)
        self.treeview_docentes.column("horario", width=100)
        self.treeview_docentes.column("funciones", width=150)
        self.treeview_docentes.column("limite", width=80)
        self.treeview_docentes.column("multa", width=70)
        
        self.treeview_docentes.pack(fill="x", padx=5, pady=5)
        
        # Frame for students
        self.frame_estudiantes = tk.Frame(self.seccion_usuarios, 
        background="#EDEAE0")
        self.frame_estudiantes.grid(row=2, 
        column=0, 
        padx=10, 
        pady=(0,5), 
        sticky="nsew")
        
        tk.Label(
            self.frame_estudiantes,
            text="Lista de Estudiantes",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        # Students Treeview with height limit
        self.treeview_estudiantes = ttk.Treeview(
            self.frame_estudiantes,
            columns=("id", "nombre", "identificacion", "matricula", "horas_sociales", "limite", "multa"),
            show="headings",
            height=3  # Limit visible rows
        )
        
        # Configure students columns
        self.treeview_estudiantes.heading("id", text="ID")
        self.treeview_estudiantes.heading("nombre", text="Nombre")
        self.treeview_estudiantes.heading("identificacion", text="Identificación")
        self.treeview_estudiantes.heading("matricula", text="N° Matrícula")
        self.treeview_estudiantes.heading("horas_sociales", text="Horas Sociales")
        self.treeview_estudiantes.heading("limite", text="Límite Préstamos")
        self.treeview_estudiantes.heading("multa", text="Tiene Multa")
        
        self.treeview_estudiantes.column("id", width=50)
        self.treeview_estudiantes.column("nombre", width=150)
        self.treeview_estudiantes.column("identificacion", width=100)
        self.treeview_estudiantes.column("matricula", width=100)
        self.treeview_estudiantes.column("horas_sociales", width=100)
        self.treeview_estudiantes.column("limite", width=80)
        self.treeview_estudiantes.column("multa", width=70)
        
        self.treeview_estudiantes.pack(fill="x", padx=5, pady=5)
        
        self.treeview_estudiantes.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.cargar_datos_treeviews()
        
    def cargar_datos_treeviews(self):
        # Clear existing items
        for item in self.treeview_docentes.get_children():
            self.treeview_docentes.delete(item)
        for item in self.treeview_estudiantes.get_children():
            self.treeview_estudiantes.delete(item)
            
        # Load teachers data
        docentes = self.biblioteca_facade.obtener_docentes()
        for docente in docentes:
            self.treeview_docentes.insert("", "end", values=(
                docente.obtener_id(),
                docente.obtener_nombre(),
                docente.obtener_identificacion(),
                docente.obtener_id_profesional(),
                f"${docente.obtener_salario():,.2f}",
                docente.obtener_horario(),
                docente.obtener_funciones(),
                docente.obtener_limite_prestamos(),
                "Sí" if docente.obtener_tiene_multa() else "No"
            ))
            
        # Load students data
        estudiantes = self.biblioteca_facade.obtener_estudiantes()
        for estudiante in estudiantes:
            self.treeview_estudiantes.insert("", "end", values=(
                estudiante.obtener_id(),
                estudiante.obtener_nombre(),
                estudiante.obtener_identificacion(),
                estudiante.obtener_numero_matricula(),
                estudiante.obtener_horas_sociales_asignadas(),
                estudiante.obtener_limite_prestamos(),
                "Sí" if estudiante.obtener_tiene_multa() else "No"
            ))
class InterfazUsuario(InterfazGeneral):
    def __init__(self,ventana,usuario):
        super().__init__(ventana)
        self.ventana.title("Ventana del usuario")
        self.usuario = usuario