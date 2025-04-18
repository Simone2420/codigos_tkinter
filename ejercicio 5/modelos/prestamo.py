from datetime import datetime, timedelta
from .excepciones import *
import random
from .usuarios import Docente,Estudiante
from .libro import Libro
import time
class Prestamo:
    usuario = None
    libro = None
    fecha_prestamo = None
    fecha_devolucion = None 
    fecha_de_reasignacion = None
    fecha_devolucion_esperada = None
    valor_multa = 0
    valor_a_pagar_multa = 0
    tiene_multa = False
    def __init__(self, usuario, libro,valor_multa=1,id=0):
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = datetime.now()
        self._fecha_de_reasignacion = None
        self._fecha_devolucion = None
        self._fecha_devolucion_esperada = None
        self._valor_multa = valor_multa
        self._valor_a_pagar_multa = 0
        self._tiene_multa = False
        self._id = id
    def obtener_id(self):
        return self._id
    def __str__(self):
        return f"Prestamo del libro {self._libro} que se entrega {self._fecha_devolucion_esperada.strftime('%Y-%m-%d')}"
    def __repr__(self):
        return f"Prestamo del libro {self._libro} que se entrega {self._fecha_devolucion_esperada.strftime('%Y-%m-%d')}"
    def obtener_usuario(self):
        return self._usuario
    def obtener_libro(self):
        return self._libro
    def establecer_usuario(self, nuevo_usuario):
        self._usuario = nuevo_usuario
    def establecer_libro(self, nuevo_libro):
        self._libro = nuevo_libro
    def obtener_fecha_prestamo(self):
        if isinstance(self._fecha_prestamo,datetime) or self._fecha_prestamo == None:
            return self._fecha_prestamo
        else:
            return datetime.strptime(self._fecha_prestamo, '%Y-%m-%d %H:%M:%S.%f')
    def obtener_fecha_devolucion_real(self):
        if isinstance(self._fecha_devolucion,datetime) or self._fecha_devolucion == None:
            return self._fecha_devolucion
        elif isinstance(self._fecha_devolucion,str):
            return datetime.strptime(self._fecha_devolucion, '%Y-%m-%d %H:%M:%S.%f')
        else:
            return None
    def obtener_valor_multa(self):
        return self._valor_multa
    def obtener_fecha_devolucion_esperada(self):
        if isinstance(self._fecha_devolucion_esperada,datetime) or self._fecha_devolucion_esperada == None:
            return self._fecha_devolucion_esperada
        else:
            return datetime.strptime(self._fecha_devolucion_esperada,'%Y-%m-%d %H:%M:%S.%f')
    def obtener_tiene_multa(self):
        return self._tiene_multa
    def establecer_tiene_multa(self,nuevo_estado):
        if nuevo_estado in (True,False):
            self._tiene_multa = nuevo_estado
        else:
            print("Solo se admite True o False")
    def establecer_valor_a_pagar_multa(self,nuevo_valor):
        self._valor_a_pagar_multa = nuevo_valor
    def establecer_valor_multa(self,nuevo_valor):
        self._valor_multa = nuevo_valor
    def establecer_fecha_prestamo(self, nueva_fecha):
        self._fecha_prestamo = nueva_fecha
    def establecer_fecha_devolucion_esperada(self, nueva_fecha):
        self._fecha_devolucion_esperada = nueva_fecha
    def establecer_fecha_devolucion(self, nueva_fecha):
        self._fecha_devolucion = nueva_fecha
    def establecer_fecha_reagsignacion(self, nueva_fecha):
        self._fecha_de_reasignacion = nueva_fecha
    def obtener_valor_a_pagar_multa(self):
        return self._valor_a_pagar_multa
    def asignar_fecha_devolucion(self):
        numero_dias = random.randint(5,10)
        self._fecha_devolucion_esperada = self.obtener_fecha_prestamo() + timedelta(days=numero_dias)
    def registrar_fecha_reasignacion(self,numero_dias):
        self._fecha_de_reasignacion = self.obtener_fecha_prestamo() + timedelta(days=numero_dias)
    def reasignar_fecha_devolucion(self):
        numero_dias = random.randint(5,10)
        self._fecha_devolucion_esperada = self.obtener_fecha_devolucion_esperada() + timedelta(days=numero_dias)
    def obtener_fecha_reasignacion(self):
        if isinstance(self._fecha_de_reasignacion,datetime) or self._fecha_de_reasignacion == None:
            return self._fecha_de_reasignacion
        else:
            return datetime.strptime(self._fecha_de_reasignacion,'%Y-%m-%d %H:%M:%S.%f')
    def registrar_devolucion(self,numero_dias):
        self._fecha_devolucion = self.obtener_fecha_prestamo() + timedelta(days=numero_dias)
    def prestar_libro(self):
        try:
            if self.obtener_libro().obtener_esta_disponible() == True:
                if self.obtener_usuario().obtener_limite_prestamos() > 0:
                    if self.obtener_usuario().obtener_tiene_multa() == False:
                        self.obtener_usuario().agregar_libro(self.obtener_libro())
                        self.obtener_usuario().establecer_limite_prestamos((self.obtener_usuario().obtener_limite_prestamos() - 1))
                        print(f"El usuario le quedan {self.obtener_usuario().obtener_limite_prestamos()} restantes de prestamos")
                        self.obtener_libro().establecer_estado(False)
                        self.obtener_libro().actualizar_numero_veces_solicitado()
                        self.asignar_fecha_devolucion()
                        print(f"El usuario tendra que devolver el libro en la fecha: {self.obtener_fecha_devolucion_esperada()}")
                        return True
                    else:
                        raise MultaNoPagada("El usuario no ha pagado su multa")
                else:
                    raise LimitePrestamosExcedido()
            else:
                raise LibroNoDisponible()
        except MultaNoPagada as e:
            return (f"Error {e}")
        except LimitePrestamosExcedido as e:
            return (f"Error {e}")
        except LibroNoDisponible as e:
            return (f"Error: {e} ")
        except Exception as e:
            return (f"Error inesperado: {e}")
    
    def cobrar_multa(self, numero_dias_excedido):
        if self._usuario.obtener_tipo() == "estudiante":
            valor_multa = numero_dias_excedido * self._valor_multa
            self._usuario.agregar_horas_sociales_asignadas(valor_multa)
            self._valor_a_pagar_multa = valor_multa
            print(f"Al usuario {self.obtener_usuario()} se le asignaron {valor_multa} horas sociales para pagar su multa")
        elif self._usuario.obtener_tipo() == "docente":
            valor_multa = numero_dias_excedido * self._valor_multa * (1/100)
            if valor_multa >= 1:
                nuevo_salario_docente = 1
            else:
                self._valor_a_pagar_multa = self._usuario.obtener_salario() - (self._usuario.obtener_salario()*valor_multa)
                print(f"Al usuario {self.obtener_usuario()} se le cobrará {valor_multa} pesos para pagar su multa")
    def devolver_libro(self,dias_transcurridos):
        try:
            if self.obtener_libro().obtener_esta_disponible() == False and self.obtener_usuario().obtener_libros_prestados() != []:
                self.obtener_usuario().quitar_libro(self.obtener_libro())
                self.obtener_libro().establecer_estado(True)
                self.obtener_usuario().establecer_limite_prestamos(self.obtener_usuario().obtener_limite_prestamos() + 1)
                tiempo_transcurrido = dias_transcurridos
                print(f"Trancurrieron {tiempo_transcurrido} dias del desde el prestamo")
                self.registrar_devolucion(tiempo_transcurrido)
                if self.obtener_fecha_devolucion_real() > self.obtener_fecha_devolucion_esperada():
                    dias_retardo = int((self.obtener_fecha_devolucion_real() - self.obtener_fecha_devolucion_esperada()).days)
                    print(f"El usuario se atrazo {dias_retardo} dias")
                    print(f"El usuario {self.obtener_usuario()} devolvio tarde el libro ")
                    self.cobrar_multa(dias_retardo)
                    self._usuario.establecer_tiene_multa(True)
                    self.establecer_tiene_multa(True)
                    print(f"El usuario {self._usuario} ha devuelto el libro.")
                else:
                    self.establecer_fecha_devolucion(self.obtener_fecha_devolucion_real())
                    print(f"El usuario {self._usuario} ha devuelto el libro.")
            else:
                raise NoHayLibroParaDevolver("El usuario no tiene libros para devolver")
        except NoHayLibroParaDevolver as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error {e}")
    def extender_prestamo(self,dias_trasncurridos):
        # try:
            print(f"Transcurrieron {dias_trasncurridos} días desde el préstamo o la última reasignación.")
            self.registrar_fecha_reasignacion(dias_trasncurridos)
            if self.obtener_fecha_reasignacion() > self.obtener_fecha_devolucion_esperada():
                dias_retardo = int((self.obtener_fecha_reasignacion() - self.obtener_fecha_devolucion_esperada()).days)
                print(f"El usuario se atrasó {dias_retardo} días.")
                print(f"El usuario {self.obtener_usuario()} devolvió tarde el libro.")
                self.cobrar_multa(dias_retardo)
                self._usuario.establecer_tiene_multa(True)
                self.establecer_tiene_multa(True)
                self.obtener_usuario().quitar_libro(self.obtener_libro())
                self.obtener_libro().establecer_estado(True)
                self.obtener_usuario().establecer_limite_prestamos(self.obtener_usuario().obtener_limite_prestamos() + 1)
                self.establecer_fecha_devolucion(self.obtener_fecha_reasignacion())
                self._tiene_multa = True
                print(f"El usuario {self._usuario} ha devuelto el libro.")
            else:
                self.reasignar_fecha_devolucion()
                print(f"La fecha se reasignó para la siguiente fecha: {self._fecha_devolucion_esperada.strftime('%Y-%m-%d')}")

        # except Exception as e:
        #     print(f"Error inesperado: {e}")
    def pagar_multa_docente(self):
        if isinstance(self._usuario, Docente):
            self.obtener_usuario().establecer_salario(self._valor_a_pagar_multa)
            self._valor_a_pagar_multa = 0
            print(f"El salario actual del usuario {self._usuario} es {self._usuario.obtener_salario()}")
            return f"El docente {self._usuario} ha pagado exitosamente su multa"
    def hacer_horas_sociales_estudiante(self):
        if isinstance(self._usuario,Estudiante):
            if self._usuario.obtener_horas_sociales_asignadas() <= 0:
                self._usuario.establecer_horas_sociales_asignadas(0)
            else:
                self._usuario.agregar_horas_sociales_asignadas(-1*self._valor_a_pagar_multa)
            self._tiene_multa = False
            
    # Método para mostrar información del préstamo
    def mostrar_informacion(self):
        print(f"Usuario: {self._usuario.obtener_nombre()} de tipo {self._usuario.obtener_tipo()}")
        print(f"Libro: {self._libro.obtener_titulo()}")
        print(f"Fecha de Préstamo: {self._fecha_prestamo.strftime('%Y-%m-%d')}")
        print(f"Fecha devolución asignada: {self._fecha_devolucion_esperada.strftime('%Y-%m-%d')}")
        if self._fecha_devolucion:
            print(f"Fecha de Devolución: {self._fecha_devolucion.strftime('%Y-%m-%d')}")
        else:
            print("Aún no ha sido devuelto.")

