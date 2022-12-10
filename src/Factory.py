from abc import ABC, abstractmethod
from Seguridad import *
from Persistent import *
from decoradoresUsuario import *
from Conexion import *

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="DB_CRM_services_v3"
        )
mycursor = mydb.cursor()

class UsuarioFactory(PersistentFactory):
    def agregarCliente(self,cliente):
        
        sql = "INSERT INTO Usuario(dni, nombre_usuario, contraseña, nombre, apellido_paterno, apellido_materno, fecha_creacion," \
              "genero,direccion_1,direccion_2,nacionalidad,fecha_nacimiento,email,telefono)"\
              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        val = (cliente._usuario.get_dni(),cliente._usuario.get_nombre_usuario(),cliente._usuario.get_contraseña(),
        cliente._usuario.get_nombre(),cliente._usuario.get_apellido_paterno(),cliente._usuario.get_apellido_materno(),
        cliente._usuario.get_fecha_creacion(),cliente._usuario.get_genero(),cliente._usuario.get_direccion1(),cliente._usuario.get_direccion2(),
        cliente._usuario.get_nacionalidad(),cliente._usuario.get_fecha_nacimiento(),cliente._usuario.get_email(),cliente._usuario.get_telefono())
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "INSERT INTO Cliente(id_usuario, ruc, num_familiares,pasatiempo,numDispositivos,nse,tiempo_servicio)"\
              " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (cliente._usuario.get_dni(),cliente.get_ruc(),cliente.get_numero_familiares(),
        cliente.get_pasatiempo(),cliente.get_numero_dispositivos(),cliente.get_nivel_socieconomico(),
        cliente.get_tiempo_servicio())
        mycursor.execute(sql, val)
        mydb.commit()
        pass
    def listarClientes(self,cliente):
        print(cliente._usuario.get_nombre())
        pass
    def listarCliente(self,id):
        pass
    def actualizarCliente(self,UsuarioDeco):
        pass
    pass

class SeguridadFactory(PersistentFactory):
    pass