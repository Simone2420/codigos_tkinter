import tkinter as tk
from tkinter import ttk, messagebox
ventana = tk.Tk()
class Formulario:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("400x400")
        self.ventana.title("Formulario simple")
        self.interfaz_grafica()
    def interfaz_grafica(self):
        self.divisor_principal = tk.Frame(self.ventana)
        self.divisor_principal.pack(pady=30)
        tk.Label(self.divisor_principal, text="Nombre").grid(row=0,column=0,padx=5,pady=5)
        self.nombre = tk.Entry(self.divisor_principal)
        self.nombre.grid(row=0,column=1)
        tk.Label(self.divisor_principal, text="Genero").grid(row=1,column=0,padx=5,pady=5)
        self.genero = tk.StringVar(value="None")
        genero_1 = tk.Radiobutton(self.divisor_principal, text="Masculino",variable=self.genero,value="Masculino")
        genero_1.grid(row=1,column=1)
        genero_2 = tk.Radiobutton(self.divisor_principal, text="Femenino",variable=self.genero,value="Femenino")
        genero_2.grid(row=1,column=2)
        genero_3 = tk.Radiobutton(self.divisor_principal, text="Otro",variable=self.genero,value="Otro")
        genero_3.grid(row=1,column=3)
        self.divisor_secundario = tk.Frame(self.ventana)
        self.divisor_secundario.pack(pady=30)
        self.actividad_1 = tk.IntVar()
        actividad_1 = tk.Checkbutton(self.divisor_secundario,text="Baloncesto",variable=self.actividad_1)
        actividad_1.pack()
        self.actividad_2 = tk.IntVar()
        actividad_2 = tk.Checkbutton(self.divisor_secundario,text="Futbol",variable=self.actividad_2)
        actividad_2.pack()
        self.actividad_3 = tk.IntVar()
        actividad_3 = tk.Checkbutton(self.divisor_secundario,text="Voleibol",variable=self.actividad_3)
        actividad_3.pack()
        self.actividad_4 = tk.IntVar()
        actividad_4 = tk.Checkbutton(self.divisor_secundario,text="Tenis",variable=self.actividad_4)
        actividad_4.pack()
        boton_enviar = tk.Button(self.ventana, text="Enviar",command=self.registrar_datos)
        boton_enviar.pack()
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
                actividades_en_texto.append("Baloncesto")
            elif i == 1 and actividad == 1:
                actividades_en_texto.append("Futbol")
            elif i == 2 and actividad == 1:
                actividades_en_texto.append("Voleibol")
            elif i == 3 and actividad == 1:
                actividades_en_texto.append("Tenis")
        proceso_datos = ProcesamientoDatos(nombre,genero,actividades_en_texto)
        datos_no_ingresado = []
        if not nombre:
            datos_no_ingresado.append("Nombre")
        if genero == "None":
            datos_no_ingresado.append("Genero")
        if not actividades_en_texto:
            datos_no_ingresado.append("Actividades")
        datos_faltantes = ""
        for datos in datos_no_ingresado:
            datos_faltantes += datos + ", "
        if not datos_no_ingresado:
            messagebox.showinfo("Datos ingresados",proceso_datos.procesar_datos())
        else:
            messagebox.showerror("Datos faltantes:",f"Datos faltantes: {datos_faltantes}")
class ProcesamientoDatos:
    def __init__(self,nombre,genero,actividades):
        self.nombre = nombre
        self.genero = genero
        self.actividades = actividades
    def procesar_datos(self):
        actividades = ""
        if len(self.actividades) == 0:
            actividades = "Ninguna"
        else: 
            for actividad in self.actividades:
                    actividades += actividad + ", "
                    
        datos = f"""
        Nombre {self.nombre}
        Genero {self.genero}
        Actividades {actividades}
        """
        return datos
app = Formulario(ventana)
ventana.mainloop()