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
        self.divisor_principal = tk.Frame(self.ventana)
        self.divisor_principal.pack(pady=10)
        self.divisor_secundario = tk.Frame(self.ventana)
        self.divisor_secundario.pack(pady=10)
        self.productos_almacenados = []
        self.interfaz_grafica()
        
    def interfaz_grafica(self):
        tk.Label(self.divisor_principal,text="Nombre producto").grid(row=0,column=0)
        self.nombre_producto = tk.Entry(self.divisor_principal)
        self.nombre_producto.grid(row=0,column=2)
        tk.Label(self.divisor_principal,text="Precio").grid(row=1,column=0)
        self.precio_producto = tk.Entry(self.divisor_principal)
        self.precio_producto.grid(row=1,column=2)
        tk.Label(self.divisor_principal,text="Cantidad").grid(row=2,column=0)
        self.cantidad_producto = tk.Entry(self.divisor_principal)
        self.cantidad_producto.grid(row=2,column=2)
        self.boton_agregar = tk.Button(self.divisor_principal,text="Agregar producto",command=self.agregar_producto)
        self.boton_agregar.grid(row=3,column=1)
        self.boton_eliminar = tk.Button(self.divisor_principal,text="Eliminar producto",command=self.eliminar_producto,state="disabled")
        self.boton_eliminar.grid(row=4,column=1)
        self.boton_editar = tk.Button(self.divisor_principal,text="Editar producto",command=self.editar_producto,state="disabled")
        self.boton_editar.grid(row=5,column=0)
        self.boton_guardar_edicion = tk.Button(self.divisor_principal,text="Guardar edición del producto",command=self.guardar_edicion_producto,state="disabled")
        self.boton_guardar_edicion.grid(row=5,column=2)
        self.boton_guardar = tk.Button(self.divisor_principal,text="Guardar",command=self.guardar_producto,state="disabled")
        self.boton_guardar.grid(row=6,column=0)
        self.boton_cargar = tk.Button(self.divisor_principal,text="Cargar",command=self.cargar_producto)
        self.boton_cargar.grid(row=6,column=2)
        self.tabla_productos = ttk.Treeview(self.divisor_secundario,columns=("Nombre", "Precio", "Cantidad", "Total"), show="headings")
        for col in ("Nombre", "Precio", "Cantidad", "Total"):
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
            self.productos_almacenados.append((nombre_producto, precio_producto, cantidad_producto, total))
            self.tabla_productos.insert("", "end", values=(nombre_producto, f"${precio_producto:.2f}", cantidad_producto, f"${total:.2f}"))
            self.boton_eliminar.config(state="normal")
            self.limpiar_entradas()
    def eliminar_producto(self):
        seleccion = self.tabla_productos.selection()
        for item in seleccion:
            valores = self.tabla_productos.item(item, "values")
            nombre = valores[0]
            self.productos = [p for p in self.productos_almacenados if p[0] != nombre]
            self.tabla_productos.delete(item)
            self.boton_eliminar.config(state="disabled")
        print(self.productos_almacenados)
    def guardar_producto(self): pass
    def cargar_producto(self): pass
    def editar_producto(self): pass
    def guardar_edicion_producto(self): pass
    def mostar_error_ingreso_datos(self): pass
    def limpiar_entradas(self): 
        self.nombre_producto.delete(0, tk.END)
        self.precio_producto.delete(0, tk.END)
        self.cantidad_producto.delete(0, tk.END)
app = InterfazInventario(ventana)
ventana.mainloop()