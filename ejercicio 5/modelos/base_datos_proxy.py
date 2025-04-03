from conector_base_datos import *
from usuarios import Docente,Estudiante
from libro import Libro
class BaseDatosProxy:
    def __init__(self):
        self.docentes = []
        self.estudiantes = []
        self.libros = []
        self.prestamos = []
        self.conexion = ConectorBasedeDatos()
        self.crear_docentes()
        self.crear_estudiantes()
    def crear_docentes(self):
        docentes = self.conexion.obtener_datos_docentes()
        for docente in docentes:
            id,nombre,identificacion,id_profesional,salario,horario,funciones,limite_libros_prestados,_=docente
            docente_objeto = Docente(nombre,identificacion,salario,horario,funciones,id_profesional,limite_prestamos=limite_libros_prestados,id=id)
            docente_objeto.establecer_tiene_multa(False)
            self.docentes.append(docente_objeto)
    def crear_estudiantes(self): 
        estudiantes = self.conexion.obtener_datos_estudiantes()
        for estudiante in estudiantes:
            id,nombre,identificacion,numero_matricula,numero_horas_sociales_asignadas,limite_libros_prestados,_=estudiante
            estudiante_objeto = Estudiante(nombre,identificacion,numero_matricula,limite_prestamos=limite_libros_prestados,id=id)
            estudiante_objeto.establecer_tiene_multa(False)
            estudiante_objeto.establecer_horas_sociales_asignadas(numero_horas_sociales_asignadas)
            self.estudiantes.append(estudiante_objeto)
        print(self.estudiantes)
    def crear_libros(self):
        libros = self.conexion.obtener_datos_libros()
        for libro in libros:
            id,titulo,autor,ano_publicacion,categoria,_,numero_veces_solicitado=libro
            libro_objeto = Libro(titulo,autor,ano_publicacion,categoria,id=id)
            libro_objeto.establecer_estado(True)
            libro_objeto.establecer_numero_veces_solicitado(numero_veces_solicitado)
            self.libros.append(libro_objeto)
            libro_objeto.mostrar_informacion()
    def registrar_prestamos(self): pass #lista con objetos tipo prestamo 

base_datos = BaseDatosProxy()
base_datos.crear_libros()