from Persistent import *

class Auditoria(Persistent):
    def __init__(self,id_auditoria,nombre,valor_anterior,valor_actual,fecha_modificacion,id_empleado,id_cliente) -> None:
        super().__init__()
        self._id_auditoria=id_auditoria
        self._nombre=nombre
        self._valor_anterior=valor_anterior
        self._valor_actual=valor_actual
        self._fecha_modificacion=fecha_modificacion
        self._id_empleado=id_empleado
        self._id_cliente=id_cliente
    
    def set_id_auditoria(self,id_auditoria):
        self._id_auditoria=id_auditoria
    def get_id_auditoria(self):
        return self._id_auditoria

    def set_nombre(self,nombre):
        self._nombre=nombre
    def get_nombre(self):
        return self._nombre

    def set_valor_anterior(self,valor_anterior):
        self._valor_anterior=valor_anterior
    def get_valor_anterior(self):
        return self._valor_anterior

    def set_valor_actual(self,valor_actual):
        self._valor_actual=valor_actual
    def get_valor_actual(self):
        return self._valor_actual

    def set_fecha_modificacion(self,fecha_modificacion):
        self._fecha_modificacion=fecha_modificacion
    def get_fecha_modificacion(self):
        return self._fecha_modificacion

    def set_id_empleado(self,id_empleado):
        self._id_empleado=id_empleado
    def get_id_empleado(self):
        return self._id_empleado

    def set_id_cliente(self,id_cliente):
        self._id_cliente=id_cliente
    def get_id_cliente(self):
        return self._id_cliente

class Log(Persistent):
    def __init__(self, id_log,tipo_log,mensaje,fecha_incidencia) -> None:
        super().__init__()
        self._id_log=id_log
        self._tipo_log=tipo_log
        self._mensaje=mensaje
        self._fecha_incidencia=fecha_incidencia
    
    def set_id_log(self,id_log):
        self._id_log=id_log
    def get_id_log(self):
        return self.id_log
    
    def set__tipo_log(self,tipo_log):
        self._tipo_log=tipo_log
    def get_tipo_log(self):
        return self._tipo_log
    
    def set_mensaje(self,mensaje):
        self._mensaje=mensaje
    def get_mensaje(self):
        return self._mensaje
    
    def set_fecha_incidencia(self,fecha_incidencia):
        self._fecha_incidencia=fecha_incidencia
    def get_fecha_incidencia(self):
        return self._fecha_incidencia
