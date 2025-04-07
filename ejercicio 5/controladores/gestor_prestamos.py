class GestorPrestamos:
    prestamos = []
    historico_prestmos = []
    def __init__(self,base_datos_proxy):
        self.base_datos_proxy = base_datos_proxy
        self._prestamos = self.base_datos_proxy.obtener_prestamos()
        self._historico_prestamos = self._prestamos.copy()
    def agregar_prestamo(self,prestamo):
        self.base_datos_proxy.registrar_prestamo(prestamo)
    def actualizar_prestamo(self,prestamo):
        self.base_datos_proxy.actualizar_datos_prestamo(prestamo)
    def filtrar_prestamos_por_usuario(self,usuario):
        prestamos_asociados_al_usuario = [
            prestamo for prestamo in self._prestamos 
            if prestamo.obtener_usuario().obtener_id() == usuario.obtener_id() and 
            prestamo.obtener_usuario().obtener_identificacion() == usuario.obtener_identificacion()
            and prestamo.obtener_tiene_multa() == False and prestamo.obtener_fecha_devolucion_real() == None
        ]
        return prestamos_asociados_al_usuario
    def filtrar_prestamos_por_usuario_con_multa(self,usuario):
        prestamos_asociados_al_usuario = [prestamo for prestamo in self._prestamos 
            if prestamo.obtener_usuario().obtener_id() == usuario.obtener_id() and prestamo.obtener_usuario().obtener_identificacion() == usuario.obtener_identificacion() and prestamo.obtener_tiene_multa() == True]
        return prestamos_asociados_al_usuario
    def filtrar_libro_prestamos_por_usuario_sin_multa(self,usuario):
        prestamos_asociados_al_usuario = [prestamo for prestamo in self._prestamos if prestamo.obtener_usuario() == usuario and prestamo.obtener_tiene_multa() == False]
        return prestamos_asociados_al_usuario
    def quitar_prestamo(self,prestamo):
        self._prestamos.remove(prestamo)
    def listar_prestamos_activos(self):
        return [f"{prestamo.obtener_libro().obtener_titulo()} a {prestamo.obtener_usuario().obtener_nombre()}" 
                for prestamo in self._prestamos]
    def listar_prestamos_activos_detallado(self):
        return self._prestamos
    def listar_historico_prestamos(self):
        return [f"{prestamo.obtener_libro().obtener_titulo()} a {prestamo.obtener_usuario().obtener_nombre()}" 
                for prestamo in self._historico_prestamos]
    def listar_historico_prestamos_detallado(self):
        return self._historico_prestamos
    def marcar_prestamo_con_multa(self, prestamo):
        for i, p in enumerate(self._prestamos):
            if p == prestamo:  # O mejor: if p is prestamo, si es la misma instancia
                self._prestamos[i].establecer_tiene_multa(True)
                return True
        return False

