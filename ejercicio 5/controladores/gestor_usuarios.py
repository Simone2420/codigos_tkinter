class GestorUsuarios():
    docentes = []
    estudiantes = []
    usuarios = []
    def __init__(self,base_datos_proxy):
        self.base_datos_proxy = base_datos_proxy
        self._docentes = self.base_datos_proxy.obtener_docentes()
        self._estudiantes = self.base_datos_proxy.obtener_estudiantes()
        self._usuarios = self.docentes + self.estudiantes
    def obtener_docentes(self):
        return self._docentes
    def obtener_estudiantes(self):
        return self._estudiantes
    def obtener_usuarios(self):
        return self._usuarios
    def existe_usuario(self, identificacion):
        return any(usuario.identificacion == identificacion for usuario in self._usuarios)
    def registrar_usuario_nuevo(self, usuario):
        """Registra un nuevo usuario si no existe uno con la misma identificación."""
        if self.existe_usuario(usuario.obtener_identificacion()):
            return False
        if usuario.obtener_tipo() == "estudiante":
            self.base_datos_proxy.registrar_estudiante(usuario)
        elif usuario.obtener_tipo() == "docente":
            self.base_datos_proxy.registrar_docente(usuario)
        self._usuarios.append(usuario)  # Agregar a la lista unificada
        return f"Usuario {usuario.obtener_nombre()} de tipo {usuario.obtener_tipo()} fue registrado correctamente."
    def actualizar_docente(self,docente):
        self.base_datos_proxy.actualizar_docente(docente)
    def actualizar_estudiante(self,estudiante):
        self.base_datos_proxy.actualizar_estudiante(estudiante)
    def buscar_usuario(self, identificacion):
        """Busca un usuario por su identificación."""
        for usuario in self._usuarios:
            if usuario.obtener_identificacion() == identificacion:
                return usuario
        return None 
    def ingresar_docente(self,nombre_docente,identificacion,id_profesional):
        for docente in self._docentes:
            if docente.obtener_nombre() == nombre_docente and docente.obtener_identificacion() == identificacion and docente.obtener_id_profesional() == id_profesional:
                return docente
        return False
    def ingresar_estudiante(self,nombre_estudiante,identificacion,numero_matricula):
        for estudiante in self._estudiantes:
            if estudiante.obtener_nombre() == nombre_estudiante and estudiante.obtener_identificacion() == identificacion and estudiante.obtener_numero_matricula() == numero_matricula:
                return estudiante
        return False
    def listar_estudiantes(self):
        if not self._estudiantes:
            print("No hay docentes registrados.")
            return False
        return self._estudiantes          

    def listar_docentes(self):
        if not self._docentes:
            print("No hay docentes registrados.")
            return False
        return self._docentes

    def listar_usuarios(self):
        return self._usuarios

