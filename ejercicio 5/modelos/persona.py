from abc import ABC, abstractmethod
class Persona(ABC):
    nombre = ""
    identificacion = 0
    def __init__(self,nombre,identificacion):
        self.__nombre = nombre
        self.__identificacion = identificacion
    def obtener_nombre(self):
        return self.__nombre
    def obtener_identificacion(self):
        return self.__identificacion
    def establecer_nombre(self,nombre):
        self.__nombre = nombre
    def establecer_identificacion(self,identificacion):
        self.__identificacion = identificacion
    def __str__(self):
        return self.obtener_nombre()
    def __repr__(self):
        return self.obtener_nombre()