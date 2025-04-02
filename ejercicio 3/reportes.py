class Reporte:
    def __init__(self,nombre,genero,edad,respuesta_1,respuesta_2,respuesta_3,comentario):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.respuesta_1 = respuesta_1
        self.respuesta_2 = respuesta_2
        self.respuesta_3 = respuesta_3
        self.comentario = comentario
    def obtener_resultados(self): 
        comentario_formateado = ""
        if self.comentario: 
            lineas = self.comentario.split('\n')
            comentario_formateado = "\n    ".join(lineas)  # 4 espacios de sangría
    
        respuesta = f"""
Nombre ingresado: {self.nombre}
Genero ingresado: {self.genero}
Edad ingresada: {self.edad}
Respuesta ingresada a la pregunta 1: {self.respuesta_1}
Respuesta ingresada a la pregunta 2: {self.respuesta_2}
Respuestas ingresadas a la pregunta 3: {', '.join(self.respuesta_3) if isinstance(self.respuesta_3, list) else self.respuesta_3}
Comentario ingresado:
    {comentario_formateado}
"""
        return respuesta
    def realizar_conclusion(self):
        conclusion = ""
        cualidad_edad = ""
        cualidad_manejo_lenguajes_de_programacion = ""
        opina = ""
        if self.edad >= 1 and self.edad <= 10:
            cualidad_edad = "muy joven"
        elif self.edad > 10 and self.edad <= 20:
            cualidad_edad = "joven"
        elif self.edad > 20 and self.edad <=35:
            cualidad_edad = "adulto joven"
        elif self.edad > 35 and self.edad <=55:
            cualidad_edad = "adulto experimentado"
        elif self.edad > 55 and self.edad <= 80:
            cualidad_edad = "adulto mayor"
        elif self.edad > 80 and self.edad <= 120:
            cualidad_edad = "una roca por que vive mucho"
        if len(self.respuesta_3) == 1:
            cualidad_manejo_lenguajes_de_programacion = "un solo lenguaje de programación"
        elif len(self.respuesta_3) == 2 or len(self.respuesta_3) == 3:
            cualidad_manejo_lenguajes_de_programacion = "pocos lenguajes de programación"
        elif len(self.respuesta_3) >= 4:
            cualidad_manejo_lenguajes_de_programacion = "muchos lenguajes de programación"
        if not self.comentario:
            opina = "no le gusta opinar"
        else:
            opina = "le gusta opinar"
        conclusion = f"""
Se puede concluir que:
    
    • El usuario {self.nombre} tiene {self.edad} años, lo que significa que es {cualidad_edad}.
    • Es del género {self.genero}.
    • Su lenguaje favorito es {self.respuesta_1}.
    • Le dedica {self.respuesta_2.lower()} a programar.
    • Sabe manejar {cualidad_manejo_lenguajes_de_programacion}.
    • Y {opina} sobre Python.
"""
        return conclusion
    def verificar_ingreso_datos(self, nombre, genero, edad, respuesta_1, respuesta_2, respuesta_3):
        problemas = []
        if not nombre.strip():
            problemas.append("• Nombre no ingresado")
        if genero == "None":
            problemas.append("• Género no seleccionado")
        if not edad:
            problemas.append("• Edad no ingresada")
        elif edad == "Edad ingresada en formato invalido":
            problemas.append("• Edad debe ser un número válido")
        elif edad < 1 or int(edad) > 120:
            problemas.append("• Edad fuera de rango (1-120 años)")
        if respuesta_1 == "Nada seleccionado":
            problemas.append("• Pregunta 1: Lenguaje favorito no seleccionado")
        if respuesta_2 == "Nada seleccionado":
            problemas.append("• Pregunta 2: Horas de programación no seleccionadas")
        if respuesta_3 == "Nada seleccionado":
            problemas.append("• Pregunta 3: Lenguajes conocidos no seleccionados")
        elif isinstance(respuesta_3, list) and not respuesta_3:
            problemas.append("• Pregunta 3: Debe seleccionar al menos un lenguaje")
        if problemas:
            mensaje = "Por favor complete los siguientes campos:\n\n" + "\n".join(problemas)
            return mensaje
        else:
            return True