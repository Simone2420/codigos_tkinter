from modelos import *
from controladores import *
class BibliotecaFacade:
    def __init__(self):
        self.__base_datos_proxy = BaseDatosProxy()
        self._gestor_usuarios = GestorUsuarios(self.__base_datos_proxy)
        self._gestor_prestamos = GestorPrestamos(self.__base_datos_proxy)
        self._gestor_libros = GestorLibros(self.__base_datos_proxy)
    def logear_usuario(self,tipo_usuario,
    nombre_usuario,id_matricula_usuario,identificacion_usuario):
        empleado = EmpleadoBiblioteca("Blass",
        "P23456",1070300400,100000,"Mañana","Gestionar")
        validar_id_profesional = self.verificar_id_matricula_usuario(
            id_matricula_usuario,tipo_usuario)
        if tipo_usuario == "empleado biblioteca" and validar_id_profesional == True:
            validador = all(
                [nombre_usuario == empleado.obtener_nombre(),
                id_matricula_usuario == empleado.obtener_id_profesional(),
                identificacion_usuario == empleado.obtener_identificacion()]
                )
            if validar_id_profesional != True:
                return "Error en el id_profesional"
            else:
                if validador == True:
                    return empleado
                else:
                    return "Bibliotecario no encontrado"
        elif tipo_usuario == "docente":
            docente = self._gestor_usuarios.ingresar_docente(nombre_usuario,
            identificacion_usuario,id_matricula_usuario)
            if docente == False:
                return "Docente no encontrado"
            elif validar_id_profesional!= True:
                return "Error en el id_profesional"
            else:
                return docente
        elif tipo_usuario == "estudiante":
            estudiante = self._gestor_usuarios.ingresar_estudiante(nombre_usuario,
            identificacion_usuario,id_matricula_usuario)
            if estudiante == False:
                return "Estudiante no encontrado"
            elif validar_id_profesional!= True:
                return "Error en el número de matrícula"
            else:
                return estudiante
        else:
            return "Tipo de usuario invalido"
    def verificar_id_matricula_usuario(self,id_matricula_usuario,tipo_usuario):
        try:
            if tipo_usuario == "empleado biblioteca" or tipo_usuario == "docente":
                if len(id_matricula_usuario) != 6:  # Verificar longitud
                    raise DatosInvalidos(
                        "El ID profesional debe tener exactamente 6 caracteres.")
                if id_matricula_usuario[0].upper() != 'P':  # Verificar prefijo
                    raise DatosInvalidos(
                        "El ID profesional debe comenzar con la letra 'P'.")
                if not id_matricula_usuario[1:].isdigit():  # Verificar dígitos
                    raise DatosInvalidos(
                        "Los últimos 5 caracteres deben ser dígitos numéricos.")
                return True
            elif tipo_usuario == "estudiante":
                if len(id_matricula_usuario) != 6:  # Verificar longitud
                    raise DatosInvalidos(
                        "El ID profesional debe tener exactamente 6 caracteres.")
                if id_matricula_usuario[0].upper() != 'M':  # Verificar prefijo
                    raise DatosInvalidos(
                        "El el Número de matrícula debe comenzar con la letra 'M'.")
                if not id_matricula_usuario[1:].isdigit():  # Verificar dígitos
                    raise DatosInvalidos(
                        "Los últimos 5 caracteres deben ser dígitos numéricos.")
                return True
        except DatosInvalidos as e:
            return e
    def obtener_informacion_usuario(self,usuario):
        if isinstance(usuario,Docente):
            return usuario.obtener_informacion()
        elif isinstance(usuario,Estudiante):
            return usuario.obtener_informacion()
        elif isinstance(usuario,EmpleadoBiblioteca):
            return usuario.obtener_informacion()
    def obtener_docentes(self):
        return self._gestor_usuarios.obtener_docentes()
    def obtener_estudiantes(self):
        return self._gestor_usuarios.obtener_estudiantes()
    def obtener_libros(self):
        return self._gestor_libros.obtener_libros()
    def obtener_prestamos_activos(self):
        return self._gestor_prestamos.listar_prestamos_activos_detallado()
    def obtener_prestamos_historico(self):
        return self._gestor_prestamos.listar_historico_prestamos_detallado()
    def registrar_docente(self,nombre,
    identificacion,
    id_matricula,
    horario,
    salario=1000000,
    funciones="enseñar"): 
        verificador = self.verificar_id_matricula_usuario(
            id_matricula,
        "docente") 
        if verificador!= True:
            return verificador
        else:
            docente_temporal = Docente(nombre,
            identificacion,salario,horario,funciones,id_matricula)
            self._gestor_usuarios.registrar_usuario_nuevo(docente_temporal)
    def registrar_estudiante(self,nombre,identificacion,id_matricula):
        verificador = self.verificar_id_matricula_usuario(
            id_matricula,
        "estudiante") 
        if verificador!= True:
            return verificador
        else:
            estudiante_temporal = Estudiante(nombre,
            identificacion,id_matricula)
            self._gestor_usuarios.registrar_usuario_nuevo(estudiante_temporal)
    def registrar_libro(self,titulo_libro,
    nombre_autor,ano_publicacion,categoria):
        libro_temporal = Libro(titulo_libro,
        nombre_autor,ano_publicacion,categoria)
        self._gestor_libros.registrar_libro(libro_temporal)
    def hacer_prestamo_libro(self,usuario,libro): pass
    def extender_prestamo_libro(self,usuario): pass
    def devolver_prestamo_libro(self,usuario): pass
    def cobrar_multa_usuario(self,usuario): pass
    def mostrar_libros(self,categoria): pass
    def mostrar_libros_mas_solicitados(self): pass
    def mostrar_prestamos_activos(self): pass
    def mostrar_historico_prestamo(self): pass
    
    #def eliminar_usuario_usuario(self): pass
    #def editar_usuario_usuario(self): pass