import tkinter as tk
from tkinter import ttk, messagebox
from procesamiento_datos import *
ventana = tk.Tk()
class Formulario:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("500x600")
        self.ventana.title("Formulario de Intereses")
        self.ventana.configure(bg="#f0f0f0")
        self.interfaz_grafica()
    def interfaz_grafica(self):
        # Frame principal con estilo
        self.divisor_principal = tk.Frame(self.ventana, bg="#f0f0f0", padx=20, pady=20)
        self.divisor_principal.pack(pady=30)

        # Estilo para las etiquetas
        estilo_label = {"bg": "#f0f0f0", "font": ("Arial", 12), "pady": 5}
        estilo_entry = {"font": ("Arial", 12), "width": 20}
        estilo_radio = {"bg": "#f0f0f0", "font": ("Arial", 10), "pady": 2}

        # Sección Nombre
        tk.Label(self.divisor_principal, text="Nombre", **estilo_label).grid(row=0, column=0, padx=10, pady=10)
        self.nombre = tk.Entry(self.divisor_principal, **estilo_entry)
        self.nombre.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        # Sección Género
        tk.Label(self.divisor_principal, text="Género", **estilo_label).grid(row=1, column=0, padx=10, pady=10)
        self.genero = tk.StringVar(value="None")
        genero_1 = tk.Radiobutton(self.divisor_principal, text="Masculino", variable=self.genero, value="Masculino", **estilo_radio)
        genero_1.grid(row=1, column=1)
        genero_2 = tk.Radiobutton(self.divisor_principal, text="Femenino", variable=self.genero, value="Femenino", **estilo_radio)
        genero_2.grid(row=1, column=2)
        genero_3 = tk.Radiobutton(self.divisor_principal, text="Otro", variable=self.genero, value="Otro", **estilo_radio)
        genero_3.grid(row=1, column=3)

        # Frame secundario para intereses
        self.divisor_secundario = tk.Frame(self.ventana, bg="#f0f0f0", padx=20, pady=20)
        self.divisor_secundario.pack(pady=20)

        # Título para la sección de intereses
        tk.Label(self.divisor_secundario, text="Intereses", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        # Estilo para los checkbuttons
        estilo_check = {"bg": "#f0f0f0", "font": ("Arial", 11), "pady": 5}

        # Checkbuttons de intereses
        self.actividad_1 = tk.IntVar()
        actividad_1 = tk.Checkbutton(self.divisor_secundario, text="Deportes", variable=self.actividad_1, **estilo_check)
        actividad_1.pack()

        self.actividad_2 = tk.IntVar()
        actividad_2 = tk.Checkbutton(self.divisor_secundario, text="Música", variable=self.actividad_2, **estilo_check)
        actividad_2.pack()

        self.actividad_3 = tk.IntVar()
        actividad_3 = tk.Checkbutton(self.divisor_secundario, text="Cocina", variable=self.actividad_3, **estilo_check)
        actividad_3.pack()

        self.actividad_4 = tk.IntVar()
        actividad_4 = tk.Checkbutton(self.divisor_secundario, text="Literatura", variable=self.actividad_4, **estilo_check)
        actividad_4.pack()

        # Botón enviar con estilo
        boton_enviar = tk.Button(self.ventana, text="Enviar", command=self.registrar_datos,
                                font=("Arial", 12), bg="#4CAF50", fg="white",
                                padx=20, pady=10, cursor="hand2")
        boton_enviar.pack(pady=20)
    def registrar_datos(self):
        nombre = self.nombre.get()
        genero = self.genero.get()
        actividad_1 = self.actividad_1.get()
        actividad_2 = self.actividad_2.get()
        actividad_3 = self.actividad_3.get()
        actividad_4 = self.actividad_4.get()
        actividades = [actividad_1, actividad_2, actividad_3, actividad_4]
        actividades_en_texto = []
        for i, actividad in enumerate(actividades): 
            if i == 0 and actividad == 1:
                actividades_en_texto.append("Deportes")
            elif i == 1 and actividad == 1:
                actividades_en_texto.append("Música")
            elif i == 2 and actividad == 1:
                actividades_en_texto.append("Cocina")
            elif i == 3 and actividad == 1:
                actividades_en_texto.append("Literatura")
        proceso_datos = ProcesamientoDatos(nombre,genero,actividades_en_texto)
        datos_no_ingresado = []
        if not nombre:
            datos_no_ingresado.append("Nombre")
        if genero == "None":
            datos_no_ingresado.append("Genero")
        if not actividades_en_texto:
            datos_no_ingresado.append("Actividades")
        if not datos_no_ingresado:
            messagebox.showinfo("Datos ingresados",proceso_datos.procesar_datos())
        else:
            datos_faltantes = ", ".join(datos_no_ingresado)
            messagebox.showerror("Datos faltantes", f"Datos faltantes: {datos_faltantes}")

app = Formulario(ventana)
ventana.mainloop()