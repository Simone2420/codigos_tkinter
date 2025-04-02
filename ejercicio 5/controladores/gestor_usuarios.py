import os
def limpiar_consola():
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para Linux/macOS
        os.system('clear')
class GestorUsuarios():
    docentes = []
    estudiantes = []
    usuarios = []
    def __init__(self,estudiantes,docentes):
        self._docentes = docentes
        self._estudiantes = estudiantes
        self._usuarios = docentes + estudiantes
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
            self._estudiantes.append(usuario)
        elif usuario.obtener_tipo() == "docente":
            self._docentes.append(usuario)
        self._usuarios.append(usuario)  # Agregar a la lista unificada
        return f"Usuario {usuario.obtener_nombre()} de tipo {usuario.obtener_tipo()} fue registrado correctamente."

    def buscar_usuario(self, identificacion):
        """Busca un usuario por su identificación."""
        for usuario in self._usuarios:
            if usuario.obtener_identificacion() == identificacion:
                return usuario
        return None 
    def ingresar_docente(self,identificacion,id_profesional):
        for docente in self._docentes:
            if docente.obtener_identificacion() == identificacion and docente.obtener_id_profesional() == id_profesional:
                return docente
        return False
    def ingresar_estudiante(self,identificacion,numero_matricula):
        for estudiante in self._estudiantes:
            if estudiante.obtener_identificacion() == identificacion and estudiante.obtener_numero_matricula() == numero_matricula:
                return estudiante
        return False
    def listar_estudiantes(self):
        if not self._estudiantes:
            print("No hay docentes registrados.")
            return
        for estudiante in self._estudiantes:
            limpiar_consola()  
            estudiante.mostrar_informacion()  
            input("Presione Enter para ver el siguiente docente...")  
        print("No hay más docentes para mostrar.")

    def listar_docentes(self):
        if not self._docentes:
            print("No hay docentes registrados.")
            return
        for docente in self._docentes:
            limpiar_consola()  
            docente.mostrar_informacion()  
            input("Presione Enter para ver el siguiente docente...")  
        print("No hay más docentes para mostrar.")

    def listar_usuarios(self):
        return self._usuarios

