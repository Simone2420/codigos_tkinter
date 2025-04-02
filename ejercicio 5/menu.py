from modelos import *
from controladores import *
from utilidades import *
from biblioteca_facade import *
import os
import sys
import time
def decorador_menu(func):
    def envoltorio(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                pass
    return envoltorio()
class Menu:
    gestor_usuarios = None   
    gestor_prestamos = None
    gestor_libros  = None   
    def __init__(self):
        self.bibliotecario = None
        self._gestor_usuarios = GestorUsuarios(BaseDatosEstudiantes().obtener_estudiantes(),BaseDatosDocentes().obtener_docentes())
        self._gestor_libros = GestorLibros(BaseDatosLibros().obtener_libros())
        self._gestor_prestamos = GestorPrestamos()
    def menu_consultar_libros(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu consultar libros",Color.AZUL,None,True))
                print(f"1.) Consultar libros por categorias.")
                print(f"2.) Consultar todos los libros.")
                opcion = int(input("Ingrese su opcion: "))
                match opcion:
                    case 1:
                        categorias_disponibles = ["Literatura", "Novela", "Realismo", "Ciencia Ficción"]
                        mostrar_lista_opciones(categorias_disponibles, "categorias disponibles")
                        selecion_categoria = int(input("Ingrese su opcion: "))
                        if 1 <= selecion_categoria <= len(categorias_disponibles):
                            categoria_elegida = categorias_disponibles[selecion_categoria-1]
                            libros_categoria_elegida = self._gestor_libros.mostrar_libros_por_categoria(categoria_elegida)
                            if libros_categoria_elegida == False:
                                print("No fue posible encontrar algun libro con esa categoria")
                                input("Presione enter para continuar")
                                continue
                            mostrar_lista_opciones(libros_categoria_elegida,f"Libros filtados de la categoria {categoria_elegida}")
                            seleccion_libro = int(input("De cual libro desea obtener informacion: "))
                            libros_categoria_elegida[seleccion_libro - 1].mostrar_informacion()
                            confirmacion_salida = input("Desea ver información de otro libro(si/no): ")
                            if confirmacion_salida.lower() == "si":
                                continue
                            elif confirmacion_salida.lower() == "no":
                                input("Presione enter para continuar")
                                break
                            else:
                                print("Escriba si o no")
                        else:
                            raise OpcionInvalida("La opcion no es valida")
                    case 2:
                        mostrar_lista_opciones(self._gestor_libros.obtener_libros(),"Libros")
                        opcion = int(input("De cual libro desea obtener mas información: "))
                        indice_libro_seleccionado = opcion - 1
                        self._gestor_libros.mostrar_todos_los_libros()[indice_libro_seleccionado].mostrar_informacion()
                        confirmacion_salida = input("Desea ver información de otro libro(si/no): ")
                        if confirmacion_salida.lower() == "si":
                            continue
                        elif confirmacion_salida.lower() == "no":
                            input("Presione enter para continuar")
                            break
                        else:
                            print("Escriba si o no")
            except (ValueError,OpcionInvalida) as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                continue
    def menu_registrar_libros(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu registro libros",Color.AZUL,None,True))
                print("1.) Categoria Literatura")
                print("2.) Categoria Novela")
                print("3.) Categoria Realismo")
                print("4.) Categoria Ciencia Ficción")
                opcion = int(input("Seleccione una opción: "))
                lista_categorias = ["Literatura","Novela","Realismo","Ciencia Ficción"]
                if opcion == 5:
                    self.menu_gestion_libros()
                elif opcion < 1 or opcion > 5:
                    raise OpcionInvalida("Opcion invalida")
                try:
                    titulo_libro = input("Ingrese el título del libro: ")
                    nombre_autor = input("Ingrese nombre del autor: ")
                    if not solo_letras_y_espacios(nombre_autor):
                        raise DatosInvalidos("Nombre inválido.")
                    ano_publicacion = int(input("Ingrese el año de publicacion del libro: "))
                    libro = Libro(titulo_libro,nombre_autor,ano_publicacion,lista_categorias[opcion-1])
                    self._gestor_libros.registrar_nuevo_libro(libro)
                    print(mensaje_con_estilo("Libro regitrado exitosamente",Color.VERDE,None,True))                            
                    confirmacion_salir = input("Desea registrar otro libro (si/no): ")
                    if confirmacion_salir.lower() == "si":
                        continue
                    elif confirmacion_salir.lower() == "no":
                        input("Presione enter para continuar")
                        self.menu_gestion_libros()
                    else:
                        print("Escriba si o no")
                except ValueError as e:
                        print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                        input("Presione enter para continuar")
                        self.menu_gestion_libros()
                except DatosInvalidos as e:
                        print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                        print("Volviendo al menu de registro...")
                        self.menu_gestion_libros()
                except Exception as e:
                        print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                        input("Presione enter para continuar")
                        self.menu_gestion_libros()
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
            except (ValueError, TypeError) as e:
                print(mensaje_con_estilo(f"Error {e}",Color.ROJO,None,True))
                input("Presione enter para volver: ")
                self.menu_gestion_libros()
            except Exception as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
    def menu_libros_mas_solicitados(self): 
        libros_mas_solicitados = self._gestor_libros.libros_mas_solicitados(5)
        for libro, veces_solicitado in libros_mas_solicitados:
            print(f"{libro} - Solicitado {veces_solicitado} veces")
        input("Presione enter para continuar...")
        self.menu_gestion_libros()
    def menu_consulta_usuarios(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu consulta usuarios",Color.AZUL,None,True))
                print("1.) Consultar docentes")
                print("2.) Consultar estudiantes")
                print("3.) Consultar todos los usuarios")
                print("4.) Volver al anterior menu")
                opcion = int(input("Selecione una opción: "))
                match opcion:
                    case 1:
                        self._gestor_usuarios.listar_docentes()
                        input("Presione enter para continuar")
                        continue
                    case 2:
                        self._gestor_usuarios.listar_estudiantes()
                        input("Presione enter para continuar")
                        continue
                    case 3:
                        while True:
                            try:
                                mostrar_lista_opciones(self._gestor_usuarios.listar_usuarios(),"Usuarios")
                                opcion = int(input("De cual usuario desea obtener mas información: "))
                                indice_usuario_seleccionado = opcion - 1
                                self._gestor_usuarios.obtener_usuarios()[indice_usuario_seleccionado].mostrar_informacion()
                                confirmacion_salida = input("Desea ver información de otro usuario(si/no): ")
                                if confirmacion_salida.lower() == "si":
                                    continue
                                elif confirmacion_salida.lower() == "no":
                                    input("Presione enter para continuar")
                                    self.menu_consulta_usuarios()
                                else:
                                    print("Escriba si o no")
                            except ValueError as e:
                                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                                input("Presione enter para continuar")
                                self.menu_consulta_usuarios()
                            except Exception as e:
                                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                                input("Presione enter para continuar")
                                self.menu_consulta_usuarios()
                        continue
                    case 4:
                        self.menu_gestion_usuarios()
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_registro_usuario(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu registro usuarios",Color.AZUL,None,True))
                print("1.) Registrar docente")
                print("2.) Registrar estudiante")
                print("3.) Volver al menu anterior")
                opcion = int(input("Seleccione una opción: "))
                match opcion:
                    case 1:
                        try:
                            nombre_docente = input("Ingrese el nombre del docente: ")
                            if not solo_letras_y_espacios(nombre_docente):
                                raise DatosInvalidos("Nombre inválido.")
                            identificacion_docente = int(input("Ingrese la identificación del docente: "))
                            horario_docente = input("Ingrese el horario del docente (diurno/nocturno/mixto): ")
                            if horario_docente.lower() not in ("diurno","nocturno","mixto"):
                                raise DatosInvalidos("Solo se admite horario: diurno, nocturno o mixto")
                            id_profesional_docente = input("Ingrese su id_profesional en el siguiente formato (P#####): ")
                            if len(id_profesional_docente) != 6:  # Verificar longitud
                                raise DatosInvalidos("El ID profesional debe tener exactamente 6 caracteres.")
                            if id_profesional_docente[0].upper() != 'P':  # Verificar prefijo
                                raise DatosInvalidos("El ID profesional debe comenzar con la letra 'P'.")
                            if not id_profesional_docente[1:].isdigit():  # Verificar dígitos
                                raise DatosInvalidos("Los últimos 5 caracteres deben ser dígitos numéricos.")
                            docente = Docente(nombre_docente,identificacion_docente,1000000,horario_docente,"Enseñar",id_profesional_docente)
                            docente_validar_datos = docente.validar_datos()
                            if docente_validar_datos == True:
                                validacion_final = self._gestor_usuarios.registrar_usuario_nuevo(docente)
                                if validacion_final == False:
                                    raise IdentificacionRepetida("La identificacion ingresada ya la tiene registrada un usuario del sistema)")
                                else:
                                    print(mensaje_con_estilo(validacion_final,Color.VERDE,None,True))
                                    confirmacion_salir = input("Desea registrar otro usuario (si/no): ")
                                    if confirmacion_salir.lower() == "si":
                                        continue
                                    elif confirmacion_salir.lower() == "no":
                                        input("Presione enter para continuar")
                                        self.menu_gestion_usuarios()
                                    else:
                                        print("Escriba si o no")
                            else:
                                raise DatosInvalidos("Los datos no son correctos intente de nuevo")
                        except IdentificacionRepetida as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                        except (DatosInvalidos,ValueError) as e:
                                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                                input("Presione enter para continuar")
                                self.menu_gestion_usuarios()   
                        except Exception as e:
                                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                                input("Presione enter para continuar")
                                self.menu_gestion_usuarios()
                    case 2:
                        try:
                            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
                            if not solo_letras_y_espacios(nombre_estudiante):
                                raise DatosInvalidos("Nombre inválido.")
                            identificacion_estudiante = int(input("Ingrese la identificación del estudiante: "))
                            numero_matricula_estudiante = input("Ingrese su numero de matricula en el siguiente formato (M#####): ")
                            if len(numero_matricula_estudiante) != 6:  # Verificar longitud
                                raise DatosInvalidos("El ID profesional debe tener exactamente 6 caracteres.")
                            if numero_matricula_estudiante[0].upper() != 'M':  # Verificar prefijo
                                raise DatosInvalidos("El Número de matrícula debe comenzar con la letra 'M'.")
                            if not numero_matricula_estudiante[1:].isdigit():  # Verificar dígitos
                                raise DatosInvalidos("Los últimos 5 caracteres deben ser dígitos numéricos.")
                            estudiante = Estudiante(nombre_estudiante,identificacion_estudiante,numero_matricula_estudiante)
                            estudiante_validar_datos = estudiante.validar_datos()
                            if estudiante_validar_datos == True:
                                validacion_final = self._gestor_usuarios.registrar_usuario_nuevo(estudiante)
                                if validacion_final == False:
                                    raise IdentificacionRepetida("La identificacion ingresada ya la tiene registrada un usuario del sistema)")
                                else:
                                    print(mensaje_con_estilo(validacion_final,Color.VERDE,None,True))
                                    confirmacion_salir = input("Desea registrar otro usuario (si/no): ")
                                    if confirmacion_salir.lower() == "si":
                                        continue
                                    elif confirmacion_salir.lower() == "no":
                                        input("Presione enter para continuar")
                                        self.menu_gestion_usuarios()
                                    else:
                                        print("Escriba si o no")
                            else:
                                raise DatosInvalidos("Los datos no son correctos intente de nuevo")
                        except (IdentificacionRepetida,DatosInvalidos,ValueError) as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                        except Exception as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            self.menu_gestion_usuarios()
                    case 3:
                        self.menu_gestion_usuarios()
                    case _:
                        print("Opcion invalida.")
            except (ValueError, TypeError) as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
                break
            except Exception as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
    def menu_prestar_libro(self,usuario):
        while True:
            try:
                limpiar_consola()
                mostrar_lista_opciones(self._gestor_libros.mostrar_libros_disponibles(),"Libros")
                opcion = int(input("De cual libro desea solicitar en prestamo: "))
                indice_libro_seleccionado = opcion - 1
                libro_solicitado = self._gestor_libros.obtener_libros_disponibles()[indice_libro_seleccionado]
                verificar_prestamo = input("Estas seguro de pedir prestado el libro (si/no)?: ")
                if verificar_prestamo.lower() == "si":
                    if usuario.obtener_limite_prestamos() > 0: 
                        prestamo = Prestamo(usuario,libro_solicitado)
                        validar_prestamo = prestamo.prestar_libro()
                        if validar_prestamo == True:
                            self._gestor_libros.quitar_libro(indice_libro_seleccionado)
                            print(mensaje_con_estilo("Prestamo exitoso",Color.VERDE,None,True))
                            self._gestor_prestamos.agregar_prestamo(prestamo)
                        else:
                            print(mensaje_con_estilo(validar_prestamo,Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            break
                    else:
                        raise LimitePrestamosExcedido("El usuario ha excedido su limite de prestamos")
                elif verificar_prestamo.lower() == "no":
                    input("Presione enter para continuar")
                    break
                else:
                    print("Escriba si o no")
                
                confirmacion_salida = input("Desea solicitar otro libro en prestamo (si/no): ")
                if confirmacion_salida.lower() == "si":
                    continue
                elif confirmacion_salida.lower() == "no":
                    input("Presione enter para continuar")
                    break
                else:
                    print("Escriba si o no")
            except (ValueError,LimitePrestamosExcedido) as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break
    def devolver_libros(self,usuario):
        while True:
            try:
                limpiar_consola()
                prestamos = self._gestor_prestamos.filtrar_libro_prestamos_por_usuario_sin_multa(usuario)
                for prestamo in prestamos:
                    print(f"Préstamo: {prestamo}, multa: {prestamo.obtener_tiene_multa()}")
                print(mensaje_con_estilo("Menu devolver libros",Color.AZUL,None,True))
                libros_prestados_al_usuario = self._gestor_prestamos.filtrar_libro_prestamos_por_usuario_sin_multa(usuario)
                mostrar_lista_opciones(libros_prestados_al_usuario,"Prestamos al usuario")
                opcion = int(input("Seleccione una opcion: "))
                indice_prestamo = opcion - 1
                prestamo_selecionado = libros_prestados_al_usuario[indice_prestamo]
                print("Que desea hacer?")
                print("1.) Extender prestamo")
                print("2.) Devolver libro")
                opcion_submenu = int(input("Seleccione una opcion: "))
                match opcion_submenu:
                    case 1:
                        validacion_final = prestamo_selecionado.extender_prestamo()
                        if validacion_final == False:
                            print(mensaje_con_estilo("Tendra que pagar la multa para solicitar un libro prestado", Color.ROJO))
                            self._gestor_prestamos.marcar_prestamo_con_multa(prestamo_selecionado)
                            self._gestor_libros.agregar_libro(prestamo_selecionado.obtener_libro())
                            input("Presione enter para continuar... ")
                            break  
                        else:
                            print(mensaje_con_estilo(validacion_final, Color.VERDE, None, True))
                            input("Presione enter para continuar... ")
                            continue
                    case 2:
                        validacion_final = prestamo_selecionado.devolver_libro()
                        if validacion_final == "El usuario devolvio su libro exitosamente":
                            print(mensaje_con_estilo(validacion_final, Color.VERDE, None, True))
                            self._gestor_prestamos.quitar_prestamo(prestamo_selecionado)
                            self._gestor_libros.agregar_libro(prestamo_selecionado.obtener_libro())
                            input("Presione enter para continuar... ")
                            continue
                        elif validacion_final == False:
                            print(mensaje_con_estilo("El usuario devolvio tarde el libro", Color.ROJO, None, True))
                            self._gestor_prestamos.marcar_prestamo_con_multa(prestamo_selecionado)
                            self._gestor_libros.agregar_libro(prestamo_selecionado.obtener_libro())
                            input("Presione enter para continuar... ")
                            continue
                        else:
                            print(mensaje_con_estilo(validacion_final, Color.ROJO, None, True))
                            input("Presione enter para continuar... ")
                            continue
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break
            except Exception as e:
                print(mensaje_con_estilo(f"Error {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break
    def ver_estadisticas(self,usuario):
        usuario.mostrar_informacion()
        input("Presione enter para continuar")
        if isinstance(usuario, Docente):
            self.menu_docente(usuario)
        else:
            self.menu_estudiante(usuario)
    def menu_pagar_multa(self,usuario):
        while True:
            try:
                if usuario.obtener_tiene_multa() == True:
                    print(mensaje_con_estilo("Pagar multa",Color.AZUL,None,True))
                    libros_prestados_al_usuario = self._gestor_prestamos.filtrar_prestamos_por_usuario_con_multa(usuario)
                    mostrar_lista_opciones(libros_prestados_al_usuario,"Prestamos al usuario con multas pendientes")
                    opcion = int(input("Seleccione una opcion: "))
                    indice_prestamo = opcion - 1
                    if opcion > len(libros_prestados_al_usuario):
                        raise OpcionInvalida("Opcion invalida")
                    prestamo_selecionado = libros_prestados_al_usuario[indice_prestamo]
                    mensaje = prestamo_selecionado.pagar_multa_docente()
                    print(mensaje_con_estilo(mensaje,Color.VERDE,None,True))
                    self._gestor_prestamos.quitar_prestamo(prestamo_selecionado)
                    libros_prestados_al_usuario.pop(indice_prestamo)
                    if len(libros_prestados_al_usuario) != 0:
                        continue
                    else:
                        print(mensaje_con_estilo("El usuario ha pagado todas sus multas",Color.VERDE))
                        input("Presione enter para continuar... ")
                        usuario.establecer_tiene_multa(False)
                        break
                else:
                    print(mensaje_con_estilo("El usuario no tiene multas",Color.VERDE))
                    usuario.establecer_tiene_multa(False)
                    break
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break
            except Exception as e:
                print(mensaje_con_estilo(f"Error {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                break

    def menu_hacer_horas_sociales(self,usuario): 
        while True:
            if usuario.obtener_tiene_multa() == True:
                print(mensaje_con_estilo("Hacer horas sociales",Color.AZUL,None,True))
                libros_prestados_al_usuario = self._gestor_prestamos.filtrar_prestamos_por_usuario_con_multa(usuario)
                mostrar_lista_opciones(libros_prestados_al_usuario,"Prestamos al usuario con multas pendientes")
                opcion = int(input("Seleccione una opcion: "))
                indice_prestamo = opcion - 1
                prestamo_selecionado = libros_prestados_al_usuario[indice_prestamo]
                mensaje = prestamo_selecionado.hacer_horas_sociales_estudiante()
                print(mensaje_con_estilo(mensaje,Color.VERDE,None,True))
                self._gestor_prestamos.quitar_prestamo(prestamo_selecionado)
                libros_prestados_al_usuario.pop(indice_prestamo)
                if libros_prestados_al_usuario != []:
                    continue
                else:
                    print(mensaje_con_estilo("El usuario ha pagado su multas",Color.VERDE))
                    usuario.establecer_tiene_multa(False)
                    input("Presione enter para continuar... ")
                    continue
            else:
                print(mensaje_con_estilo("El usuario no tiene multas",Color.VERDE))
                usuario.establecer_tiene_multa(False)
                break
    def menu_docente(self,docente):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu bienvenido docente {docente}",Color.AZUL,None,True))
                print("1.) Ver libros disponibles.")
                print("2.) Solicitar prestamo libro.")
                print("3.) Devolver libro.")
                print("4.) Pagar multa.")
                print("5.) Ver estadísticas.")
                print("6.) Cerrar sesión.")
                opcion = int(input("Ingrese su opción: "))
                match opcion:
                    case 1:
                        self.menu_consultar_libros()
                    case 2:
                        self.menu_prestar_libro(docente)
                    case 3:
                        self.devolver_libros(docente)
                    case 4:
                        self.menu_pagar_multa(docente)
                    case 5:
                        self.ver_estadisticas(docente)
                    case 6:
                        self.menu_gestion_usuarios()
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_estudiante(self,estudiante):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu bienvenido estudiante {estudiante}",Color.AZUL,None,True))
                print("1.) Ver libros disponibles.")
                print("2.) Solicitar prestamo libro.")
                print("3.) Devolver libro.")
                print("4.) Hacer horas sociales.")
                print("5.) Ver estadísticas.")
                print("6.) Cerrar sesión.")
                opcion = int(input("Ingrese su opción: "))
                match opcion:
                    case 1:
                        self.menu_consultar_libros()
                    case 2:
                        self.menu_prestar_libro(estudiante)
                    case 3:
                        self.devolver_libros(estudiante)
                    case 4:
                        self.menu_hacer_horas_sociales(estudiante)
                    case 5:
                        self.ver_estadisticas(estudiante)
                    case 6:
                        self.menu_gestion_usuarios()
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_ingresar_usuario(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu ingreso usuario",Color.AZUL,None,True))
                print("1.) Ingresar docente")
                print("2.) Ingresar estudiante")
                print("3.) Volver al menu anterior")
                opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
                match opcion:
                    case 1:
                        try:
                            docente_identificacion_validar = int(input("Ingrese el número de su identificación: "))
                            docente_id_profesional_validar = input("Ingrese el número de id profesional del docente (P#####): ")
                            if len(docente_id_profesional_validar) != 6:  # Verificar longitud
                                raise DatosInvalidos("El ID profesional debe tener exactamente 6 caracteres.")
                            if docente_id_profesional_validar[0].upper() != 'P':  # Verificar prefijo
                                raise DatosInvalidos("El ID profesional debe comenzar con la letra 'P'.")
                            if not docente_id_profesional_validar[1:].isdigit():  # Verificar dígitos
                                raise DatosInvalidos("Los últimos 5 caracteres deben ser dígitos numéricos.")
                            docente_encontrado = self._gestor_usuarios.ingresar_docente(docente_identificacion_validar,docente_id_profesional_validar)
                            if docente_encontrado:
                                print(mensaje_con_estilo(f"Bienvenido, {docente_encontrado.obtener_nombre()}.",Color.VERDE,None,True))
                                input("Presione enter para continuar...")
                                self.menu_docente(docente_encontrado)
                            else:
                                raise UsuarioNoEncontrado("El usuario no pudo ser encontrado")
                            print(f"Bienvenido, {docente_encontrado.obtener_nombre()}.")
                        except (DatosInvalidos,UsuarioNoEncontrado,ValueError) as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                        except Exception:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                    case 2:    
                        try:
                            estudiante_identificacion_validar = int(input("Ingrese el número de su identificación: "))
                            estudiante_matricula_validar = input("Ingrese el numero de matricula del estudiante (M#####): ")
                            if len(estudiante_matricula_validar) != 6:  # Verificar longitud
                                raise DatosInvalidos("El ID profesional debe tener exactamente 6 caracteres.")
                            if estudiante_matricula_validar[0].upper() != 'M':  # Verificar prefijo
                                raise DatosInvalidos("El Número de matrícula debe comenzar con la letra 'M'.")
                            if not estudiante_matricula_validar[1:].isdigit():  # Verificar dígitos
                                raise DatosInvalidos("Los últimos 5 caracteres deben ser dígitos numéricos.")
                            estudiante_encontrado = self._gestor_usuarios.ingresar_estudiante(estudiante_identificacion_validar,estudiante_matricula_validar)
                            if estudiante_encontrado:
                                print(mensaje_con_estilo(f"Bienvenido, {estudiante_encontrado.obtener_nombre()}.",Color.VERDE,None,True))
                                input("Presione enter para continuar...")
                                self.menu_estudiante(estudiante_encontrado)
                            else:
                                raise UsuarioNoEncontrado("El usuario no pudo ser encontrado")
                        except (DatosInvalidos,UsuarioNoEncontrado,ValueError) as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                        except Exception as e:
                            print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                            input("Presione enter para continuar")
                            continue
                    case 3:
                        self.menu_gestion_usuarios()
                    case _:
                        raise OpcionInvalida("Opción inválida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Error: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_gestion_usuarios(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo("Menu gestor usuarios",Color.AZUL,None,True))
                print("1.) Consultar usuarios registrados")
                print("2.) Registrar nuevo usuario")
                print("3.) Ingresar usuario")
                print("4.) Volver al anterior menu")
                opcion = int(input("Selecione una opción: "))
                match opcion:
                    case 1:
                        self.menu_consulta_usuarios()
                    case 2:
                        self.menu_registro_usuario()
                    case 3:
                        self.menu_ingresar_usuario()
                    case 4:
                        self.menu_principal()
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_gestion_libros(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu Gestion Libros",Color.AZUL,None,True))
                print("1.) Consultar libros disponibles")
                print("2.) Registar nuevo libro")
                print("3.) Estadisticas libros mas solicitados")
                print("4.) Volver al anterior menu")
                opcion = int(input("Selecione una opción: "))
                match opcion:
                    case 1:
                        self.menu_consultar_libros()
                    case 2:
                        self.menu_registrar_libros()
                    case 3:
                        self.menu_libros_mas_solicitados()
                    case 4:
                        self.menu_principal()
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Advertencia: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_prestamos_activos(self): 
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu consulta prestamos activos",Color.AZUL,None,True))
                prestamos_historicos = self._gestor_prestamos.listar_prestamos_activos()
                mostrar_lista_opciones(prestamos_historicos, "Prestamos activos")
                opcion = int(input("Escriba su opcion"))
                if opcion > len(prestamos_historicos) or opcion < 1:
                    raise OpcionInvalida("Opcion invalida")
                indice_prestamo = opcion - 1
                prestamos_a_selecionar = self._gestor_prestamos.listar_prestamos_activos_detallado()
                prestamo_selecionado = prestamos_a_selecionar[indice_prestamo]
                prestamo_selecionado.mostrar_informacion()
                confirmacion_salir = input("Desea ver informacion de otro prestamo (si/no): ")
                if confirmacion_salir.lower() == "si":
                    continue
                elif confirmacion_salir.lower() == "no":
                    input("Presione enter para continuar")
                    self.menu_gestion_prestamos()
                else:
                    print("Escriba si o no")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Error: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                self.menu_gestion_prestamos()
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                self.menu_gestion_prestamos()
    def menu_prestamos_historico(self): 
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu consulta historico prestamos",Color.AZUL,None,True))
                prestamos_historicos = self._gestor_prestamos.listar_historico_prestamos()
                mostrar_lista_opciones(prestamos_historicos, "Todos los prestamos")
                opcion = int(input("Escriba su opcion: "))
                if opcion > len(prestamos_historicos) or opcion < 1:
                    raise OpcionInvalida("Opcion invalida")
                indice_prestamo = opcion - 1
                prestamos_a_selecionar = self._gestor_prestamos.listar_historico_prestamos_detallado()
                prestamo_selecionado = prestamos_a_selecionar[indice_prestamo]
                prestamo_selecionado.mostrar_informacion()
                confirmacion_salir = input("Desea ver informacion de otro prestamo (si/no): ")
                if confirmacion_salir.lower() == "si":
                    continue
                elif confirmacion_salir.lower() == "no":
                    input("Presione enter para continuar")
                    self.menu_gestion_prestamos()
                else:
                    print("Escriba si o no")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Error: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                self.menu_gestion_prestamos()
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                self.menu_gestion_prestamos()
    def menu_gestion_prestamos(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Menu Gestion Prestamos",Color.AZUL,None,True))
                print("1.) Consultar prestamos activos")
                print("2.) Consultar historial de prestamos")
                print("3.) Volver al anterior menu")
                opcion = int(input("Selecione una opción: "))
                match opcion:
                    case 1:
                        self.menu_prestamos_activos()
                    case 2:
                        self.menu_prestamos_historico()
                    case 3:
                        self.menu_principal()
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Error: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
    def menu_principal(self):
        while True:
            try:
                limpiar_consola()
                print(mensaje_con_estilo(f"Bienvenido bibliotecario {self.bibliotecario} de la Universidad de Cundinamarca",Color.AZUL,None,True))
                print("1.) Gestionar usuarios")
                print("2.) Gestionar prestamos")
                print("3.) Gestionar libros")
                print("4.) Salir del programa")
                opcion = int(input("Selecione una opción: "))
                match opcion:
                    case 1:
                        self.menu_gestion_usuarios()
                    case 2:
                        self.menu_gestion_prestamos()
                    case 3:
                        self.menu_gestion_libros()
                    case 4:
                        sys.exit()
                    case _:
                        raise OpcionInvalida("Opcion invalida")
            except OpcionInvalida as w:
                print(mensaje_con_estilo(f"Error: {w}",Color.AMARILLO,None,True))
                input("Presione enter para continuar")
                continue
            except ValueError as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
                input("Presione enter para continuar")
                continue
            
    def menu_inicial(self):
        while True:
            print("Bienvenido Bibliotecario")
            try:
                nombre_bibliotecario = input("Ingrese su nombre por favor: ")
                if not solo_letras_y_espacios(nombre_bibliotecario):
                    raise DatosInvalidos("El nombre debe solo tener letras y espacios")
                identificacion_bibliotecario = int(input("Ingrese su identificación (solo numeros): "))
                self.bibliotecario = EmpleadoBiblioteca(nombre_bibliotecario, identificacion_bibliotecario,1000000,"Diurno","Supervisar")
                self.menu_principal()
            except (ValueError,DatosInvalidos) as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
            except Exception as e:
                print(mensaje_con_estilo(f"Error: {e}",Color.ROJO,None,True))
if __name__ == "__main__":
    menu =  Menu()
    menu.menu_inicial()

