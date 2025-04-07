class GestorLibros:
    libros = []
    libros_disponibles = []
    def __init__(self,base_datos_proxy):
        self.base_datos_proxy = base_datos_proxy
        self._libros = self.base_datos_proxy.obtener_libros()
        self._libros_disponibles = self._libros.copy()
    def obtener_libros(self):
        return self._libros
    def obtener_libros_disponibles(self):
        return self._libros_disponibles
    def actualizar_datos_libro(self,libro):
        self.base_datos_proxy.actualizar_datos_libro(libro)
    def registrar_libro(self,nuevo_libro):
        self._libros_disponibles.append(nuevo_libro)
        self.base_datos_proxy.registrar_datos_libro(nuevo_libro)
    def quitar_libro(self,indice_libro):
        return self._libros_disponibles.pop(indice_libro)
    def mostrar_todos_los_libros(self):
        return self._libros
    def mostrar_libros_disponibles(self):
        libros_filtrados = [libro for libro in self._libros_disponibles if libro.obtener_esta_disponible() == True or libro.obtener_esta_disponible() == 1]
        return libros_filtrados
    def mostrar_libros_por_categoria(self,categoria_elegida):
        libros_filtrados = [libro for libro in self._libros if libro.obtener_categoria() == categoria_elegida]
        if libros_filtrados == []:
            return False
        return libros_filtrados
    
    def libros_mas_solicitados(self, top=None):
        libros_ordenados = sorted(self._libros, key=lambda libro: libro.obtener_numero_veces_solicitado(), reverse=True)
        if top is not None and isinstance(top,int):
            libros_ordenados[:top]
        return [(libro, libro.obtener_numero_veces_solicitado()) for libro in libros_ordenados]
