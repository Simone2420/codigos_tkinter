class LibroNoDisponible(Exception):
    def __init__(self, mensaje="El libro no está disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class EstadoInvalido(Exception):
    def __init__(self, mensaje="Solo se admite True o False"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class LimitePrestamosExcedido(Exception):
    """Excepción lanzada cuando un usuario excede su límite de préstamos."""
    def __init__(self, mensaje="El usuario ha excedido su límite de préstamos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class NoHayLibroParaDevolver(Exception):
    """Excepcion lanzada cuando el usuario no tiene libros para devolver."""
    def __init__(self, mensaje="El usuario no tiene libros para devolver"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class DatosInvalidos(Exception):
    """Excepción lanzada cuando los datos ingresados son inválidos."""
    def __init__(self, mensaje="Los datos ingresados son inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class OpcionInvalida(Exception): 
    def __init__(self,mensaje="Opcion invalida"):
        self.mensaje = mensaje
class IdentificacionRepetida(Exception):
    def __init__(self,mensaje="La identificacion ingresada ya la tiene registrada un usuario del sistema)"):
        self.mensaje = mensaje
class UsuarioNoEncontrado(Exception):
    def __init__(self,mensaje="El usuario no fue encontrado"):
        self.mensaje = mensaje
class MultaNoPagada(Exception):
    def __init__(self, mensaje="El usuario tiene que pagar su multa"):
        self.mensaje = mensaje
class LibroYaDevuelto(Exception):
    def __init__(self,mensaje="El usuario ya devolvio el libro"):
        self.mensaje = mensaje