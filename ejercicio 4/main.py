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
        tk.Label(self.divisor_principal,text="Nombre producto").grid(row=0,column=0)
        self.nombre_producto = tk.Entry(self.divisor_principal)
        self.nombre_producto.grid(row=0,column=1)
        tk.Label(self.divisor_principal,text="Precio").grid(row=1,column=0)
        self.precio_producto = tk.Entry(self.divisor_principal)
        self.precio_producto.grid(row=1,column=1)
        tk.Label(self.divisor_principal,text="Cantidad").grid(row=2,column=0)
        self.cantidad_producto = tk.Entry(self.divisor_principal)
        self.cantidad_producto.grid(row=2,column=1)
        self.boton_agregar = tk.Button(self.divisor_principal,text="Agregar producto",command=self.agregar_producto)
        self.boton_agregar.grid(row=3,column=1,columnspan=3)
        self.boton_eliminar = tk.Button(self.divisor_principal,text="Eliminar producto",command=self.eliminar_producto,state="disabled")
        self.boton_eliminar.grid(row=4,column=1,columnspan=3)
        self.boton_editar = tk.Button(self.divisor_principal,text="Editar producto",command=self.editar_producto,state="disabled")
        self.boton_editar.grid(row=5,column=0)
        self.boton_guardar_edicion = tk.Button(self.divisor_principal,text="Guardar edición del producto",command=self.guardar_edicion_producto,state="disabled")
        self.boton_guardar_edicion.grid(row=5,column=1)
        self.boton_guardar = tk.Button(self.divisor_principal,text="Guardar",command=self.guardar_producto,state="disabled")
        self.boton_guardar.grid(row=6,column=0)
        self.boton_cargar = tk.Button(self.divisor_principal,text="Cargar",command=self.cargar_producto)
        self.boton_cargar.grid(row=6,column=1)
        self.tabla_productos = ttk.Treeview(self.divisor_secundario,columns=("Indice","Nombre", "Precio", "Cantidad", "Total"), show="headings")
        for col in ("Indice","Nombre", "Precio", "Cantidad", "Total"):
            self.tabla_productos.heading(col, text=col)
        self.tabla_productos.pack()
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
    # Mostrar una ventana emergente con dos opciones
        opcion = messagebox.askquestion(
            "Guardar producto",
            "¿Cómo desea guardar los productos?\n\n"
            "Seleccione 'Sí' para guardar dinámicamente (agregar a los datos existentes).\n"
            "Seleccione 'No' para sobrescribir los datos existentes."
        )

        if opcion == "yes":  # Guardado dinámico
                self.manejo_productos = ManejoProductos(self.productos_almacenados)
                mensaje = self.manejo_productos.registrar_datos_sin_sobrescritura()
                if mensaje == "Los productos se han guardado dinámicamente.":
                    messagebox.showinfo("Guardado exitoso", mensaje)
                else:
                    messagebox.showerror("Error al guardar", mensaje)

        elif opcion == "no":  
            try:
                conexion = ConectorBasedeDatos()
                conexion.cursor.execute("DELETE FROM productos")
                conexion.conexion.commit()
                for producto in self.productos_almacenados:
                    _, nombre, precio, cantidad, total = producto
                    conexion.registrar_datos(nombre, precio, cantidad, total)
                messagebox.showinfo("Guardado exitoso", "Los productos se han guardado con sobreescritura.")
            except Exception as e:
                messagebox.showerror("Error al guardar", f"Ocurrió un error: {e}")
            finally:
                conexion.cerrar_conexion()
    def cargar_producto(self): pass
    def editar_producto(self):
        seleccionado = self.tabla_productos.selection()
        item = self.tabla_productos.item(seleccionado[0])
        indice,nombre,precio,cantidad,_ = item["values"]
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