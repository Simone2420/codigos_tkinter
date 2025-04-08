class ProcesamientoDatos:
    def __init__(self,nombre,genero,actividades):
        self.nombre = nombre
        self.genero = genero
        self.actividades = actividades
    def procesar_datos(self):
        actividades = "Ninguna" if len(self.actividades) == 0 else ", ".join(self.actividades)
        
        datos = f"""Resumen de Datos:
• Nombre: {self.nombre}
• Género: {self.genero}
• Actividades: {actividades}"""
        return datos