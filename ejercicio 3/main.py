import tkinter as tk
ventana = tk.Tk()
from tkinter import ttk, messagebox
from reportes import *
class Encuesta:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Encuesta de programación")
        self.ventana.geometry("1000x600")
        self.divisor_principal = tk.Frame(self.ventana)
        self.divisor_principal.grid(row=0,column=0,sticky="w",pady=25,padx=20)
        self.divisor_secundario = tk.Frame(self.ventana)
        self.divisor_secundario.grid(row=0,column=1,sticky="w")
        self.datos_personales = tk.Frame(self.divisor_principal)
        self.datos_personales.pack()
        self.interfaz_grafica()
    def interfaz_grafica(self):
        tk.Label(self.datos_personales, text="Nombre").grid(row=0,column=0)
        self.nombre = tk.Entry(self.datos_personales)
        self.nombre.grid(row=0,column=1)
        tk.Label(self.datos_personales, text="Genero").grid(row=2,column=0,padx=5,pady=5)
        self.genero = tk.StringVar(value="None")
        genero_1 = tk.Radiobutton(self.datos_personales, text="Masculino",variable=self.genero,value="Masculino")
        genero_1.grid(row=2,column=1)
        genero_2 = tk.Radiobutton(self.datos_personales, text="Femenino",variable=self.genero,value="Femenino")
        genero_2.grid(row=2,column=2)
        genero_3 = tk.Radiobutton(self.datos_personales, text="Otro",variable=self.genero,value="Otro")
        genero_3.grid(row=2,column=3)
        tk.Label(self.datos_personales, text="Edad").grid(row=1,column=0)
        self.edad = tk.Entry(self.datos_personales)
        self.edad.grid(row=1,column=1)
        tk.Label(self.divisor_principal, text="¿Cual es tu lenguaje de programación favorito?").pack()
        self.pregunta_1 = tk.Listbox(self.divisor_principal, selectmode=tk.SINGLE, height=5,justify="left",state="normal",exportselection=False)
        self.pregunta_1.pack(pady=10)
        lenguajes = ["Python", "JavaScript", "Java", "C#", "PHP", "Go"]
        for lenguaje in lenguajes:
            self.pregunta_1.insert(tk.END, lenguaje)
        tk.Label(self.divisor_principal, text="¿Cuantas horas al día le dedicas a programar?").pack()
        self.pregunta_2 = tk.Listbox(self.divisor_principal, selectmode=tk.SINGLE, height=5,justify="left",exportselection=False)
        self.pregunta_2.pack(pady=10)
        horas = ["1 hora o menos", "1 a 3 horas", "3 a 4 horas", "4 horas o mas"]
        for hora in horas:
            self.pregunta_2.insert(tk.END, hora)
        tk.Label(self.divisor_principal, text="¿Cuales lenguajes de programación sabes usar?").pack()
        self.pregunta_3 = tk.Listbox(self.divisor_principal, selectmode=tk.MULTIPLE, height=5,justify="left",exportselection=False)
        self.pregunta_3.pack(pady=10)
        lenguajes_usados = ["Python", "JavaScript", "Java", "C#", "PHP", "Go", "Otro"]
        for lenguaje_usado in lenguajes_usados:
            self.pregunta_3.insert(tk.END, lenguaje_usado)
        # For pregunta_1 (you already have part of this)
        tk.Label(self.divisor_secundario,text="¿Que opinas de python?").pack()
        self.comentario = tk.Text(self.divisor_secundario,height=4)
        self.comentario.pack()
        self.boton_enviar = tk.Button(self.divisor_secundario,text="Enviar",command=self.obtener_resultados)
        self.boton_enviar.pack(pady=20)
    def obtener_resultados(self):
        nombre = self.nombre.get()
        try:
            edad = int(self.edad.get())
        except ValueError:
            edad = "Edad ingresada en formato invalido"
        genero = self.genero.get()
        pregunta_1 = self.obtener_respuesta_pregunta_1()
        pregunta_2 = self.obtener_respuesta_pregunta_2()
        pregunta_3 = self.obtener_respuesta_pregunta_3()
        comentario = self.comentario.get("1.0", tk.END).strip()
        reporte = Reporte(nombre, genero, edad, pregunta_1, pregunta_2, pregunta_3, comentario)
        resultados = reporte.obtener_resultados()
        mensaje = reporte.verificar_ingreso_datos(nombre, genero, edad, pregunta_1, pregunta_2, pregunta_3)
        if mensaje != True:
            messagebox.showerror("Datos faltantes:", f"Datos faltantes: {mensaje}")
        else:
            if hasattr(self, 'label_resultados'):
                self.label_resultados.destroy()
                self.conclusion.destroy()
            conclusion = reporte.realizar_conclusion()
            self.label_resultados = tk.Label(
                self.divisor_secundario,
                text=resultados,
                anchor='w',
                justify='left',
                wraplength=400  # Ajustar según necesidad
            )
            self.label_resultados.pack(pady=10)
            self.conclusion = tk.Label(
                self.divisor_secundario,
                text=conclusion,
                anchor='w',
                justify='left',
                wraplength=400  # Ajustar según necesidad
            )
            self.conclusion.pack(pady=10)
            # Resetear campos
            self.resetear_campos()

    def resetear_campos(self):
        """Función para limpiar todos los campos del formulario"""
        self.nombre.delete(0, tk.END)
        self.edad.delete(0, tk.END)
        self.genero.set("None")
        self.pregunta_1.selection_clear(0, tk.END)
        self.pregunta_2.selection_clear(0, tk.END)
        self.pregunta_3.selection_clear(0, tk.END)
        self.comentario.delete("1.0", tk.END)
    def obtener_respuesta_pregunta_1(self):
        try:
            indice_seleccionado = self.pregunta_1.curselection()[0]  # [0] toma el primer índice seleccionado
            pregunta_1_seleccion = self.pregunta_1.get(indice_seleccionado)
        except IndexError:
            pregunta_1_seleccion = "Nada seleccionado"
        finally:
            return pregunta_1_seleccion
    def obtener_respuesta_pregunta_2(self):
        try:
            indice_seleccionado = self.pregunta_2.curselection()[0]  # [0] toma el primer índice seleccionado
            pregunta_2_seleccion = self.pregunta_2.get(indice_seleccionado)
        except IndexError:
            pregunta_2_seleccion = "Nada seleccionado"
        finally:
            return pregunta_2_seleccion
    def obtener_respuesta_pregunta_3(self): 
        try:
            seleccion_pregunta_3 = [self.pregunta_3.get(i) for i in self.pregunta_3.curselection()]
            if seleccion_pregunta_3 == []:
                raise IndexError
        except IndexError:
            seleccion_pregunta_3 = "Nada seleccionado"
        finally:
            return seleccion_pregunta_3

app = Encuesta(ventana)
ventana.mainloop()