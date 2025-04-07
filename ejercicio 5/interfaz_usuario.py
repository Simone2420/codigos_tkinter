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
        self.seccion_principal = tk.Frame(self.divisor_principal, background="#EDEAE0")
        self.seccion_principal.grid(row=1, column=0, sticky="nsew")
        self.dias_trasncurridos = 0
        self.interfaz_grafica()
        
    # Modify the method to handle the event
    def aumentar_dias(self):
        self.dias_trasncurridos += 1
        print("Space pressed - Updating dates")
        self.actualizar_informacion()
    def resetear_dias(self):
        self.dias_trasncurridos = 0
        self.actualizar_informacion()
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
        self.informacion_dias_trasncurridos = tk.Label(
            self.seccion_informacion,
            text=f"Dias transcurridos: {self.dias_trasncurridos}",
            font=("Helvetica", 9) 
        )
        self.informacion_dias_trasncurridos.pack()
        self.seccion_libros_para_prestamo = tk.Frame(self.seccion_principal, background="#EDEAE0")
        self.seccion_libros_para_prestamo.grid(row=0, column=0, sticky="nsew")
        #agregar tabla de libros para prestamo con filtro de libros disponibles
        self.tabla_libros_disponibles = ttk.Treeview(self.seccion_libros_para_prestamo, 
        columns=("ID", "Titulo", "Autor", "Año de publicacion","Categoria"), show="headings")
        for columna in self.tabla_libros_disponibles["columns"]:
            self.tabla_libros_disponibles.heading(columna, text=columna)
            self.tabla_libros_disponibles.column(columna, width=100)
        self.tabla_libros_disponibles.pack()
        self.tabla_libros_disponibles.config(height=5)
        #agregar boton para hacer prestamos
        self.boton_hacer_prestamo = tk.Button(
            self.seccion_libros_para_prestamo,
            text="Hacer prestamo",
            command=self.hacer_prestamo,
            background="#EDEAE0"
        )
        self.boton_hacer_prestamo.pack()
        self.seccion_libros_prestados = tk.Frame(self.seccion_principal, background="#EDEAE0")
        self.seccion_libros_prestados.grid(row=1, column=0, sticky="nsew")
        self.tabla_libros_prestados = ttk.Treeview(
            self.seccion_libros_prestados, 
            columns=("ID", "Titulo", "Autor", "Año de publicacion"
            ,"Categoria","Fecha de prestamo","Fecha de devolucion", "Fecha de devolucion reasignada"), 
            show="headings")
        self.tabla_libros_prestados.heading("ID", text="ID")
        self.tabla_libros_prestados.column("ID", width=50)
        self.tabla_libros_prestados.heading("Titulo", text="Titulo")
        self.tabla_libros_prestados.column("Titulo", width=80)
        self.tabla_libros_prestados.heading("Autor", text="Autor")
        self.tabla_libros_prestados.column("Autor", width=80)
        self.tabla_libros_prestados.heading("Año de publicacion", text="Año de publicacion")
        self.tabla_libros_prestados.column("Año de publicacion", width=70)
        self.tabla_libros_prestados.heading("Categoria", text="Categoria")
        self.tabla_libros_prestados.column("Categoria", width=70)
        self.tabla_libros_prestados.heading("Fecha de prestamo", text="Fecha de prestamo")
        self.tabla_libros_prestados.column("Fecha de prestamo", width=70)
        self.tabla_libros_prestados.heading("Fecha de devolucion", text="Fecha de devolucion")
        self.tabla_libros_prestados.column("Fecha de devolucion", width=70)
        self.tabla_libros_prestados.heading("Fecha de devolucion reasignada", text="Fecha de devolucion reasignada")
        self.tabla_libros_prestados.column("Fecha de devolucion reasignada", width=70)
        self.tabla_libros_prestados.pack()
        self.tabla_libros_prestados.config(height=5)
        #agregar boton para extender prestamo
        self.boton_extender_prestamo = tk.Button(
            self.seccion_libros_prestados,
            text="Extender prestamo",
            command=self.extender_prestamo 
        )
        self.boton_extender_prestamo.pack()
        
        self.boton_devolver_prestamo = tk.Button(
            self.seccion_libros_prestados,
            text="Devolver prestamo",
            command=self.devolver_prestamo
        )
        self.boton_devolver_prestamo.pack()
        
        self.seccion_multas = tk.Frame(self.divisor_secundario, background="#EDEAE0")
        self.seccion_multas.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        tk.Label(
            self.seccion_multas,
            text="Multas Pendientes",
            font=("Helvetica", 16),
            background="#EDEAE0"
        ).pack(pady=5)
        
        self.tabla_multas = ttk.Treeview(
            self.seccion_multas,
            columns=("ID", "Nombre Usuario", "Valor Multa"),
            show="headings",
            height=5
        )
        
        self.tabla_multas.heading("ID", text="ID")
        self.tabla_multas.column("ID", width=50)
        self.tabla_multas.heading("Nombre Usuario", text="Nombre Usuario")
        self.tabla_multas.column("Nombre Usuario", width=150)
        self.tabla_multas.heading("Valor Multa", text="Valor Multa")
        self.tabla_multas.column("Valor Multa", width=100)
        
        self.tabla_multas.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.boton_pagar_multa = tk.Button(
            self.seccion_multas,
            text="Pagar Multa",
            command=self.pagar_multa,
            background="#4CAF50",
            foreground="white"
        )
        self.boton_pagar_multa.pack(pady=10)
        self.ventana.bind('<space>', lambda event: self.aumentar_dias())
        self.ventana.bind('<r>', lambda event: self.resetear_dias())    
        self.actualizar_tablas()
        self.actualizar_informacion()
    def hacer_prestamo(self):
        seleccion = self.tabla_libros_disponibles.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Selecciona un producto para eliminar.")
            return
        if self.usuario.obtener_tipo() == "docente" and self.usuario.obtener_limite_prestamos() <= 0:
            messagebox.showwarning("Limite de prestamos", "No puedes tener mas de 3 prestamos activos.")
            return
        if self.usuario.obtener_tipo() == "estudiante" and self.usuario.obtener_limite_prestamos() <= 0:
            messagebox.showwarning("Limite de prestamos", "No puedes tener mas de 2 prestamos activos.")
            return
        if self.usuario.obtener_tiene_multa() == True:
            messagebox.showwarning("Multa", "No puedes puedes pedir prestado libros mientras tengas una multa.")
            return
        id_libro = self.tabla_libros_disponibles.item(seleccion[0], "values")[0]
        libro_obtenido = self.biblioteca_facade.buscar_libro_por_id(int(id_libro))
        self.biblioteca_facade.hacer_prestamo_libro(self.usuario,libro_obtenido)
        self.actualizar_informacion()
        self.actualizar_tablas()
    def extender_prestamo(self):
        seleccion = self.tabla_libros_prestados.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Selecciona un producto para eliminar.")
            return
        id_libro = self.tabla_libros_prestados.item(seleccion[0], "values")[0]
        prestamo_obtenido = self.biblioteca_facade.buscar_prestamo_por_id_libro(int(id_libro))
        libro_obtenido = self.biblioteca_facade.buscar_libro_por_id(int(id_libro))
        self.usuario,libro_obtenido = self.biblioteca_facade.extender_prestamo_libro(prestamo_obtenido,self.dias_trasncurridos,self.usuario)
        if self.usuario.obtener_tipo() == "docente":
            self.biblioteca_facade.actualizar_datos_docente(self.usuario)
        elif self.usuario.obtener_tipo() == "estudiante":
            self.biblioteca_facade.actualizar_datos_estudiante(self.usuario)
        self.biblioteca_facade.actualizar_datos_libro(libro_obtenido)
        self.actualizar_informacion()
        self.actualizar_tablas()
    def devolver_prestamo(self):
        seleccion = self.tabla_libros_prestados.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Selecciona un producto para eliminar.")
            return
        id_libro = self.tabla_libros_prestados.item(seleccion[0], "values")[0]
        prestamo_obtenido = self.biblioteca_facade.buscar_prestamo_por_id_libro(int(id_libro))
        self.usuario,libro_obtenido = self.biblioteca_facade.devolver_prestamo_libro(self.usuario,prestamo_obtenido,self.dias_trasncurridos)
        if self.usuario.obtener_tipo() == "docente":
            self.biblioteca_facade.actualizar_datos_docente(self.usuario)
        elif self.usuario.obtener_tipo() == "estudiante":
            self.biblioteca_facade.actualizar_datos_estudiante(self.usuario)
        self.biblioteca_facade.actualizar_datos_libro(libro_obtenido)
        self.actualizar_informacion()
        self.actualizar_tablas()
    def pagar_multa(self):
        seleccion = self.tabla_multas.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Selecciona una multa para pagar.")
            return
        id_prestamo = self.tabla_multas.item(seleccion[0], "values")[0]
        prestamo_encontrado = self.biblioteca_facade.buscar_prestamo_por_id(int(id_prestamo))
        self.biblioteca_facade.pagar_multa(prestamo_encontrado,self.usuario)
        self.actualizar_informacion()
        self.actualizar_tablas()
    def actualizar_informacion(self):
        self.informacion.config(text=self.biblioteca_facade.obtener_informacion_usuario(self.usuario))
        self.informacion_dias_trasncurridos.config(text=f"Dias transcurridos: {self.dias_trasncurridos}")
    def actualizar_tablas(self):
        for item in self.tabla_libros_disponibles.get_children():
            self.tabla_libros_disponibles.delete(item)
        for item in self.tabla_libros_prestados.get_children():
            self.tabla_libros_prestados.delete(item)
        for item in self.tabla_multas.get_children():
            self.tabla_multas.delete(item)
        
        libros_disponibles = self.biblioteca_facade.obtener_libros_disponibles()
        for libro in libros_disponibles:
            self.tabla_libros_disponibles.insert("", "end", values=(
                libro.obtener_id(),
                libro.obtener_titulo(),
                libro.obtener_autor(),
                libro.obtener_ano_publicacion(),
                libro.obtener_categoria()
            ))
        prestamos_activos = self.biblioteca_facade.obtener_prestamos_activos_usuario(self.usuario)
        for prestamo in prestamos_activos:
            self.tabla_libros_prestados.insert("", "end", values=(
                prestamo.obtener_libro().obtener_id(),
                prestamo.obtener_libro().obtener_titulo(),
                prestamo.obtener_libro().obtener_autor(),
                prestamo.obtener_libro().obtener_ano_publicacion(),
                prestamo.obtener_libro().obtener_categoria(),
                prestamo.obtener_fecha_prestamo(),
                prestamo.obtener_fecha_devolucion_esperada(),
                prestamo.obtener_fecha_reasignacion()
            ))
        
        prestamos_con_multas_pendientes = self.biblioteca_facade.obtener_restamos_con_multas_pendientes(self.usuario)
        for multa in prestamos_con_multas_pendientes:
            self.tabla_multas.insert("", "end", values=(
                multa.obtener_id(),
                multa.obtener_usuario().obtener_nombre(),
                multa.obtener_valor_a_pagar_multa()
            ))
        