from .excepciones import EstadoInvalido
class Libro:
    titulo = ""
    autor = ""
    ano_publicacion = 0
    disponible = True
    categoria = ""
    numero_veces_solicitado = 0
    def __init__(self, titulo, autor, ano_publicacion,categoria):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacion = ano_publicacion
        self._disponible = True
        self._categoria = categoria
        self._numero_veces_solicitado = 0  
    def obtener_titulo(self):
        return self._titulo
    def obtener_autor(self):
        return self._autor
    def obtener_ano_publicacion(self):
        return self._ano_publicacion
    def obtener_esta_disponible(self):
        return self._disponible
    def obtener_categoria(self):
        return self._categoria
    def obtener_numero_veces_solicitado(self):
        return self._numero_veces_solicitado
    def actualizar_numero_veces_solicitado(self):
        self._numero_veces_solicitado += 1
    def mostrar_informacion(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Año de publicacion: {self._ano_publicacion}")
        print(f"Estado de disponibilidad {self._disponible}")
        print(f"Categoria: {self._categoria}")
        print(f"Numero veces solicitados: {self._numero_veces_solicitado}")
    def establecer_estado(self,nuevo_estado):
        try:
            if nuevo_estado == True:
                self._disponible = nuevo_estado
            elif nuevo_estado == False:
                self._disponible = nuevo_estado
            else:
                raise EstadoInvalido()
        except EstadoInvalido as e:
            print(f"Error: {e}")
    def __str__(self):
        return self.obtener_titulo()
    def __repr__(self):
        return self.obtener_titulo()