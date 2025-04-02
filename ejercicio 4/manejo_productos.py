# Fix for manejo_productos.py
from conexion_base_datos import *

class ManejoProductos:
    def __init__(self, productos_registrados=None):
        if productos_registrados is None:
            productos_registrados = []
        self.productos_registrados = productos_registrados
        self.conexion = ConectorBasedeDatos()
    
    def registrar_datos_sin_sobrescritura(self):
        try:
            if self.conexion.error:
                return f"Error de conexión a la base de datos: {self.conexion.error}"
            
            for producto in self.productos_registrados:
                _, nombre, precio, cantidad, total = producto
                self.conexion.registrar_datos(nombre, precio, cantidad, total)
            return "Los productos se han guardado dinámicamente."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            self.conexion.cerrar_conexion()
    
    def registrar_datos_con_sobrescritura(self):
        try:
            if self.conexion.error:
                return f"Error de conexión a la base de datos: {self.conexion.error}"
                
            self.conexion.cursor.execute("DELETE FROM productos")
            self.conexion.conexion.commit()
            
            for producto in self.productos_registrados:
                _, nombre, precio, cantidad, total = producto
                self.conexion.registrar_datos(nombre, precio, cantidad, total)
            return "Los productos se han guardado con sobreescritura."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            self.conexion.cerrar_conexion()
    
    def cargar_productos_desde_bd(self):
        try:
            conexion = ConectorBasedeDatos()
            if conexion.error:
                return [], f"Error de conexión a la base de datos: {conexion.error}"
            
            conexion.cursor.execute("SELECT id, nombre_producto, precio_producto, cantidad_producto, total FROM productos")
            productos = conexion.cursor.fetchall()
            
            return productos, "Productos cargados exitosamente."
        except Exception as e:
            return [], f"Ocurrió un error al cargar productos: {e}"
        finally:
            if 'conexion' in locals() and conexion:
                conexion.cerrar_conexion()