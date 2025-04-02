from conexion_base_datos import *
class ManejoProductos:
    def __init__(self,productos_registrados):
        self.productos_registrados = productos_registrados
        self.conexion = ConectorBasedeDatos()
    def registrar_datos_sin_sobrescritura(self):
        try:
            for producto in self.productos_almacenados:
                _, nombre, precio, cantidad, total = producto
                self.conexion.registrar_datos(nombre, precio, cantidad, total)
            return "Los productos se han guardado dinámicamente."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            conexion.cerrar_conexion()
    def registrar_datos_con_sobrescritura(self):
        try:
            self.conexion.cursor.execute("DELETE FROM productos")
            conexion.conexion.commit()
            for producto in self.productos_almacenados:
                _, nombre, precio, cantidad, total = producto
                conexion.registrar_datos(nombre, precio, cantidad, total)
            messagebox.showinfo("Guardado exitoso", "Los productos se han guardado con sobreescritura.")
        except Exception as e:
            messagebox.showerror("Error al guardar", f"Ocurrió un error: {e}")
        finally:
            conexion.cerrar_conexion()