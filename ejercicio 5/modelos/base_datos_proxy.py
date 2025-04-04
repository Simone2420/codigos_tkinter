from .conector_base_datos import *
from .usuarios import Docente,Estudiante
from .libro import Libro
class BaseDatosProxy:
    def __init__(self):
        self._docentes = []
        self._estudiantes = []
        self._libros = []
        self._prestamos = []
        self.conexion = ConectorBasedeDatos()
        self.crear_docentes()
        self.crear_estudiantes()
        self.crear_libros()
    def crear_docentes(self):
        docentes = self.conexion.obtener_datos_docentes()
        for docente in docentes:
            id,nombre,identificacion,id_profesional,salario,horario,funciones,limite_libros_prestados,_=docente
            docente_objeto = Docente(nombre,identificacion,salario,horario,funciones,id_profesional,limite_prestamos=limite_libros_prestados,id=id)
            docente_objeto.establecer_tiene_multa(False)
            self._docentes.append(docente_objeto)
    def crear_estudiantes(self): 
        estudiantes = self.conexion.obtener_datos_estudiantes()
        for estudiante in estudiantes:
            id,nombre,identificacion,numero_matricula,numero_horas_sociales_asignadas,limite_libros_prestados,_=estudiante
            estudiante_objeto = Estudiante(nombre,identificacion,numero_matricula,limite_prestamos=limite_libros_prestados,id=id)
            estudiante_objeto.establecer_tiene_multa(False)
            estudiante_objeto.establecer_horas_sociales_asignadas(numero_horas_sociales_asignadas)
            self._estudiantes.append(estudiante_objeto)
    def crear_libros(self):
        libros = self.conexion.obtener_datos_libros()
        for libro in libros:
            id,titulo,autor,ano_publicacion,categoria,_,numero_veces_solicitado=libro
            libro_objeto = Libro(titulo,autor,ano_publicacion,categoria,id=id)
            libro_objeto.establecer_estado(True)
            libro_objeto.establecer_numero_veces_solicitado(numero_veces_solicitado)
            self._libros.append(libro_objeto)
    def crear_ultimo_docente_registrado(self):
        datos_ultimo_docente_registrado = self.conexion.obtener_ultimo_docente_registrado()
        if datos_ultimo_docente_registrado:
            id,nombre,identificacion,id_profesional,salario,horario,funciones,limite_libros_prestados,_ = datos_ultimo_docente_registrado
            docente_objeto = Docente(nombre,identificacion,salario,horario,funciones,id_profesional,limite_prestamos=limite_libros_prestados,id=id)
            docente_objeto.establecer_tiene_multa(False)
            self._docentes.append(docente_objeto)
    def crear_ultimo_estudiante_registrado(self):
        datos_ultimo_estudiante_registrado = self.conexion.obtener_ultimo_estudiante_registrado()
        if datos_ultimo_estudiante_registrado:
            id,nombre,identificacion,numero_matricula,numero_horas_sociales_asignadas,limite_libros_prestados,_ = datos_ultimo_estudiante_registrado
            estudiante_objeto = Estudiante(nombre,identificacion,numero_matricula,limite_prestamos=limite_libros_prestados,id=id)
            estudiante_objeto.establecer_tiene_multa(False)
            estudiante_objeto.establecer_horas_sociales_asignadas(numero_horas_sociales_asignadas)
            self._estudiantes.append(estudiante_objeto)
    def crear_ultimo_libro_registrado(self):
        datos_ultimo_libro_registrado = self.conexion.obtener_ultimo_libro_registrado()
        if datos_ultimo_libro_registrado:
            id,titulo,autor,ano_publicacion,categoria,_,numero_veces_solicitado = datos_ultimo_libro_registrado
            libro_objeto = Libro(titulo,autor,ano_publicacion,categoria,id=id)
            libro_objeto.establecer_estado(True)
            libro_objeto.establecer_numero_veces_solicitado(numero_veces_solicitado)
            self._libros.append(libro_objeto)
    def registrar_prestamo(self,prestamo):
        nombre_usuario = prestamo.obtener_usuario().obtener_nombre()
        identificacion_usuario = prestamo.obtener_usuario().obtener_identificacion()
        id_usuario = prestamo.obtener_usuario().obtener_id()
        titulo_libro = prestamo.obtener_libro().obtener_titulo()
        tipo_usuario = prestamo.obtener_usuario().obtener_tipo()
        titulo_libro = prestamo.obtener_libro().obtener_titulo()
        fecha_prestamo = prestamo.obtener_fecha_prestamo()
        fecha_devolucion = prestamo.obtener_fecha_devolucion_real()
        fecha_devolucion_esperada = prestamo.obtener_fecha_devolucion_esperada()
        fecha_devolucion_reagsignada = prestamo.obtener_fecha_reasignacion()
        valor_multa = prestamo.obtener_valor_multa()
        valor_a_pagar_multa = prestamo.obtener_valor_a_pagar_multa()
        tiene_multa = prestamo.obtener_tiene_multa()
        self.conexion.registrar_datos_prestamo(
            nombre_usuario,
            identificacion_usuario,
            id_usuario,
            tipo_usuario,
            titulo_libro,
            fecha_prestamo,
            fecha_devolucion_esperada,
            fecha_devolucion,
            fecha_devolucion_reagsignada,
            valor_multa,
            valor_a_pagar_multa,
            tiene_multa
            )
    def registrar_datos_docente(self,docente):
        self.conexion.registrar_datos_docente(
            docente.obtener_nombre(),
            docente.obtener_identificacion(),
            docente.obtener_id_profesional(),
            docente.obtener_salario(),
            docente.obtener_horario(),
            docente.obtener_funciones(), 
            docente.obtener_limite_prestamos() 
        )
        self.crear_ultimo_docente_registrado()
    def registrar_datos_estudiante(self,estudiante):
        self.conexion.registrar_datos_estudiante(
            estudiante.obtener_nombre(),
            estudiante.obtener_identificacion(),
            estudiante.obtener_numero_matricula(),
            estudiante.obtener_horas_sociales_asignadas(),
            estudiante.obtener_limite_prestamos()  
        )
        self.crear_ultimo_estudiante_registrado()
    def registrar_datos_libro(self,libro):
        self.conexion.registrar_datos_libro(
            libro.obtener_titulo(),
            libro.obtener_autor(),
            libro.obtener_ano_publicacion(),
            libro.obtener_categoria(),
            libro.obtener_esta_disponible(),
            libro.obtener_numero_veces_solicitado()  
        )
        self.crear_ultimo_libro_registrado()
    def actualizar_datos_prestamo(self,prestamo):
        id_prestamo = prestamo.obtener_id()
        nombre_usuario = prestamo.obtener_usuario().obtener_nombre()
        identificacion_usuario = prestamo.obtener_usuario().obtener_identificacion()
        id_usuario = prestamo.obtener_usuario().obtener_id()
        tipo_usuario = prestamo.obtener_usuario().obtener_tipo()
        titulo_libro = prestamo.obtener_libro().obtener_titulo()
        fecha_prestamo = prestamo.obtener_fecha_prestamo()
        fecha_devolucion_esperada = prestamo.obtener_fecha_devolucion_esperada()
        fecha_devolucion = prestamo.obtener_fecha_devolucion_real()
        fecha_devolucion_reagsignada = prestamo.obtener_fecha_reasignacion()
        valor_multa = prestamo.obtener_valor_multa()
        valor_a_pagar_multa = prestamo.obtener_valor_a_pagar_multa()
        tiene_multa = prestamo.obtener_tiene_multa()
        self.conexion.actualizar_datos_prestamo(
            id_prestamo,
            nombre_usuario,
            identificacion_usuario,
            id_usuario,
            tipo_usuario,
            titulo_libro,
            fecha_prestamo,
            fecha_devolucion_esperada,
            fecha_devolucion,
            fecha_devolucion_reagsignada,
            valor_multa,
            valor_a_pagar_multa,
            tiene_multa
        )
        def actualizar_datos_docente(self,docente):
            id_docente = docente.obtener_id()
            nombre = docente.obtener_nombre()
            identificacion = docente.obtener_identificacion()
            id_profesional = docente.obtener_id_profesional()
            salario = docente.obtener_salario()
            horario = docente.obtener_horario()
            funciones = docente.obtener_funciones()
            limite_prestamos = docente.obtener_limite_prestamos()
            tiene_multa = docente.obtener_tiene_multa()
            self.conexion.actualizar_datos_docente(
                id_docente,
                nombre,
                identificacion,
                id_profesional,
                salario,
                horario,
                funciones,
                limite_prestamos,
                tiene_multa
            )
        def actualizar_datos_estudiante(self,estudiante):
            id_estudiante = estudiante.obtener_id()
            nombre = estudiante.obtener_nombre()
            identificacion = estudiante.obtener_identificacion()
            numero_matricula = estudiante.obtener_numero_matricula()
            numero_horas_sociales_asignadas = estudiante.obtener_horas_sociales_asignadas()
            limite_prestamos = estudiante.obtener_limite_prestamos()
            tiene_multa = estudiante.obtener_tiene_multa()
            self.conexion.actualizar_datos_estudiante(
                id_estudiante,
                nombre,
                identificacion,
                numero_matricula,
                numero_horas_sociales_asignadas,
                limite_prestamos,
                tiene_multa 
            )
        def actualizar_datos_libro(self,libro):
            id_libro = libro.obtener_id()
            titulo = libro.obtener_titulo()
            autor = libro.obtener_autor()
            ano_publicacion = libro.obtener_ano_publicacion()
            categoria = libro.obtener_categoria()
            estado = libro.obtener_esta_disponible()
            numero_veces_solicitado = libro.obtener_numero_veces_solicitado()
            self.conexion.actualizar_datos_libro(
                id_libro,
                titulo,
                autor,
                ano_publicacion,
                categoria,
                estado,
                numero_veces_solicitado
            )
    def obtener_docentes(self):
        return self._docentes
    def obtener_estudiantes(self):
        return self._estudiantes
    def obtener_libros(self):
        return self._libros
if __name__ == "__main__":
    # from datetime import datetime, timedelta
    # from prestamo import Prestamo  # Make sure to import the Prestamo class
    
    # # Initialize the proxy
    # base_datos = BaseDatosProxy()
    
    # # Test 1: Create and update a teacher
    # print("\n=== Test 1: Teacher Operations ===")
    # docente = Docente("María López", 54321, 4500, "9:00 AM - 5:00 PM", 
    #                   "Mathematics Professor", "P12345", limite_prestamos=3)
    # base_datos.conexion.registrar_datos_docente(
    #     docente.obtener_nombre(),
    #     docente.obtener_identificacion(),
    #     docente.obtener_id_profesional(),
    #     docente.obtener_salario(),
    #     docente.obtener_horario(),
    #     docente.obtener_funciones(),
    #     docente.obtener_limite_prestamos()
    # )
    
    # # Test 2: Create and update a student
    # print("\n=== Test 2: Student Operations ===")
    # estudiante = Estudiante("Carlos Pérez", 98765, "M12345", limite_prestamos=2)
    # estudiante.establecer_horas_sociales_asignadas(15)
    # base_datos.conexion.registrar_datos_estudiante(
    #     estudiante.obtener_nombre(),
    #     estudiante.obtener_identificacion(),
    #     estudiante.obtener_numero_matricula(),
    #     estudiante.obtener_horas_sociales_asignadas(),
    #     estudiante.obtener_limite_prestamos()
    # )
    
    # # Test 3: Create a book
    # print("\n=== Test 3: Book Operations ===")
    # libro = Libro("Python Programming", "Jane Smith", 2023, "Technology")
    # base_datos.conexion.registrar_datos_libro(
    #     libro.obtener_titulo(),
    #     libro.obtener_autor(),
    #     libro.obtener_ano_publicacion(),
    #     libro.obtener_categoria(),
    #     True,  # disponible
    #     0      # numero_veces_solicitado
    # )
    
    # # Test 4: Create a loan
    # print("\n=== Test 4: Loan Creation ===")
    # fecha_actual = datetime.now()
    # fecha_devolucion = fecha_actual + timedelta(days=15)
    
    # prestamo = Prestamo(estudiante, libro)
    # prestamo.establecer_fecha_prestamo(fecha_actual.strftime("%Y-%m-%d"))
    # prestamo.establecer_fecha_devolucion_esperada(fecha_devolucion.strftime("%Y-%m-%d"))
    
    # base_datos.registrar_prestamo(prestamo)
    
    # # Test 5: Update loan (simulating a return)
    # print("\n=== Test 5: Loan Update ===")
    # fecha_devolucion_real = fecha_actual + timedelta(days=16)  # One day late
    # prestamo.establecer_fecha_devolucion(fecha_devolucion_real.strftime("%Y-%m-%d"))
    # prestamo.establecer_valor_multa(5000)  # Example fine for late return
    # prestamo.establecer_tiene_multa(True)
    
    # base_datos.actualizar_datos_prestamo(prestamo)
    
    # # Print final results
    # print("\n=== Final Database State ===")
    # print("\nDocentes:")
    # docentes = base_datos.conexion.obtener_datos_docentes()
    # for doc in docentes:
    #     print(doc)
    
    # print("\nEstudiantes:")
    # estudiantes = base_datos.conexion.obtener_datos_estudiantes()
    # for est in estudiantes:
    #     print(est)
    
    # print("\nLibros:")
    # libros = base_datos.conexion.obtener_datos_libros()
    # for lib in libros:
    #     print(lib)
    
    # print("\nPréstamos:")
    # prestamos = base_datos.conexion.obtener_datos_prestamos()
    # for pres in prestamos:
    #     print(pres)
    
    # # Close connection
    # base_datos.conexion.cerrar_conexion()
    base_datos = BaseDatosProxy()
    print(base_datos.obtener_estudiantes())
    print(base_datos.obtener_docentes())
    print(base_datos.obtener_libros())