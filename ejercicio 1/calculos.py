class Calculos:
    def __init__(self,numero_1,numero_2,operacion):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.operacion = operacion
    def sumar(self):
        return self.numero_1 + self.numero_2
    def restar(self):
        return self.numero_1 - self.numero_2
    def multiplicar(self): 
        return self.numero_1 * self.numero_2
    def dividir(self):
        if self.numero_2 == 0: return "Error no se puede dividir por cero"
        else: return self.numero_1/self.numero_2
    def ejecutar_operacion(self):
        if self.operacion == "sumar":
            return self.sumar()
        elif self.operacion == "restar":
            return self.restar()
        elif self.operacion == "multiplicar":
            return self.multiplicar()
        elif self.operacion == "dividir":
            return self.dividir()