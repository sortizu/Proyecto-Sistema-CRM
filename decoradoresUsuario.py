from abc import abstractclassmethod
from usuario import Usuario
from datetime import date
from Conexion import conexion

conn = conexion
class UsuarioDeco(Usuario):
    @abstractclassmethod
    def __init__(self) -> None:
        super().__init__()



class Cliente(UsuarioDeco):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario: Usuario, ruc, numFamiliares, pasatiempo, numDispositivos, nivelSocioeconomico, tiempoServicio) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono)
        self._usuario = usuario
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

     #Ingresa una tupla nueva en la tabla de clientes
    


class Empleado(UsuarioDeco):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario: Usuario,  sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono)
        self._usuario = usuario
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

    def registrarCliente():
        nombre_usuario=input("Nombres: ")
        contrasenia = input("contraseña: ")
        #fecha_creacion = input("fecha_creacion: ")
        apellido_paterno = input("apellido_paterno: ")
        apellido_materno = input("apellido_materno: ")
        genero = input("genero: ")
        direccion = input("direccion: ")
        ubigeo = input("ubigeo: ")
        nacionalidad = input("nacionalidad: ")
        fecha_nacimiento = input("fecha_nacimiento: ")
        dni = input("dni: ")
        email = input("email: ")
        telefono = input("telefono: ")
        ruc = input("ruc: ")
        servicio_cliente = input("servicio_cliente: ")
        num_familiares = input("num_familiares: ")
        servicio_familiar = input("servicio_familiar: ")
        pasatiempo = input("pasatiempo: ")
        num_dispositivos = input("num_dispositivos: ")
        nivel_socioeconomico = input("nivel_socioeconomico: ")
        proveedor_anterior = input("proveedor_anterior: ")
        tiempo_servicio = input("tiempo_servicio: ")

        sql = "INSERT INTO cliente(nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno, genero," \
              " direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email, telefono, ruc, servicio_cliente, num_familiares," \
              " servicio_familiar, pasatiempo, num_dispositivos, nivel_socioeconomico, proveedor_anterior, tiempo_servicio)" \
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nombre_usuario, contrasenia,   date.today(), apellido_paterno, apellido_materno, genero, direccion, ubigeo, nacionalidad,
               fecha_nacimiento, dni, email, telefono, ruc, servicio_cliente, int(num_familiares),
               servicio_familiar, pasatiempo, int(num_dispositivos), nivel_socioeconomico, proveedor_anterior, tiempo_servicio)
        conn.mycursor.execute(sql, val)
        conn.mydb.commit()
    
    #Se encarga de encontrar a un cliente en particular si no lo encuentra debuelcve 0
    def buscarCliente(n,idem):
        # Busqueda por id del cliente
        if n == 1:
            conn.mycursor.execute("SELECT * FROM cliente WHERE id_cliente=" + str(idem))
            myresult = conn.mycursor.fetchall()

        # busqueda por DNI del cliente
        if n == 2:
            conn.mycursor.execute("SELECT * FROM cliente WHERE dni=" + str(idem))
            myresult = conn.mycursor.fetchall()

        else:
            print("Objetivo de busqueda inapropiado")

        print(myresult[0][3])
        for x in myresult:
            print(x)



    #Se encarga de imprimier en pantalla los atributos de u cliente los cuales se reallizan con la busqueda mediante su ID o DNI
    def generarReporteCliente(n, idem):
        # Busqueda por id del cliente
        if n == 1:
            conn.mycursor.execute("SELECT * FROM cliente WHERE id_cliente=" + str(idem))
            myresult = conn.mycursor.fetchall()

        # busqueda por DNI del cliente
        if n == 2:
            conn.mycursor.execute("SELECT * FROM cliente WHERE dni=" + str(idem))
            myresult = conn.mycursor.fetchall()

        else:
            print("Objetivo de busqueda inapropiado")

        print(myresult[0][3])
        for x in myresult:
            print(x)

    #MOdifica los datos en la BD
    def actualizarCliente(idem, nombre_usuario,contrasenia, apellido_paterno,apellido_materno,genero,direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email,
                 telefono, ruc,servicio_cliente,num_familiares,servicio_familiar,pasatiempo, num_dispositivos, nivel_socioeconomico,proveedor_anterior,tiempo_servicio):
        sql = "UPDATE cliente SET nombre_usuario = '"+nombre_usuario+"', contrasenia ='"+contrasenia+"', apellido_paterno ='"+apellido_paterno+"', apellido_materno ='"+apellido_materno+\
              "',  genero='"+genero+"',  direccion='"+direccion+"',  ubigeo='"+ubigeo+"', nacionalidad='"+nacionalidad+"', fecha_nacimiento='"+fecha_nacimiento+\
              "', dni='"+dni+"', email='"+email+"', telefono='"+telefono+"', ruc='"+ruc+"', servicio_cliente='"+servicio_cliente+"', num_familiares='"+str(num_familiares)+\
              "', servicio_familiar='"+servicio_familiar+"', pasatiempo='"+pasatiempo+"', num_dispositivos='"+str(num_dispositivos)+"', nivel_socioeconomico='"+nivel_socioeconomico+\
              "', proveedor_anterior='"+proveedor_anterior+"', tiempo_servicio='"+tiempo_servicio+"' WHERE id_cliente= "+str(idem)
        conn.mycursor.execute(sql)
        conn.mydb.commit()
        print(conn.mycursor.rowcount, "registros afectado/s")

class AgenteAtencionCliente(Empleado):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario: Usuario, sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario, sueldo, rango, tiempoContratacion, FechaContratación)

class AdministradorArea(Empleado):
    def __init__(self, dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario: Usuario, sueldo, rango, tiempoContratacion, FechaContratación) -> None:
        super().__init__(dni, nombreUsuario, contraseña, fechaCreacion, apellidoPaterno, apellidoMaterno, genero, direccion1, direccion2, nacionalidad, fechaNacimiento, email, telefono, usuario, sueldo, rango, tiempoContratacion, FechaContratación)
    
