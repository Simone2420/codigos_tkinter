from pickle import FALSE
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
    def obtener_libros_disponibles(self):
        return self._gestor_libros.mostrar_libros_disponibles()
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
    def hacer_prestamo_libro(self,usuario,libro):
        prestamo_temporal = Prestamo(usuario,libro)
        prestamo_temporal.prestar_libro()
        usuario_prestamo = prestamo_temporal.obtener_usuario()
        libro_prestamo = prestamo_temporal.obtener_libro()
        usuario = usuario_prestamo
        libro = libro_prestamo
        if usuario.obtener_tipo() == "estudiante":
            self.actualizar_datos_estudiante(usuario)
        elif usuario.obtener_tipo() == "docente":
            self.actualizar_datos_docente(usuario)
        self._gestor_libros.actualizar_datos_libro(libro)
        self._gestor_prestamos.agregar_prestamo(prestamo_temporal)
    def buscar_libro_por_titulo(self,titulo_libro):
        libros = self._gestor_libros.obtener_libros()
        for libro in libros:
            if libro.obtener_titulo() == titulo_libro:
                return libro
    def buscar_libro_por_id(self,id_libro):
        libros = self._gestor_libros.obtener_libros()
        for libro in libros:
            if libro.obtener_id() == id_libro:
                return libro
    def obtener_prestamos_activos_usuario(self,usuario):
        return self._gestor_prestamos.filtrar_prestamos_por_usuario(usuario)
    def actualizar_datos_docente(self,docente):
        self._gestor_usuarios.actualizar_docente(docente)
    def actualizar_datos_estudiante(self,estudiante):
        self._gestor_usuarios.actualizar_estudiante(estudiante)
    def actualizar_datos_libro(self,libro):
        self._gestor_libros.actualizar_datos_libro(libro)
    def actualizar_datos_prestamo(self,prestamo):
        self._gestor_prestamos.actualizar_prestamo(prestamo)
    def buscar_prestamo_por_nombre_libro(self,nombre_libro):
        prestamos = self._gestor_prestamos.obtener_prestamos()
        for prestamo in prestamos:
            if prestamo.obtener_libro().obtener_titulo() == nombre_libro:
                return prestamo
    def extender_prestamo_libro(self,prestamo,dias_transcurridos,usuario_interfaz):
        prestamo.establecer_usuario(usuario_interfaz)
        prestamo.extender_prestamo(dias_transcurridos)
        self._gestor_prestamos.actualizar_prestamo(prestamo)
        usuario = prestamo.obtener_usuario()
        usuario_interfaz = usuario
        libro_actulizado = prestamo.obtener_libro()
        return (usuario_interfaz,libro_actulizado)
        
    def devolver_prestamo_libro(self,usuario,prestamo,dias_transcurridos):
        prestamo.establecer_usuario(usuario)
        prestamo.devolver_libro(dias_transcurridos)
        self._gestor_prestamos.actualizar_prestamo(prestamo)
        usuario = prestamo.obtener_usuario()
        libro = prestamo.obtener_libro()
        return (usuario,libro)
    def buscar_prestamo_por_id(self,id_prestamo):
        prestamos = self._gestor_prestamos.listar_prestamos_activos_detallado()
        for prestamo in prestamos:
            if prestamo.obtener_id() == id_prestamo:
                return prestamo
    def buscar_prestamo_por_id_libro(self,id_libro):
        prestamos = self._gestor_prestamos.listar_prestamos_activos_detallado()
        for prestamo in prestamos:
            if prestamo.obtener_libro().obtener_id() == id_libro:
                return prestamo
    def obtener_restamos_con_multas_pendientes(self,usuario):
        prestamos_filtrados = self._gestor_prestamos.filtrar_prestamos_por_usuario_con_multa(usuario)
        return prestamos_filtrados
    def pagar_multa(self,prestamo,usuario):
        prestamo.establecer_usuario(usuario)
        if isinstance(usuario,Estudiante):
            prestamo.hacer_horas_sociales_estudiante()
        elif isinstance(usuario,Docente):
            prestamo.pagar_multa_docente()
        usuario = prestamo.obtener_usuario()
        if isinstance(usuario,Estudiante):
            self.actualizar_datos_estudiante(usuario)
        elif isinstance(usuario,Docente):
            self.actualizar_datos_docente(usuario)
        self._gestor_prestamos.actualizar_prestamo(prestamo)
        verificador = self.verificar_multas_pendientes(usuario)
        if verificador == False:
            usuario.establecer_tiene_multa(False)
            if isinstance(usuario,Estudiante):
                self.actualizar_datos_estudiante(usuario)
            elif isinstance(usuario,Docente):
                self.actualizar_datos_docente(usuario)
    def mostrar_libros_mas_solicitados(self): pass
    def verificar_multas_pendientes(self,usuario):
        prestamos_pendientes = self._gestor_prestamos.filtrar_prestamos_por_usuario_con_multa(usuario)
        if len(prestamos_pendientes) == 0:
            return False
        else:
            return True
    def mostrar_prestamos_activos(self): pass
    def mostrar_historico_prestamo(self): pass
    
    #def eliminar_usuario_usuario(self): pass
    #def editar_usuario_usuario(self): pass