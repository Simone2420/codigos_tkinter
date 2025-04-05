import tkinter as tk
from tkinter import messagebox, ttk
from biblioteca_facade import BibliotecaFacade
from modelos.excepciones import *
class InterfazBibliotecario:
    def __init__(self, ventana, bibliotecario):
        self.biblioteca_facade = BibliotecaFacade()
        self.ventana = ventana
        self.ventana.geometry("1400x700")
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
            font=("Helvetica", 18), 
            background="#EDEAE0"
        ).grid(row=0, column=0, sticky="nsew")

        self.seccion_docentes = tk.Frame(self.seccion_usuarios, background="#EDEAE0")
        self.seccion_docentes.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        
        tk.Label(
            self.seccion_docentes,
            text="Lista de Docentes",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_docentes = ttk.Treeview(
            self.seccion_docentes,
            columns=("id", "nombre", "identificacion", "id_profesional", "salario", "horario", "funciones", "limite", "multa"),
            show="headings",
            height=3  
        )
        
        self.tabla_docentes.heading("id", text="ID")
        self.tabla_docentes.heading("nombre", text="Nombre")
        self.tabla_docentes.heading("identificacion", text="Identificación")
        self.tabla_docentes.heading("id_profesional", text="ID Profesional")
        self.tabla_docentes.heading("salario", text="Salario")
        self.tabla_docentes.heading("horario", text="Horario")
        self.tabla_docentes.heading("funciones", text="Funciones")
        self.tabla_docentes.heading("limite", text="Límite Préstamos")
        self.tabla_docentes.heading("multa", text="Tiene Multa")
        
        self.tabla_docentes.column("id", width=25)
        self.tabla_docentes.column("nombre", width=100)
        self.tabla_docentes.column("identificacion", width=80)
        self.tabla_docentes.column("id_profesional", width=70)
        self.tabla_docentes.column("salario", width=90)
        self.tabla_docentes.column("horario", width=60)
        self.tabla_docentes.column("funciones", width=85)
        self.tabla_docentes.column("limite", width=70)
        self.tabla_docentes.column("multa", width=65)
        
        self.tabla_docentes.pack(fill="x", padx=5, pady=5)

        # Botón para agregar docente
        tk.Button(
            self.seccion_docentes,
            text="Agregar Docente",
            command=self.agregar_docente,
            background="#4CAF50",
            foreground="white"
        ).pack(pady=10)

        self.seccion_estudiantes = tk.Frame(self.seccion_usuarios, background="#EDEAE0")
        self.seccion_estudiantes.grid(row=2, 
        column=0, 
        padx=10, 
        pady=(0,5), 
        sticky="nsew")
        
        tk.Label(
            self.seccion_estudiantes,
            text="Lista de Estudiantes",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_estudiantes = ttk.Treeview(
            self.seccion_estudiantes,
            columns=("id", "nombre", "identificacion", "matricula", "horas_sociales", "limite", "multa"),
            show="headings",
            height=3 
        )

        self.tabla_estudiantes.heading("id", text="ID")
        self.tabla_estudiantes.heading("nombre", text="Nombre")
        self.tabla_estudiantes.heading("identificacion", text="Identificación")
        self.tabla_estudiantes.heading("matricula", text="N° Matrícula")
        self.tabla_estudiantes.heading("horas_sociales", text="Horas Sociales")
        self.tabla_estudiantes.heading("limite", text="Límite Préstamos")
        self.tabla_estudiantes.heading("multa", text="Tiene Multa")
        
        self.tabla_estudiantes.column("id", width=50)
        self.tabla_estudiantes.column("nombre", width=150)
        self.tabla_estudiantes.column("identificacion", width=100)
        self.tabla_estudiantes.column("matricula", width=100)
        self.tabla_estudiantes.column("horas_sociales", width=100)
        self.tabla_estudiantes.column("limite", width=80)
        self.tabla_estudiantes.column("multa", width=70)
        
        self.tabla_estudiantes.pack(fill="x", padx=5, pady=5)
        
        self.tabla_estudiantes.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botón para agregar estudiante
        tk.Button(
            self.seccion_estudiantes,
            text="Agregar Estudiante",
            command=self.agregar_estudiante,
            background="#4CAF50",
            foreground="white"
        ).pack(pady=10)
        self.seccion_libros = tk.Frame(self.divisor_secundario, background="#EDEAE0")
        self.seccion_libros.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        tk.Label(
            self.seccion_libros,
            text="Lista de Libros",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_libros = ttk.Treeview(
            self.seccion_libros,
            columns=("id", "titulo", "autor", "año_publicacion", "categoria"),
            show="headings",
            height=5
        )
        
        self.tabla_libros.heading("id", text="ID")
        self.tabla_libros.heading("titulo", text="Título")
        self.tabla_libros.heading("autor", text="Autor")
        self.tabla_libros.heading("año_publicacion", text="Año Publicación")
        self.tabla_libros.heading("categoria", text="Categoria")
        
        self.tabla_libros.column("id", width=50)
        self.tabla_libros.column("titulo", width=100)
        self.tabla_libros.column("autor", width=140)
        self.tabla_libros.column("año_publicacion", width=70)
        self.tabla_libros.column("categoria", width=80)
        
        self.tabla_libros.pack(fill="both", expand=True, padx=5, pady=5)
        
        tk.Button(
            self.seccion_libros,
            text="Agregar Libro",
            command=self.agregar_libro,
            background="#4CAF50",
            foreground="white"
        ).pack(pady=10)
        
        # Sección de préstamos activos
        self.seccion_prestamos = tk.Frame(self.divisor_secundario, background="#EDEAE0")
        self.seccion_prestamos.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        tk.Label(
            self.seccion_prestamos,
            text="Préstamos Activos",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_prestamos_activos = ttk.Treeview(
            self.seccion_prestamos,
            columns=("id", "nombre_usuario", "id_usuario", "tipo_usuario", "titulo_libro", "fecha_prestamo", "fecha_devolucion", "fecha_reasignada"),
            show="headings",
            height=5
        )
        
        self.tabla_prestamos_activos.heading("id", text="ID Préstamo")
        self.tabla_prestamos_activos.heading("nombre_usuario", text="Nombre Usuario")
        self.tabla_prestamos_activos.heading("id_usuario", text="ID Usuario")
        self.tabla_prestamos_activos.heading("tipo_usuario", text="Tipo Usuario")
        self.tabla_prestamos_activos.heading("titulo_libro", text="Título Libro")
        self.tabla_prestamos_activos.heading("fecha_prestamo", text="Fecha Préstamo")
        self.tabla_prestamos_activos.heading("fecha_devolucion", text="Fecha Devolución")
        self.tabla_prestamos_activos.heading("fecha_reasignada", text="Fecha Reasignada")
        
        self.tabla_prestamos_activos.column("id", width=50)
        self.tabla_prestamos_activos.column("nombre_usuario", width=80)
        self.tabla_prestamos_activos.column("id_usuario", width=50)
        self.tabla_prestamos_activos.column("tipo_usuario", width=60)
        self.tabla_prestamos_activos.column("titulo_libro", width=85)
        self.tabla_prestamos_activos.column("fecha_prestamo", width=80)
        self.tabla_prestamos_activos.column("fecha_devolucion", width=80)
        self.tabla_prestamos_activos.column("fecha_reasignada", width=80)
        
        self.tabla_prestamos_activos.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Sección de historial de préstamos
        tk.Label(
            self.seccion_prestamos,
            text="Historial de Préstamos",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_historial = ttk.Treeview(
            self.seccion_prestamos,
            columns=("id", "nombre_usuario", "id_usuario", "tipo_usuario", "titulo_libro", "fecha_prestamo", "fecha_devolucion", "fecha_reasignada", "estado", "multa"),
            show="headings",
            height=5
        )
        
        self.tabla_historial.heading("id", text="ID Préstamo")
        self.tabla_historial.heading("nombre_usuario", text="Nombre Usuario")
        self.tabla_historial.heading("id_usuario", text="ID Usuario")
        self.tabla_historial.heading("tipo_usuario", text="Tipo Usuario")
        self.tabla_historial.heading("titulo_libro", text="Título Libro")
        self.tabla_historial.heading("fecha_prestamo", text="Fecha Préstamo")
        self.tabla_historial.heading("fecha_devolucion", text="Fecha Devolución")
        self.tabla_historial.heading("fecha_reasignada", text="Fecha Reasignada")
        self.tabla_historial.heading("estado", text="Estado")
        self.tabla_historial.heading("multa", text="Multa")
        
        self.tabla_historial.column("id", width=50)
        self.tabla_historial.column("nombre_usuario", width=80)
        self.tabla_historial.column("id_usuario", width=50)
        self.tabla_historial.column("tipo_usuario", width=60)
        self.tabla_historial.column("titulo_libro", width=85)
        self.tabla_historial.column("fecha_prestamo", width=75)
        self.tabla_historial.column("fecha_devolucion", width=75)
        self.tabla_historial.column("fecha_reasignada", width=75)
        self.tabla_historial.column("estado", width=50)
        self.tabla_historial.column("multa", width=40)
        
        self.tabla_historial.pack(fill="both", expand=True, padx=5, pady=5)

        self.boton_cerrar_sesion = tk.Button(
            self.seccion_prestamos,
            text="Cerrar Sesión",
            command=self.cerrar_sesion,
            background="#FF4444",
            foreground="white",
            font=("Helvetica", 12)
        )
        self.boton_cerrar_sesion.pack(pady=20)
        self.cargar_tablas()
    def cargar_tablas(self):
        # Clear existing items
        for item in self.tabla_docentes.get_children():
            self.tabla_docentes.delete(item)
        for item in self.tabla_estudiantes.get_children():
            self.tabla_estudiantes.delete(item)
        for item in self.tabla_libros.get_children():
            self.tabla_libros.delete(item)
        for item in self.tabla_prestamos_activos.get_children():
            self.tabla_prestamos_activos.delete(item)
        for item in self.tabla_historial.get_children():
            self.tabla_historial.delete(item)
            
        docentes = self.biblioteca_facade.obtener_docentes()
        for docente in docentes:
            self.tabla_docentes.insert("", "end", values=(
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
            self.tabla_estudiantes.insert("", "end", values=(
                estudiante.obtener_id(),
                estudiante.obtener_nombre(),
                estudiante.obtener_identificacion(),
                estudiante.obtener_numero_matricula(),
                estudiante.obtener_horas_sociales_asignadas(),
                estudiante.obtener_limite_prestamos(),
                "Sí" if estudiante.obtener_tiene_multa() else "No"
            ))

        # Load books data
        libros = self.biblioteca_facade.obtener_libros()
        for libro in libros:
            self.tabla_libros.insert("", "end", values=(
                libro.obtener_id(),
                libro.obtener_titulo(),
                libro.obtener_autor(),
                libro.obtener_ano_publicacion(),
                libro.obtener_categoria()
            ))
            
        # Cargar préstamos activos
        prestamos_activos = self.biblioteca_facade.obtener_prestamos_activos()
        for prestamo in prestamos_activos:
            self.tabla_prestamos_activos.insert("", "end", values=(
                prestamo.obtener_id(),
                prestamo.obtener_usuario().obtener_nombre(),
                prestamo.obtener_usuario().obtener_id(),
                prestamo.obtener_usuario().obtener_tipo_usuario(),
                prestamo.obtener_libro().obtener_titulo(),
                prestamo.obtener_fecha_prestamo(),
                prestamo.obtener_fecha_devolucion(),
                prestamo.obtener_fecha_reasignada()
            ))
            
        # Cargar historial de préstamos
        historial_prestamos = self.biblioteca_facade.obtener_historial_prestamos()
        for prestamo in historial_prestamos:
            self.tabla_historial.insert("", "end", values=(
                prestamo.obtener_id(),
                prestamo.obtener_usuario().obtener_nombre(),
                prestamo.obtener_usuario().obtener_id(),
                prestamo.obtener_tipo_usuario(),
                prestamo.obtener_libro().obtener_titulo(),
                prestamo.obtener_fecha_prestamo(),
                prestamo.obtener_fecha_devolucion(),
                prestamo.obtener_fecha_reasignada(),
                prestamo.obtener_estado(),
                prestamo.obtener_multa()
            ))
    def cerrar_sesion(self):
        self.ventana.destroy()
        ventana_login = tk.Tk()
        from interfaz_login import LoginBiblioteca
        LoginBiblioteca(ventana_login)
        ventana_login.mainloop()
    def agregar_libro(self):
        # Crear ventana emergente para agregar libro
        ventana_libro = tk.Toplevel(self.ventana)
        ventana_libro.title("Agregar Libro")
        ventana_libro.geometry("400x350")
        ventana_libro.config(background="#EDEAE0")
    
        # Crear campos de entrada
        tk.Label(ventana_libro, text="Título:", background="#EDEAE0").pack(pady=5)
        titulo = tk.Entry(ventana_libro)
        titulo.pack(pady=5)
    
        tk.Label(ventana_libro, text="Autor:", background="#EDEAE0").pack(pady=5)
        autor = tk.Entry(ventana_libro)
        autor.pack(pady=5)
        tk.Label(ventana_libro, text="Año de publicación:", background="#EDEAE0").pack(pady=5)
        ano_publicacion = tk.Entry(ventana_libro)
        ano_publicacion.pack(pady=5)
        tk.Label(ventana_libro, text="Género:", background="#EDEAE0").pack(pady=5)

        categoria = ttk.Combobox(ventana_libro, values=["Literatura","Novela","Realismo","Ciencia Ficción"])
        categoria.pack(pady=5)
        
        tk.Button(
            ventana_libro,
            text="Guardar",
            command=lambda: self._guardar_libro(ventana_libro, titulo, autor, ano_publicacion , categoria),
            background="#4CAF50",
            foreground="white"
        ).pack(pady=20)

    def _guardar_libro(self, ventana_libro, titulo, autor, ano_publicacion, categoria):
        try:
            # Validar campos
            if not titulo.get() or not autor.get() or not ano_publicacion.get() or not categoria.get():
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            # Crear libro
            self.biblioteca_facade.registrar_libro(
                titulo.get(),
                autor.get(),
                ano_publicacion.get(),
                categoria.get()
                
            )
            
            messagebox.showinfo("Éxito", "Libro registrado correctamente")
            self.cargar_tablas()
            ventana_libro.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def agregar_estudiante(self):
        # Crear ventana emergente para agregar estudiante
        ventana_estudiante = tk.Toplevel(self.ventana)
        ventana_estudiante.title("Agregar Estudiante")
        ventana_estudiante.geometry("400x300")
        ventana_estudiante.config(background="#EDEAE0")
    
        # Crear campos de entrada
        tk.Label(ventana_estudiante, text="Nombre:", background="#EDEAE0").pack(pady=5)
        nombre = tk.Entry(ventana_estudiante)
        nombre.pack(pady=5)
    
        tk.Label(ventana_estudiante, text="Identificación:", background="#EDEAE0").pack(pady=5)
        identificacion = tk.Entry(ventana_estudiante)
        identificacion.pack(pady=5)
    
        tk.Label(ventana_estudiante, text="Número de Matrícula:", background="#EDEAE0").pack(pady=5)
        matricula = tk.Entry(ventana_estudiante)
        matricula.pack(pady=5)
        tk.Button(
            ventana_estudiante,
            text="Guardar",
            command=lambda: self._guardar_estudiante(ventana_estudiante,nombre,identificacion,matricula),
            background="#4CAF50",
            foreground="white"
        ).pack(pady=20)
    def _guardar_estudiante(self,ventana_estudiante,nombre,identificacion,matricula):
        try:
            # Validar campos
            if not nombre.get() or not identificacion.get() or not matricula.get():
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            # Crear estudiante
            vefificador = self.biblioteca_facade.registrar_estudiante(
                nombre.get(),
                int(identificacion.get()),
                matricula.get()
            )
            if isinstance(vefificador,DatosInvalidos):
                messagebox.showerror("Error", str(vefificador))
                return
            else:
                messagebox.showinfo("Éxito", "Estudiante registrado correctamente")
                self.cargar_tablas()
            ventana_estudiante.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def agregar_docente(self):
        # Crear ventana emergente para agregar docente
        ventana_docente = tk.Toplevel(self.ventana)
        ventana_docente.title("Agregar Docente")
        ventana_docente.geometry("400x450")
        ventana_docente.config(background="#EDEAE0")
    
        # Crear campos de entrada
        tk.Label(ventana_docente, text="Nombre:", background="#EDEAE0").pack(pady=5)
        nombre = tk.Entry(ventana_docente)
        nombre.pack(pady=5)
    
        tk.Label(ventana_docente, text="Identificación:", background="#EDEAE0").pack(pady=5)
        identificacion = tk.Entry(ventana_docente)
        identificacion.pack(pady=5)
    
        tk.Label(ventana_docente, text="ID Profesional:", background="#EDEAE0").pack(pady=5)
        id_profesional = tk.Entry(ventana_docente)
        id_profesional.pack(pady=5)
    
        tk.Label(ventana_docente, text="Salario:", background="#EDEAE0").pack(pady=5)
        salario = tk.Entry(ventana_docente)
        salario.pack(pady=5)
    
        tk.Label(ventana_docente, text="Horario:", background="#EDEAE0").pack(pady=5)
        horario = tk.Entry(ventana_docente)
        horario.pack(pady=5)
    
        tk.Label(ventana_docente, text="Funciones:", background="#EDEAE0").pack(pady=5)
        funciones = tk.Entry(ventana_docente)
        funciones.pack(pady=5)
        tk.Button(
            ventana_docente,
            text="Guardar",
            command=lambda: self._guardar_docente(ventana_docente,nombre,identificacion,id_profesional,salario,horario,funciones),
            background="#4CAF50",
            foreground="white"
        ).pack(pady=20)
    def _guardar_docente(self,ventana_docente,nombre,identificacion,id_profesional,salario,horario,funciones):
            try:
                # Validar campos
                if not all([nombre.get(), identificacion.get(), id_profesional.get(),
                        salario.get(), horario.get(), funciones.get()]):
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return
    
                # Validar que salario sea un número
                try:
                    float(salario.get())
                except ValueError:
                    messagebox.showerror("Error", "El salario debe ser un número")
                    return
    
                
                verificador = self.biblioteca_facade.registrar_docente(
                    nombre.get(),
                    identificacion.get(),
                    id_profesional.get(),
                    horario.get(),
                    float(salario.get()),
                    funciones.get()
                )
                if isinstance(verificador,DatosInvalidos):
                    messagebox.showerror("Error", str(verificador))
                    return
                else:
                    messagebox.showinfo("Éxito", "Docente registrado correctamente")
                    self.cargar_tablas()
                ventana_docente.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
