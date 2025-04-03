from .usuarios import Estudiante,Docente
from .libro import Libro
from .conector_base_datos import *
import random
nombres_docentes = ["Carlos Inti","Blass Muñoz","Omar Bravo","Juan Hediberto","Brian Aldana"]
nombres_estudiantes = ["Diego Ortiz","Hediberto de las Nieves", "Alberto Fonseca","Carlitos Nuñez","Andres Aya"]
identificaciones = [random.randint(10000000,99999999) for _ in range(10)]
id_profesionales = [f"P{random.randint(10000, 99999)}" for _ in range(5)]
numeros_matriculas = [f"M{random.randint(10000,99999)}" for _ in range(5)]
horarios = ["Diurno","Nocturno","Mixto"]
titulos_libros = [
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "La sombra del viento",
    "El amor en los tiempos del cólera",
    "Rayuela",
    "Crónica de una muerte anunciada",
    "El principito",
    "1984",
    "Ficciones",
    "La casa de los espíritus",
    "Los detectives salvajes",
    "El laberinto de la soledad",
    "Pedro Páramo",
    "El túnel",
    "La ciudad y los perros",
    "El aleph",
    "El nombre del viento",
    "El retrato de Dorian Gray",
    "Orgullo y prejuicio",
    "Crimen y castigo"
]
nombre_autores = [
    "Gabriel García Márquez",
    "Miguel de Cervantes",
    "Jorge Luis Borges",
    "Isabel Allende",
    "Mario Vargas Llosa"
]
categorias = ["Literatura","Novela","Realismo","Ciencia Ficción"]
anos_publicaciones = [random.randint(1800,2025) for _ in range(20)]
class BaseDatosEstudiantes:
    estudiantes = []
    def __init__(self):
        self._estudiantes = []
        self.agregar_estudiantes(nombres_estudiantes,identificaciones,numeros_matriculas)
    def agregar_estudiantes(self,nombres_estudiantes,identificaciones,numeros_matriculas,numero_estudiantes=5):
        nombres_estudiante_copia = nombres_estudiantes
        identificaciones_aux = identificaciones[5:]
        numeros_matriculas_copia = numeros_matriculas[:]
        for _ in range(numero_estudiantes):
            nombre_estudiante = nombres_estudiante_copia.pop(0)
            identificacion_estudiante = identificaciones_aux.pop(0)
            numero_matricula_estudiante = numeros_matriculas_copia.pop(0)
            self._estudiantes.append(Estudiante(nombre_estudiante, identificacion_estudiante,numero_matricula_estudiante))
    def registrar_estudiante(self,estudiante):
        self._estudiantes.append(estudiante)
    def obtener_estudiantes(self):
        return self._estudiantes
class BaseDatosDocentes:
    docentes = []
    def __init__(self):
        self._docentes = []
        self.agregar_docentes(nombres_docentes,identificaciones,id_profesionales,horarios)
    def agregar_docentes(self,nombres_docentes,identificaciones,id_profesionales,horarios,numero_docentes = 5):
        nombres_docentes_copia = nombres_docentes[:]
        identificaciones_aux = identificaciones[0:5]
        id_profesionales_copia = id_profesionales[:]
        for _ in range(numero_docentes):
            nombre_docente = nombres_docentes_copia.pop(0)
            identificacion_docente = identificaciones_aux.pop(0)
            horario_docente = random.choice(horarios)
            id_profesional_docente = id_profesionales_copia.pop(0)
            self._docentes.append(Docente(nombre_docente,identificacion_docente,1000000,horario_docente,"Enseñar",id_profesional_docente))
    def registrar_docente(self,docente):
        self._docentes.append(docente)
    def obtener_docentes(self):
        return self._docentes
class BaseDatosLibros:
    libros = []
    def __init__(self):
        self._libros = []
        self.agregar_libros(titulos_libros,nombre_autores,anos_publicaciones,categorias)
    def agregar_libros(self,titulos_libros,nombre_autores,anos_publicaciones,categorias,numero_libros=20):
        titulos_libros_copia = titulos_libros[:]
        for _ in range(numero_libros):
            titulo_libro = titulos_libros_copia.pop(0)
            nombre_autor = random.choice(nombre_autores)
            ano_publicacion = random.choice(anos_publicaciones)
            categoria = random.choice(categorias)
            self._libros.append(Libro(titulo_libro,nombre_autor,ano_publicacion,categoria))
    def registrar_libro(self,libro):
        self._libros.append(libro)
    def obtener_libros(self):
        return self._libros
if __name__ == "__main__":
    estudiantes = BaseDatosEstudiantes().obtener_estudiantes()
    docentes = BaseDatosDocentes().obtener_docentes()
    libros = BaseDatosLibros().obtener_libros()
    conexion = ConectorBasedeDatos()
    for estudiante in estudiantes:
        conexion.registrar_datos_estudiante(
            estudiante.obtener_nombre(),
            estudiante.obtener_identificacion(),
            estudiante.obtener_numero_matricula(),
            estudiante.obtener_horas_sociales_asignadas(),
            estudiante.obtener_limite_prestamos())
    for libro in libros:
        conexion.registrar_datos_libro(
            libro.obtener_titulo(),
            libro.obtener_autor(),
            libro.obtener_ano_publicacion(),
            libro.obtener_categoria(),
            libro.obtener_esta_disponible(),
            libro.obtener_numero_veces_solicitado()
        )
    for docente in docentes:
        conexion.registrar_datos_docente(
            docente.obtener_nombre(),
            docente.obtener_identificacion(),
            docente.obtener_id_profesional(),
            docente.obtener_salario(),
            docente.obtener_horario(),
            docente.obtener_funciones(),
            docente.obtener_limite_prestamos()
        )