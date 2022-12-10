from abc import abstractclassmethod
from usuario import Usuario
from datetime import date
from Conexion import conexion
from Factory import *

conn = conexion
class UsuarioDeco(Usuario):
    @abstractclassmethod
    def __init__(self) -> None:
        super().__init__()



class Cliente(UsuarioDeco):
    def __init__(self,usuario: Usuario, ruc, numFamiliares, pasatiempo, numDispositivos, nivelSocioeconomico, tiempoServicio) -> None:
        self._usuario = usuario
        self._ruc = ruc
        self._numFamiliares = numFamiliares
        self._pasatiempo= pasatiempo
        self._numDispositivos = numDispositivos
        self._nivelSocioeconomico = nivelSocioeconomico
        self._tiempoServicio = tiempoServicio
       
       
    def set_ruc(self, valor_ruc: str) -> None:
        self._ruc=valor_ruc
    def get_ruc(self) -> str:
        return self._ruc
        
    def set_numero_familiares(self, valor_numFamiliares: str) -> None:
        self._numFamiliares=valor_numFamiliares
    def get_numero_familiares(self) -> str:
        return self._numFamiliares
        
    def set_pasatiempo(self, valor_pasatiempo: str) -> None:
        self._pasatiempo=valor_pasatiempo
    def get_pasatiempo(self) -> str:
        return self._pasatiempo
        
    def set_numero_dispositivos(self, valor_numDispositivos: str) -> None:
        self._numDispositivos=valor_numDispositivos
    def get_numero_dispositivos(self) -> str:
        return self._numDispositivos
        
    def set_nivel_socieconomico(self, valor_nivelSocioeconomico: str) -> None:
        self._nivelSocioeconomico=valor_nivelSocioeconomico
    def get_nivel_socieconomico(self) -> str:
        return self._nivelSocioeconomico
        
    def set_tiempo_servicio(self, valor_tiempoServicio: str) -> None:
        self._tiempoServicio=valor_tiempoServicio
    def get_tiempo_servicio(self) -> str:
        return self._tiempoServicio

     #Ingresa una tupla nueva en la tabla de clientes
    


class Empleado(UsuarioDeco):
    def __init__(self,usuario: Usuario,  sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        self._usuario = usuario
        self._sueldo = sueldo
        self._rango = rango
        self._tiempoContratacion = tiempoContratacion
        self._FechaContratación = FechaContratación
        
    def set_sueldo(self, valor_sueldo: str) -> None:
        self._sueldo=valor_sueldo
    def get_sueldo(self) -> str:
        return self._sueldo
                
    def set_rango(self, valor_rango: str) -> None:
        self._rango=valor_rango
    def get_rango(self) -> str:
        return self._rango
        
    def set_tiempo_contratacion(self, valor_tiempoContratacion: str) -> None:
        self._tiempoContratacion=valor_tiempoContratacion
    def get_tiempo_contratacion(self) -> str:
        return self._tiempoContratacion
        
    def set_fecha_contratacion(self, valor_FechaContratación: str) -> None:
        self._FechaContratación=valor_FechaContratación
    def get_fecha_contratacion(self) -> str:
        return self._FechaContratación

class AgenteAtencionCliente(Empleado):
    def __init__(usuario: Usuario, sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(usuario, sueldo, rango, tiempoContratacion, FechaContratación)
    def registrar_cliente(self,cliente:Cliente):
        usuarioFactory = UsuarioFactory()
        usuarioFactory.agregarCliente(cliente)
        pass
    def modificar_cliente(cliente):
        pass
    def buscar_cliente(id):
        pass
    def consultar_operacion_cliente():
        pass
    def generar_reporte_cliente():
        pass

class AdministradorArea(AgenteAtencionCliente):
    def __init__(usuario: Usuario, sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(usuario, sueldo, rango, tiempoContratacion, FechaContratación)
    def auditar_cliente():
        pass
    def eliminar_cliente():
        pass
    
