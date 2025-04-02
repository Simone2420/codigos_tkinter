from abc import ABC, abstractmethod
from .persona import Persona

class UsuarioBase(Persona, ABC):
    tipo = ""
    libros_prestados = []
    limite_prestamos = 0
    tiene_multa = False
    def __init__(self, nombre, identificacion, tipo="Usuario"):
        Persona.__init__(self,nombre, identificacion)
        self._tipo = tipo
        self._libros_prestados = []
        self._limite_prestamos = 0
        self._tiene_multa = False
    def obtener_tiene_multa(self):
        return self._tiene_multa
    def establecer_tiene_multa(self,nuevo_estado):
        if nuevo_estado in (True, False):
            self._tiene_multa = nuevo_estado
        else:
            print("Solo se admite True o False")
    def establecer_limite_prestamos(self,nuevo_limite):
        try:
            if nuevo_limite >= 0:
                self._limite_prestamos = nuevo_limite
            else:
                raise Exception("Entrada invalida debe ser numerica y mayor a 0")
        except Exception as e:
            print(f"Error: {e}")
            return False
    def obtener_tipo(self):
        return self._tipo

    def obtener_libros_prestados(self):
        return self._libros_prestados
    def agregar_libro(self,libro):
        self._libros_prestados.append(libro)
    def quitar_libro(self, libro):
        try:
            indice = self._libros_prestados.index(libro)
            libro_eliminado = self._libros_prestados.pop(indice)
            return libro_eliminado
        except ValueError:
            print("El libro no está en la lista de libros prestados.")
            return None
    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def validar_datos(self):
        pass


class Estudiante(UsuarioBase):
    numero_matricula = "M#####"
    horas_sociales_asignadas = 0
    def __init__(self, nombre, identificacion, numero_matricula, limite_prestamos=2):
        super().__init__(nombre, identificacion, "estudiante")
        self.__numero_matricula = numero_matricula
        self._horas_sociales_asignadas = 0
        self._limite_prestamos = limite_prestamos

    def obtener_numero_matricula(self):
        return self.__numero_matricula
    def obtener_limite_prestamos(self):
        return self._limite_prestamos
    def obtener_horas_sociales_asignadas(self):
        return self._horas_sociales_asignadas
    def establecer_horas_sociales_asignadas(self,nuevas_horas_sociales_asignadas):
        self._horas_sociales_asignadas = nuevas_horas_sociales_asignadas
    def agregar_horas_sociales_asignadas(self,nuevas_horas_sociales_asignadas):
        self._horas_sociales_asignadas += nuevas_horas_sociales_asignadas
    def mostrar_informacion(self):
        print(f"Nombre: {self.obtener_nombre()}")
        print(f"Identificacion: {self.obtener_identificacion()}")
        print(f"Numero Matricula: {self.obtener_numero_matricula()}")
        print(f"Horas sociales asignada {self.obtener_horas_sociales_asignadas()}")
        print(f"Limite libros prestados: {self.obtener_limite_prestamos()}")
        print(f"Libros prestados: {self.obtener_libros_prestados()} \n")

    def validar_datos(self):
        try:
            # Validar nombre
            if not isinstance(self.obtener_nombre(), str) or not self.obtener_nombre().strip():
                raise ValueError("El nombre debe ser una cadena no vacía.")

            # Validar identificación
            if not isinstance(self.obtener_identificacion(), int) or self.obtener_identificacion() <= 0:
                raise ValueError("La identificación debe ser un número positivo.")

            # Validar número de matrícula
            if not isinstance(self.__numero_matricula, str) or not self.__numero_matricula.strip() or not self.__numero_matricula.startswith("M"):
                raise ValueError("El número de matrícula debe ser una cadena no vacía que comience con 'M'.")

            # Validar límite de préstamos
            if not isinstance(self._limite_prestamos, int) or self._limite_prestamos <= 0:
                raise ValueError("El límite de préstamos debe ser un número positivo.")

            return True
        except ValueError as e:
            return False

class EmpleadoBiblioteca(Persona):
    salario = 0
    salario_constante = 0
    horario = ""
    funciones = ""
    def __init__(self, nombre, id_profesional, identificacion, salario, horario, funciones):
        super().__init__(nombre, identificacion)
        self.__salario = salario
        self.__id_profesional = id_profesional
        self.__salario_constante = self.__salario
        self.__horario = horario
        self.__funciones = funciones

    def obtener_salario(self):
        return self.__salario
    def obtener_salario_constante(self):
        return self.__salario_constante
    def establecer_salario(self,nuevo_salario):
        self.__salario = nuevo_salario
    def obtener_horario(self):
        return self.__horario
    def obtener_id_profesional(self):
        return self.__id_profesional
    def obtener_funciones(self):
        return self.__funciones

class Docente(UsuarioBase, EmpleadoBiblioteca):
    id_profesional = "P#####"
    def __init__(self, nombre, identificacion, salario, horario, funciones, id_profesional,limite_prestamos=3):
        EmpleadoBiblioteca.__init__(self,nombre, id_profesional,identificacion, salario, horario, funciones)
        UsuarioBase.__init__(self,nombre, identificacion, "docente")
        self.__id_profesional = id_profesional
        self._limite_prestamos = limite_prestamos

    def obtener_id_profesional(self):
        return self.__id_profesional
    def obtener_limite_prestamos(self):
        return self._limite_prestamos
    def mostrar_informacion(self):
        print(f"Tipo {self.obtener_tipo()}")
        print(f"Nombre: {self.obtener_nombre()}")
        print(f"Identificacion: {self.obtener_identificacion()}")
        print(f"Id profesional: {self.obtener_id_profesional()}")
        print(f"Horario: {self.obtener_horario()}")
        print(f"Salario: {self.obtener_salario()}")
        print(f"Funciones: {self.obtener_funciones()}")
        print(f"Limite prestamos: {self.obtener_limite_prestamos()}")
        print(f"Libros prestados: {self.obtener_libros_prestados()} \n")
    def validar_datos(self):
        try:
            # Validar nombre
            if not isinstance(self.obtener_nombre(), str) or not self.obtener_nombre().strip():
                raise ValueError("El nombre debe ser una cadena no vacía.")

            # Validar identificación
            if not isinstance(self.obtener_identificacion(), int) or self.obtener_identificacion() <= 0:
                raise ValueError("La identificación debe ser un número positivo.")

            # Validar ID profesional
            if not isinstance(self.__id_profesional, str) or not self.__id_profesional.strip() or not self.__id_profesional.startswith("P"):
                raise ValueError("El ID profesional debe ser una cadena no vacía que comience con 'P'.")

            # Validar salario
            if not isinstance(self.obtener_salario(), (int, float)) or self.obtener_salario() <= 0:
                raise ValueError("El salario debe ser un número positivo.")

            # Validar horario
            if not isinstance(self.obtener_horario(), str) or not self.obtener_horario().strip():
                raise ValueError("El horario debe ser una cadena no vacía.")

            # Validar funciones
            if not isinstance(self.obtener_funciones(), str) or not self.obtener_funciones().strip():
                raise ValueError("Las funciones deben ser una cadena no vacía.")

            return True
        except ValueError as e:
            return False
