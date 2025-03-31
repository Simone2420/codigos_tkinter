import tkinter as tk
from tkinter import ttk
from calculos import *
ventana = tk.Tk()

class Calculadora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("400x400")
        self.ventana.title("Calculadora Básica")
        self.interfaz_grafica()
    def interfaz_grafica(self):
        tk.Label(self.ventana, text="Número 1").grid(row=0,column=0,padx=5,pady=5)
        self.numero_1 = tk.Entry(self.ventana)
        self.numero_1.grid(row=0,column=1)
        tk.Label(self.ventana, text="Número 2").grid(row=1,column=0,padx=5,pady=5)
        self.numero_2 = tk.Entry(self.ventana)
        self.numero_2.grid(row=1,column=1)
        tk.Label(self.ventana, text="Operación").grid(row=2,column=0,padx=5,pady=5)
        self.operacion = ttk.Combobox(
            self.ventana,
            values=["sumar","restar","multiplicar","dividir"])
        self.operacion.grid(row=2,column=1,pady=5)
        boton_calcular = tk.Button(self.ventana, text="calcular",command=self.ejecutar_calculo)
        boton_calcular.grid(row=3,column=0,pady=5)
    def ejecutar_calculo(self):
        numero_1 = int(self.numero_1.get())
        numero_2 = int(self.numero_2.get())
        operacion = self.operacion.get()
        calculo= Calculos(numero_1,numero_2,operacion)
        resultado = calculo.ejecutar_operacion()
        print(resultado)
        self.resultado = tk.Label(self.ventana,text=f"El resultado es {str(resultado)}")
        self.resultado.grid(row=4, column=0,pady=5)

app = Calculadora(ventana)
ventana.mainloop()
