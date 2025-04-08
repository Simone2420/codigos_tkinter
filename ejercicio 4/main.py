import tkinter as tk
from tkinter import messagebox, ttk
from excepciones import *
from conexion_base_datos import *
from manejo_productos import *
ventana = tk.Tk()
class InterfazInventario:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("1000x600")
        self.ventana.title("Gestor de inventarios")
        self.ventana.config(background="#EDEAE0")
        self.divisor_principal = tk.Frame(self.ventana)
        self.divisor_principal.grid(row=0,column=0,sticky="n")
        self.divisor_principal.config(background="#EDEAE0")
        self.divisor_secundario = tk.Frame(self.ventana)
        self.divisor_secundario.grid(row=1,column=0)
        self.productos_almacenados = []
        self.interfaz_grafica()
    def interfaz_grafica(self):
        # Frame contenedor para los campos de entrada
        frame_entradas = tk.Frame(self.divisor_principal, bg="#EDEAE0", padx=20, pady=10)
        frame_entradas.grid(row=0, column=0, sticky="nsew")

        # Estilo para las etiquetas
        estilo_label = {"bg": "#EDEAE0", "font": ("Arial", 11), "pady": 5}

        # Campos de entrada con etiquetas
        tk.Label(frame_entradas, text="Nombre producto", **estilo_label).grid(row=0, column=0, padx=10, pady=5)
        self.nombre_producto = tk.Entry(frame_entradas, font=("Arial", 10), width=25)
        self.nombre_producto.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_entradas, text="Precio", **estilo_label).grid(row=1, column=0, padx=10, pady=5)
        self.precio_producto = tk.Entry(frame_entradas, font=("Arial", 10), width=25)
        self.precio_producto.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_entradas, text="Cantidad", **estilo_label).grid(row=2, column=0, padx=10, pady=5)
        self.cantidad_producto = tk.Entry(frame_entradas, font=("Arial", 10), width=25)
        self.cantidad_producto.grid(row=2, column=1, padx=10, pady=5)

        # Frame para los botones
        frame_botones = tk.Frame(self.divisor_principal, bg="#EDEAE0", padx=20, pady=10)
        frame_botones.grid(row=1, column=0, sticky="nsew")

        # Estilo común para los botones
        estilo_boton = {
            "font": ("Arial", 10),
            "borderwidth": 0,
            "relief": "flat",
            "padx": 15,
            "pady": 8,
            "cursor": "hand2"
        }

        # Botones principales
        self.boton_agregar = tk.Button(frame_botones, text="Agregar producto", command=self.agregar_producto,
                                    bg="#4CAF50", fg="white", **estilo_boton)
        self.boton_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_eliminar = tk.Button(frame_botones, text="Eliminar producto", command=self.eliminar_producto,
                                      bg="#f44336", fg="white", state="disabled", **estilo_boton)
        self.boton_eliminar.grid(row=0, column=1, padx=5, pady=5)

        self.boton_editar = tk.Button(frame_botones, text="Editar producto", command=self.editar_producto,
                                    bg="#2196F3", fg="white", state="disabled", **estilo_boton)
        self.boton_editar.grid(row=1, column=0, padx=5, pady=5)

        self.boton_guardar_edicion = tk.Button(frame_botones, text="Guardar edición", command=self.guardar_edicion_producto,
                                              bg="#4CAF50", fg="white", state="disabled", **estilo_boton)
        self.boton_guardar_edicion.grid(row=1, column=1, padx=5, pady=5)

        self.boton_guardar = tk.Button(frame_botones, text="Guardar", command=self.guardar_producto,
                                      bg="#9C27B0", fg="white", state="disabled", **estilo_boton)
        self.boton_guardar.grid(row=2, column=0, padx=5, pady=5)

        self.boton_cargar = tk.Button(frame_botones, text="Cargar", command=self.cargar_producto,
                                     bg="#FF9800", fg="white", **estilo_boton)
        self.boton_cargar.grid(row=2, column=1, padx=5, pady=5)

        # Tabla de productos
        self.tabla_productos = ttk.Treeview(self.divisor_secundario,
                                          columns=("Indice", "Nombre", "Precio", "Cantidad", "Total"),
                                          show="headings",
                                          height=10)

        # Configuración de las columnas de la tabla
        for col in ("Indice", "Nombre", "Precio", "Cantidad", "Total"):
            self.tabla_productos.heading(col, text=col)
            self.tabla_productos.column(col, width=100)

        self.tabla_productos.pack(padx=20, pady=20, fill="both", expand=True)
    def agregar_producto(self):
        try:
            nombre_producto = self.nombre_producto.get().strip()
            if nombre_producto == "":
                raise NombreVacio("El nombre no debe ser vacio")
            precio_producto = float(self.precio_producto.get())
            cantidad_producto = int(self.cantidad_producto.get())
        except NombreVacio:
            messagebox.showerror("Nombre no debe ser vacio","Nombre no debe ser vacio")
        except ValueError:
            messagebox.showerror("Error de ingreso de datos","Por favor ingrese valores numericos enteros para cantidad y valores decimales para el precio")
        finally:
            total = precio_producto * cantidad_producto
            indice = len(self.productos_almacenados) + 1
            self.productos_almacenados.append((indice,nombre_producto, precio_producto, cantidad_producto, total))
            self.tabla_productos.insert("", "end", values=(indice,nombre_producto, f"${precio_producto:.2f}", cantidad_producto, f"${total:.2f}"))
            self.boton_eliminar.config(state="normal")
            self.boton_editar.config(state="normal")
            self.boton_guardar.config(state="normal")
            self.limpiar_entradas()
    def eliminar_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Selecciona un producto para eliminar.")
            return
        for item in seleccion:
            valores = self.tabla_productos.item(item, "values")
            indice = int(valores[0])
            self.productos_almacenados.pop(indice-1)
            self.tabla_productos.delete(item)
        self.actualizar_indices()
    def guardar_producto(self):
    # Usar askyesnocancel que devuelve True (Sí), False (No) o None (Cancelar)
        opcion = messagebox.askyesnocancel(
            "Guardar producto",
            "¿Cómo desea guardar los productos?\n\n"
            "Seleccione 'Sí' para guardar dinámicamente (agregar a los datos existentes).\n"
            "Seleccione 'No' para sobrescribir los datos existentes.\n"
            "Seleccione 'Cancelar' para no guardar."
        )
    
        # Si el usuario cierra la ventana o presiona Cancelar
        if opcion is None:
            return  # No hacer nada
            
        if opcion is True:  # Guardado dinámico (Sí)
            self.manejo_productos = ManejoProductos(self.productos_almacenados)
            mensaje = self.manejo_productos.registrar_datos_sin_sobrescritura()
            if mensaje == "Los productos se han guardado dinámicamente.":
                messagebox.showinfo("Guardado exitoso", mensaje)
            else:
                messagebox.showerror("Error al guardar", mensaje)
            self.productos_almacenados.clear()
            self.actualizar_indices()
            
        elif opcion is False:  # Sobrescritura (No)
            self.manejo_productos = ManejoProductos(self.productos_almacenados)
            mensaje = self.manejo_productos.registrar_datos_con_sobrescritura()
            if mensaje == "Los productos se han guardado con sobreescritura.":
                messagebox.showinfo("Guardado exitoso", mensaje)
            else:
                messagebox.showerror("Error al guardar", mensaje)
            self.productos_almacenados.clear()
            self.actualizar_indices()
    def cargar_producto(self):
        # Crear una instancia de ManejoProductos sin productos
        gestor_productos = ManejoProductos()

        # Cargar productos desde la base de datos
        productos_bd, mensaje = gestor_productos.cargar_productos_desde_bd()

        if not productos_bd:
            messagebox.showinfo("Información", mensaje if "error" in mensaje.lower() else "No hay productos para cargar.")
            return

        # Limpiar tabla y lista actual
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        self.productos_almacenados.clear()

        # Agregar productos cargados a la lista y tabla
        for producto in productos_bd:
            id_bd, nombre, precio, cantidad, total = producto
            # Agregar a la lista con índice basado en la posición
            indice = len(self.productos_almacenados) + 1
            self.productos_almacenados.append((indice, nombre, precio, cantidad, total))
            # Agregar a la tabla
            self.tabla_productos.insert("", "end", values=(indice, nombre, f"${precio:.2f}", cantidad, f"${total:.2f}"))

        if productos_bd:
            messagebox.showinfo("Carga exitosa", f"Se han cargado {len(productos_bd)} productos.")
            # Activar botones relevantes
            self.boton_eliminar.config(state="normal")
            self.boton_editar.config(state="normal")
            self.boton_guardar.config(state="normal")
    def editar_producto(self):
        seleccionado = self.tabla_productos.selection()
        item = self.tabla_productos.item(seleccionado[0])
        _,nombre,precio,cantidad,_ = item["values"]
        self.nombre_producto.delete(0, tk.END)
        self.nombre_producto.insert(0, nombre)
        self.precio_producto.delete(0, tk.END)
        self.precio_producto.insert(0, precio.replace("$", ""))
        self.cantidad_producto.delete(0, tk.END)
        self.cantidad_producto.insert(0, cantidad)
        self.boton_agregar.config(state='disabled')
        self.boton_guardar_edicion.config(state='normal')
    def guardar_edicion_producto(self):
        try:
            nombre_producto = self.nombre_producto.get().strip()
            if nombre_producto == "":
                raise NombreVacio("El nombre no debe ser vacio")
            precio_producto = float(self.precio_producto.get())
            cantidad_producto = int(self.cantidad_producto.get())
            if not precio_producto or not cantidad_producto:
                messagebox.showerror("Datos precio y cantidad","Deben ingresarse los datos de precio y cantidad")
        except NombreVacio:
            messagebox.showerror("Nombre no debe ser vacio","Nombre no debe ser vacio")
        except ValueError:
            messagebox.showerror("Error de ingreso de datos","Por favor ingrese valores numericos enteros para cantidad y valores decimales para el precio")
        finally:
            seleccionado = self.tabla_productos.selection()
            item = self.tabla_productos.item(seleccionado[0])
            indice,_,_,_,_ = item["values"]
            total = precio_producto * cantidad_producto
            # Actualizamos el producto editado con su índice
            for i, producto in enumerate(self.productos_almacenados):
                if producto[0] == indice:  # Encontramos el índice correspondiente
                    self.productos_almacenados[i] = (indice, nombre_producto, precio_producto, cantidad_producto, total)
            self.actualizar_indices()
            self.limpiar_entradas()
            self.boton_agregar.config(state="normal")
    def mostar_error_ingreso_datos(self): pass
    def limpiar_entradas(self): 
        self.nombre_producto.delete(0, tk.END)
        self.precio_producto.delete(0, tk.END)
        self.cantidad_producto.delete(0, tk.END)
    def actualizar_indices(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)
        for indice, producto in enumerate(self.productos_almacenados):
            _,nombre, precio, cantidad, total = producto
            self.tabla_productos.insert("", "end", values=(indice + 1, nombre, f"${precio:.2f}", cantidad, f"${total:.2f}"))
app = InterfazInventario(ventana)
ventana.mainloop()