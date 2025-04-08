import tkinter as tk
from tkinter import ttk
from calculos import *
ventana = tk.Tk()

class Calculadora:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("800x500")
        self.ventana.title("Calculadora Básica")
        self.ventana.configure(bg="#f0f0f0")
        self.texto_resultado = None
        self.interfaz_grafica()
    def interfaz_grafica(self):
        # Frame principal
        frame = tk.Frame(self.ventana, bg="#f0f0f0", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Estilo para las etiquetas
        estilo_label = {"bg": "#f0f0f0", "font": ("Arial", 12), "pady": 5}
        
        # Número 1
        tk.Label(frame, text="Número 1", **estilo_label).grid(row=0, column=0, padx=10, pady=10)
        self.numero_1 = tk.Entry(frame, font=("Arial", 12), width=15)
        self.numero_1.grid(row=0, column=1, padx=10, pady=10)
        
        # Número 2
        tk.Label(frame, text="Número 2", **estilo_label).grid(row=1, column=0, padx=10, pady=10)
        self.numero_2 = tk.Entry(frame, font=("Arial", 12), width=15)
        self.numero_2.grid(row=1, column=1, padx=10, pady=10)
        
        # Operación
        tk.Label(frame, text="Operación", **estilo_label).grid(row=2, column=0, padx=10, pady=10)
        self.operacion = ttk.Combobox(frame, values=["sumar","restar","multiplicar","dividir"], 
        font=("Arial", 12), width=12)
        self.operacion.grid(row=2, column=1, padx=10, pady=10)
        self.operacion.set("sumar")
        
        # Botón calcular
        estilo_boton = {}
        boton_calcular = tk.Button(frame, text="Calcular", command=self.ejecutar_calculo, **estilo_boton)
        boton_calcular.grid(row=3, column=0, columnspan=2, pady=20)
    def ejecutar_calculo(self):
        try:
            # Limpiar resultado anterior si existe
            if self.texto_resultado:
                self.texto_resultado.destroy()
            
            numero_1 = int(self.numero_1.get())
            numero_2 = int(self.numero_2.get())
            operacion = self.operacion.get()
            calculo = Calculos(numero_1, numero_2, operacion)
            resultado = calculo.ejecutar_operacion()
            
            # Crear nuevo label con el resultado
            frame = self.ventana.winfo_children()[0]
            self.texto_resultado = tk.Label(frame,
                text=f"El resultado es: {str(resultado)}",
                font=("Arial", 14, "bold"),
                bg="#f0f0f0",
                fg="#2E7D32")
            self.texto_resultado.grid(row=4, column=0, columnspan=2, pady=20)
        except ValueError:
            if self.texto_resultado:
                self.texto_resultado.destroy()
            self.texto_resultado = tk.Label(frame,
                text="Error: Ingrese números válidos",
                font=("Arial", 12),
                bg="#f0f0f0",
                fg="#D32F2F")
            self.texto_resultado.grid(row=4, column=0, columnspan=2, pady=20)
    def actulizar_resultado(self,resultado):
        self.resultado = resultado
app = Calculadora(ventana)
ventana.mainloop()
