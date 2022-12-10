from abc import ABC, abstractmethod
class Usuario(ABC):
    def __init__(self) -> None:
        self._description = "Usuario"

class ConcreteUsuario(Usuario):
    def __init__(self, dni,nombreUsuario, contraseña, fechaCreacion, nombre,apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono) -> None:
        self._dni = dni
        self._nombreUsuario = nombreUsuario
        self._contraseña= contraseña
        self._fechaCreacion = fechaCreacion
        self._nombre=nombre
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._genero = genero
        self._direccion1 = direccion1
        self._direccion2 = direccion2
        self._nacionalidad = nacionalidad
        self._fechaNacimiento = fechaNacimiento
        self._email = email
        self._telefono = telefono

    def set_dni(self, valor_dni: str) -> None:
        self._dni=valor_dni
    def get_dni(self) -> str:
        return self._dni
    
    def set_nombre_usuario(self, valor_nombreUsuario: str) -> None:
        self._nombreUsuario=valor_nombreUsuario
    def get_nombre_usuario(self) -> str:
        return self._nombreUsuario
    
    def set_contraseña(self, valor_contraseña: str) -> None:
        self._contraseña=valor_contraseña
    def get_contraseña(self) -> str:
        return self._contraseña
    
    def set_fecha_creacion(self, valor_fechaCreacion: str) -> None:
        self._fechaCreacion=valor_fechaCreacion
    def get_fecha_creacion(self) -> str:
        return self._fechaCreacion
    
    def set_nombre(self, valor_nombre: str) -> None:
        self._nombre=valor_nombre
    def get_nombre(self) -> str:
        return self._nombre

    def set_apellido_paterno(self, valor_apellidoPaterno: str) -> None:
        self._apellidoPaterno=valor_apellidoPaterno
    def get_apellido_paterno(self) -> str:
        return self._apellidoPaterno
    
    def set_apellido_materno(self, valor_apellidoMaterno: str) -> None:
        self._apellidoMaterno=valor_apellidoMaterno
    def get_apellido_materno(self) -> str:
        return self._apellidoMaterno
    
    def set_genero(self, valor_genero: str) -> None:
        self._genero=valor_genero
    def get_genero(self) -> str:
        return self._genero
    
    def set_direccion1(self, valor_direccion1: str) -> None:
        self._direccion1=valor_direccion1
    def get_direccion1(self) -> str:
        return self._direccion1
    
    def set_direccion2(self, valor_direccion2: str) -> None:
        self.__direccion2=valor_direccion2
    def get_direccion2(self) -> str:
        return self._direccion2
    
    def set_nacionalidad(self, valor_nacionalidad: str) -> None:
        self._nacionalidad=valor_nacionalidad
    def get_nacionalidad(self) -> str:
        return self._nacionalidad
    
    def set_fecha_nacimiento(self, valor_fechaNacimiento: str) -> None:
        self._fechaNacimiento=valor_fechaNacimiento
    def get_fecha_nacimiento(self) -> str:
        return self._fechaNacimiento
     
    def set_email(self, valor_email: str) -> None:
        self._email=valor_email
    def get_email(self) -> str:
        return self._email
     
    def set_telefono(self, valor_telefono: str) -> None:
        self._telefono=valor_telefono
    def get_telefono(self) -> str:
        return self._telefono



"""
class Usuario(ABC):
    def __init__(self, dni,nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono) -> None:
        self._dni = dni
        self._nombreUsuario = nombreUsuario
        self._contraseña= contraseña
        self._fechaCreacion = fechaCreacion
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._genero = genero
        self._direccion1 = direccion1
        self._direccion2 = direccion2
        self._nacionalidad = nacionalidad
        self._fechaNacimiento = fechaNacimiento
        self._email = email
        self._telefono = telefono

    def set_dni(self, valor_dni: str) -> None:
        self._dni=valor_dni
    def get_dni(self) -> str:
        return self._dni
    
    def set_dni(self, valor_nombreUsuario: str) -> None:
        self._nombreUsuario=valor_nombreUsuario
    def get_dni(self) -> str:
        return self._nombreUsuario
    
    def set_dni(self, valor_contraseña: str) -> None:
        self._contraseña=valor_contraseña
    def get_dni(self) -> str:
        return self._contraseña
    
    def set_dni(self, valor_fechaCreacion: str) -> None:
        self._fechaCreacion=valor_fechaCreacion
    def get_dni(self) -> str:
        return self._fechaCreacion
    
    def set_dni(self, valor_apellidoPaterno: str) -> None:
        self._apellidoPaterno=valor_apellidoPaterno
    def get_dni(self) -> str:
        return self._apellidoPaterno
    
    def set_dni(self, valor_apellidoMaterno: str) -> None:
        self._apellidoMaterno=valor_apellidoMaterno
    def get_dni(self) -> str:
        return self._apellidoMaterno
    
    def set_dni(self, valor_genero: str) -> None:
        self._genero=valor_genero
    def get_dni(self) -> str:
        return self._genero
    
    def set_dni(self, valor_direccion1: str) -> None:
        self._direccion1=valor_direccion1
    def get_dni(self) -> str:
        return self._direccion1
    
    def set_dni(self, valor_direccion2: str) -> None:
        self.__direccion2=valor_direccion2
    def get_dni(self) -> str:
        return self.__direccion2
    
    def set_dni(self, valor_nacionalidad: str) -> None:
        self._nacionalidad=valor_nacionalidad
    def get_dni(self) -> str:
        return self._nacionalidad
    
    def set_dni(self, valor_fechaNacimiento: str) -> None:
        self._fechaNacimiento=valor_fechaNacimiento
    def get_dni(self) -> str:
        return self._fechaNacimiento
     
    def set_dni(self, valor_email: str) -> None:
        self._email=valor_email
    def get_dni(self) -> str:
        return self._email
     
    def set_dni(self, valor_telefono: str) -> None:
        self._telefono=valor_telefono
    def get_dni(self) -> str:
        return self._telefono


class Cliente(Usuario):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, ruc, numFamiliares, pasatiempo, numDispositivos, nivelSocioeconomico, tiempoServicio) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono)
        self._ruc = ruc
        self._numFamiliares = numFamiliares
        self._pasatiempo= pasatiempo
        self._numDispositivos = numDispositivos
        self._nivelSocioeconomico = nivelSocioeconomico
        self._tiempoServicio = tiempoServicio

        
    def set_dni(self, valor_ruc: str) -> None:
        self._ruc=valor_ruc
    def get_dni(self) -> str:
        return self.__ruc
        
    def set_dni(self, valor_numFamiliares: str) -> None:
        self._numFamiliares=valor_numFamiliares
    def get_dni(self) -> str:
        return self._numFamiliares
        
    def set_dni(self, valor_pasatiempo: str) -> None:
        self._pasatiempo=valor_pasatiempo
    def get_dni(self) -> str:
        return self._pasatiempo
        
    def set_dni(self, valor_numDispositivos: str) -> None:
        self._numDispositivos=valor_numDispositivos
    def get_dni(self) -> str:
        return self._numDispositivos
        
    def set_dni(self, valor_nivelSocioeconomico: str) -> None:
        self._nivelSocioeconomico=valor_nivelSocioeconomico
    def get_dni(self) -> str:
        return self._nivelSocioeconomico
        
    def set_dni(self, valor_tiempoServicio: str) -> None:
        self._tiempoServicio=valor_tiempoServicio
    def get_dni(self) -> str:
        return self._tiempoServicio


class EmpleadoBase(Usuario):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono)
        self._sueldo = sueldo
        self._rango = rango
        self._tiempoContratacion = tiempoContratacion
        self._FechaContratación = FechaContratación
        
    def set_dni(self, valor_sueldo: str) -> None:
        self._sueldo=valor_sueldo
    def get_dni(self) -> str:
        return self._sueldo
                
    def set_dni(self, valor_rango: str) -> None:
        self._rango=valor_rango
    def get_dni(self) -> str:
        return self._rango
        
    def set_dni(self, valor_tiempoContratacion: str) -> None:
        self._tiempoContratacion=valor_tiempoContratacion
    def get_dni(self) -> str:
        return self._tiempoContratacion
        
    def set_dni(self, valor_FechaContratación: str) -> None:
        self._FechaContratación=valor_FechaContratación
    def get_dni(self) -> str:
        return self._FechaContratación

"""