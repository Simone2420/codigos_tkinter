import tkinter as tk
ventana = tk.Tk()
from tkinter import ttk, messagebox
from reportes import *
class Encuesta:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Encuesta de programación")
        self.ventana.geometry("1000x1000")
        self.ventana.configure(bg="#f0f0f0")
        self.divisor_principal = tk.Frame(self.ventana, bg="#f0f0f0", padx=30, pady=10)
        self.divisor_principal.grid(row=0,column=0,sticky="w",pady=25,padx=20)
        self.divisor_secundario = tk.Frame(self.ventana, bg="#f0f0f0", padx=30, pady=20)
        self.divisor_secundario.grid(row=0,column=1,sticky="w")
        self.datos_personales = tk.Frame(self.divisor_principal, bg="#f0f0f0", padx=20, pady=15)
        self.datos_personales.pack()
        self.interfaz_grafica()
    def interfaz_grafica(self):
        # Estilos generales
        estilo_label = {"bg": "#f0f0f0", "font": ("Arial", 12), "pady": 5}
        estilo_entry = {"font": ("Arial", 12), "width": 25, "relief": "solid", "bd": 1}
        estilo_radio = {"bg": "#f0f0f0", "font": ("Arial", 11), "pady": 2}
        estilo_listbox = {"font": ("Arial", 11), "relief": "solid", "bd": 1, "height": 5, "width": 30, "exportselection": False}

        # Sección datos personales
        tk.Label(self.datos_personales, text="Datos Personales", font=("Arial", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=4)

        tk.Label(self.datos_personales, text="Nombre", **estilo_label).grid(row=1,column=0)
        self.nombre = tk.Entry(self.datos_personales, **estilo_entry)
        self.nombre.grid(row=1,column=1, columnspan=3, pady=5)

        tk.Label(self.datos_personales, text="Edad", **estilo_label).grid(row=2,column=0)
        self.edad = tk.Entry(self.datos_personales, **estilo_entry)
        self.edad.grid(row=2,column=1, columnspan=3, pady=5)

        tk.Label(self.datos_personales, text="Género", **estilo_label).grid(row=3,column=0,padx=5,pady=10)
        self.genero = tk.StringVar(value="None")
        genero_1 = tk.Radiobutton(self.datos_personales, text="Masculino",variable=self.genero,value="Masculino", **estilo_radio)
        genero_1.grid(row=3,column=1)
        genero_2 = tk.Radiobutton(self.datos_personales, text="Femenino",variable=self.genero,value="Femenino", **estilo_radio)
        genero_2.grid(row=3,column=2)
        genero_3 = tk.Radiobutton(self.datos_personales, text="Otro",variable=self.genero,value="Otro", **estilo_radio)
        genero_3.grid(row=3,column=3)

        # Sección preguntas
        tk.Label(self.divisor_principal, text="Preguntas de la Encuesta", font=("Arial", 14, "bold"), bg="#f0f0f0", pady=15).pack()

        tk.Label(self.divisor_principal, text="¿Cuál es tu lenguaje de programación favorito?", **estilo_label).pack()
        self.pregunta_1 = tk.Listbox(self.divisor_principal, selectmode= tk.SINGLE, **estilo_listbox)
        self.pregunta_1.pack(pady=10)
        lenguajes = ["Python", "JavaScript", "Java", "C#", "PHP", "Go"]
        for lenguaje in lenguajes:
            self.pregunta_1.insert(tk.END, lenguaje)

        tk.Label(self.divisor_principal, text="¿Cuántas horas al día le dedicas a programar?", **estilo_label).pack()
        self.pregunta_2 = tk.Listbox(self.divisor_principal, selectmode= tk.SINGLE, **estilo_listbox)
        self.pregunta_2.pack(pady=10)
        horas = ["1 hora o menos", "1 a 3 horas", "3 a 4 horas", "4 horas o más"]
        for hora in horas:
            self.pregunta_2.insert(tk.END, hora)

        tk.Label(self.divisor_secundario, text="¿Cuáles lenguajes de programación sabes usar?", **estilo_label).pack()
        self.pregunta_3 = tk.Listbox(self.divisor_secundario, selectmode=tk.MULTIPLE, **estilo_listbox)
        self.pregunta_3.pack(pady=10)
        lenguajes_usados = ["Python", "JavaScript", "Java", "C#", "PHP", "Go", "Otro"]
        for lenguaje_usado in lenguajes_usados:
            self.pregunta_3.insert(tk.END, lenguaje_usado)

        # Sección comentario
        tk.Label(self.divisor_secundario, text="¿Qué opinas de Python?", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
        self.comentario = tk.Text(self.divisor_secundario, height=4, width=40, font=("Arial", 11), relief="solid", bd=1)
        self.comentario.pack(pady=10)

        # Botón enviar
        self.boton_enviar = tk.Button(self.divisor_secundario, text="Enviar", command=self.obtener_resultados,
                                    font=("Arial", 12), bg="#4CAF50", fg="white",
                                    padx=20, pady=8, cursor="hand2", relief="raised")
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
        mensaje = reporte.verificar_ingreso_datos(nombre, genero, edad, pregunta_1, pregunta_2, pregunta_3)
        if mensaje != True:
            messagebox.showerror("Datos faltantes:", f"Datos faltantes: {mensaje}")
        
        else:
            resultados = reporte.obtener_resultados()
            conclusion = reporte.realizar_conclusion()
            if hasattr(self, 'frame_resultados'):
                self.frame_resultados.destroy()
            
            # Crear frame con scroll para los resultados
            self.frame_resultados = tk.Frame(self.divisor_secundario, bg="#f5f5f5", relief="solid", bd=1)
            self.frame_resultados.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Configurar canvas y scrollbar
            canvas = tk.Canvas(self.frame_resultados, bg="#f5f5f5", highlightthickness=0)
            scrollbar = ttk.Scrollbar(self.frame_resultados, orient="vertical", command=canvas.yview)
            frame_contenido = tk.Frame(canvas, bg="#f5f5f5")
            
            # Configurar el canvas
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Crear ventana en el canvas
            canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
            
            # Crear labels con estilo mejorado
            self.label_resultados = tk.Label(
                frame_contenido,
                text=resultados,
                anchor='w',
                justify='left',
                wraplength=350,
                bg="#f5f5f5",
                font=("Arial", 11),
                padx=10,
                pady=5
            )
            self.label_resultados.pack(fill="x", pady=5)
            
            self.conclusion = tk.Label(
                frame_contenido,
                text=conclusion,
                anchor='w',
                justify='left',
                wraplength=350,
                bg="#f5f5f5",
                font=("Arial", 11),
                padx=10,
                pady=5
            )
            self.conclusion.pack(fill="x", pady=5)
            
            # Actualizar el scroll region
            frame_contenido.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
            
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
            indice_seleccionado = self.pregunta_1.curselection()[0]  
            pregunta_1_seleccion = self.pregunta_1.get(indice_seleccionado)
        except IndexError:
            pregunta_1_seleccion = "Nada seleccionado"
        finally:
            return pregunta_1_seleccion
    def obtener_respuesta_pregunta_2(self):
        try:
            indice_seleccionado = self.pregunta_2.curselection()[0]  
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