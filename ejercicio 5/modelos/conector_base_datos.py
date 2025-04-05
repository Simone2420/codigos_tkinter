import sqlite3

class ConectorBasedeDatos:
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("./ejercicio 5/modelos/biblioteca.db")
            self.cursor = self.conexion.cursor()
            self.crear_tabla_docentes()
            self.crear_tabla_estudiantes()
            self.crear_tabla_libros()
            self.crear_tabla_prestamos()
            self.error = False
        except Exception as e:
            self.error = self.retornar_error()
    # a
    def crear_tabla_docentes(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS docentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_docente TEXT NOT NULL,
                identificacion INTEGER,
                id_profesional TEXT NOT NULL,
                salario INTEGER NOT NULL,
                horario TEXT NOT NULL,
                funciones TEXT NOT NULL,
                limite_prestamos INTEGER DEFAULT 3,
                tiene_multa INTEGER DEFAULT 0
            )
        ''')
        self.conexion.commit()
    def crear_tabla_estudiantes(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                identificacion INTEGER NOT NULL,
                numero_matricula TEXT NOT NULL,
                horas_sociales_asignadas INTEGER DEFAULT 0,
                limite_prestamos INTEGER DEFAULT 2,
                tiene_multa INTEGER DEFAULT 0
            )
        ''')
        self.conexion.commit()

    def crear_tabla_libros(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacion INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                disponible INTEGER DEFAULT 1,
                numero_veces_solicitado INTEGER DEFAULT 0
            )
        ''')
        self.conexion.commit()
    def crear_tabla_prestamos(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario TEXT NOT NULL,
                identificacion_usuario INTEGER NOT NULL,
                id_usuario TEXT NOT NULL,
                tipo_usuario TEXT NOT NULL,
                titulo_libro TEXT NOT NULL,
                fecha_prestamo DATE NOT NULL,
                fecha_devolucion_esperada DATE NOT NULL,
                fecha_devolucion_real DATE,
                fecha_reasignacion DATE,
                valor_multa REAL DEFAULT 0,
                valor_a_pagar_multa REAL DEFAULT 0,
                tiene_multa INTEGER DEFAULT 0
            )
        ''')
        self.conexion.commit()
    def registrar_datos_estudiante(self, nombre, identificacion, numero_matricula, horas_sociales_asignadas, limite_prestamos):
        try:
            self.cursor.execute('''
                INSERT INTO estudiantes (nombre, identificacion, numero_matricula, horas_sociales_asignadas, limite_prestamos)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, identificacion, numero_matricula, horas_sociales_asignadas, limite_prestamos))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al registrar datos: {e}")

    def registrar_datos_libro(self, titulo, autor, ano_publicacion, categoria, disponible, numero_veces_solicitado):
        try:
            self.cursor.execute('''
                INSERT INTO libros (titulo, autor, ano_publicacion, categoria, disponible, numero_veces_solicitado)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (titulo, autor, ano_publicacion, categoria, disponible, numero_veces_solicitado))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al registrar datos: {e}")

    def registrar_datos_prestamo(self, nombre_usuario, identificacion_usuario, id_usuario, tipo_usuario, titulo_libro, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real, fecha_reasignacion, valor_multa, valor_a_pagar_multa, tiene_multa):
        try:
            self.cursor.execute('''
                INSERT INTO prestamos (nombre_usuario, identificacion_usuario, id_usuario, tipo_usuario, titulo_libro, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real, fecha_reasignacion, valor_multa, valor_a_pagar_multa, tiene_multa)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre_usuario, identificacion_usuario, id_usuario, tipo_usuario, titulo_libro, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real, fecha_reasignacion, valor_multa, valor_a_pagar_multa, tiene_multa))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al registrar datos de préstamo: {e}")

    def registrar_datos_docente(self, nombre_docente, identificacion, id_profesional, salario,horario, funciones, limite_prestamos):
        try:
            self.cursor.execute('''
                INSERT INTO docentes (nombre_docente, identificacion, id_profesional, salario,horario, funciones, limite_prestamos)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (nombre_docente, identificacion, id_profesional, salario,horario, funciones, limite_prestamos))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al registrar datos: {e}")
    def obtener_datos_docentes(self):
        try:
            self.cursor.execute("SELECT * FROM docentes")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")

    def obtener_datos_estudiantes(self):
        try:
            self.cursor.execute("SELECT * FROM estudiantes")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")

    def obtener_datos_libros(self):
        try:
            self.cursor.execute("SELECT * FROM libros")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")

    def obtener_datos_prestamos(self):
        try:
            self.cursor.execute("SELECT * FROM prestamos")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener datos: {e}")

    def actualizar_datos_docente(self, id_docente, nombre_docente, identificacion, id_profesional, salario, horario, funciones, limite_prestamos,tiene_multa):
        try:
            self.cursor.execute('''
                UPDATE docentes SET nombre_docente=?, identificacion=?, id_profesional=?, salario=?, horario=?, funciones=?, limite_prestamos=?,tiene_multa=? WHERE id=?
            ''', (nombre_docente, identificacion, id_profesional, salario, horario, funciones, limite_prestamos, tiene_multa,id_docente))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar datos: {e}")

    def actualizar_datos_estudiante(self, id_estudiante, nombre, identificacion, numero_matricula, horas_sociales_asignadas, limite_prestamos,tiene_multa):
        try:
            self.cursor.execute('''
                UPDATE estudiantes SET nombre=?, identificacion=?, numero_matricula=?, horas_sociales_asignadas=?, limite_prestamos=?,tiene_multa=? WHERE id=?
            ''', (nombre, identificacion, numero_matricula, horas_sociales_asignadas, limite_prestamos, id_estudiante))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar datos: {e}")

    def actualizar_datos_libro(self, id_libro, titulo, autor, ano_publicacion, categoria, disponible, numero_veces_solicitado):
        try:
            self.cursor.execute('''
                UPDATE libros SET titulo=?, autor=?, ano_publicacion=?, categoria=?, disponible=?, numero_veces_solicitado=? WHERE id=?
            ''', (titulo, autor, ano_publicacion, categoria, disponible, numero_veces_solicitado, id_libro))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar datos: {e}")

    def actualizar_datos_prestamo(self, id_prestamo, nombre_usuario, identificacion_usuario, id_usuario, tipo_usuario, titulo_libro, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real, fecha_reasignacion, valor_multa, valor_a_pagar_multa, tiene_multa):
        try:
            self.cursor.execute('''
                UPDATE prestamos SET nombre_usuario=?, identificacion_usuario=?, id_usuario=?, tipo_usuario=?, titulo_libro=?, fecha_prestamo=?, fecha_devolucion_esperada=?, fecha_devolucion_real=?, fecha_reasignacion=?, valor_multa=?, valor_a_pagar_multa=?, tiene_multa=? WHERE id=?
            ''', (nombre_usuario, identificacion_usuario, id_usuario, tipo_usuario, titulo_libro, fecha_prestamo, fecha_devolucion_esperada, fecha_devolucion_real, fecha_reasignacion, valor_multa, valor_a_pagar_multa, tiene_multa, id_prestamo))
            self.conexion.commit()
        except Exception as e:
            print(f"Error al actualizar datos: {e}")
    def obtener_ultimo_docente_registrado(self):
        self.cursor.execute("SELECT * FROM docentes ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
    def obtener_ultimo_estudiante_registrado(self):
        self.cursor.execute("SELECT * FROM estudiantes ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
    def obtener_ultimo_libro_registrado(self):
        self.cursor.execute("SELECT * FROM libros ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
    def obtener_ultimo_prestamo_registrado(self):
        self.cursor.execute("SELECT * FROM prestamos ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
    def retornar_error(self):
        import traceback
        return traceback.format_exc()
    
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
if __name__ == "__main__":
    conexion = ConectorBasedeDatos()
    if conexion.error:
        print("Ocurrió un error:", conexion.error)
    else:
        conexion.registrar_datos_docente("Fabricio", 1000, "P12345", 5000, "8:00 AM - 5:00 PM", "Teaching and research", 5)
        conexion.registrar_datos_docente("Maurico", 20, "P67890", 200, "9:00 AM - 6:00 PM", "Assisting students", 3)
        conexion.registrar_datos_estudiante("Juan", 123456, "M12345", 10, 2)
        conexion.registrar_datos_libro("Python for Dummies", "John Doe", 2022, "Programming", 1, 0)
        conexion.registrar_datos_prestamo("Juan", 123456, "M12345", "Estudiante", "Python for Dummies", "2022-05-01", "2022-05-15", None, None, 0, 0, 0)
        conexion = ConectorBasedeDatos()


        docentes = conexion.obtener_datos_docentes()
        estudiantes = conexion.obtener_datos_estudiantes()
        libros = conexion.obtener_datos_libros()
        prestamos = conexion.obtener_datos_prestamos()

        print("Docentes:")
        for docente in docentes:
            print(docente)

        print("Estudiantes:")
        for estudiante in estudiantes:
            print(estudiante)

        print("Libros:")
        for libro in libros:
            print(libro)

        print("Préstamos:")
        for prestamo in prestamos:
            print(prestamo)

        conexion.cerrar_conexion()