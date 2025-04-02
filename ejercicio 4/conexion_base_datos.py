import sqlite3

class ConectorBasedeDatos:
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("./ejercicio 4/productos.db")
            self.cursor = self.conexion.cursor()
            self.crear_tabla()
            self.error = False
        except Exception as e:
            self.error = self.retornar_error()
    
    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_producto TEXT NOT NULL,
                precio_producto INTEGER NOT NULL,
                cantidad_producto INTEGER NOT NULL,
                total INTEGER NOT NULL
            )
        ''')
        self.conexion.commit()
    
    def registrar_datos(self, nombre_producto, precio_producto, cantidad_producto, total):
        try:
            self.cursor.execute('''
                INSERT INTO productos (nombre_producto, precio_producto, cantidad_producto, total)
                VALUES (?, ?, ?, ?)
            ''', (nombre_producto, precio_producto, cantidad_producto, total))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al registrar datos: {e}")
    
    def retornar_error(self):
        import traceback
        return traceback.format_exc()
    
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
if __name__ == "__main__":
    conexion = ConectorBasedeDatos()

# Verificar si hubo un error durante la conexión
    if conexion.error:
        print("Ocurrió un error:", conexion.error)
    else:
        conexion.registrar_datos("Laptop", 1000, 5, 5000)
        conexion.registrar_datos("Mouse", 20, 10, 200)
        conexion.cerrar_conexion()