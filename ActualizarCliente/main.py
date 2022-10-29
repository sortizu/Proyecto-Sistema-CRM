import mariadb
import sys
from datetime import date
import mysql.connector
import self


#Realiza la conexion con la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="atencion_cliente"
)
mycursor = mydb.cursor()


#Clase para implementar la busqueda del ubigeo del cliente en la base de datos
class ubigeo:
    def __init__(self, id_ubigeo, departemento, provincia, distrito, codigo_postal):
        self.__departemento = departemento
        self.__provincia = provincia
        self.__distrito = distrito
        self.__codigo_postal = codigo_postal

#Clase para definir a los proveedores anteriores de nuestro cliente
class Proveedor:
    def __init__(self,id_proveedor, nombre, descripcion, ruc, tipo):
        self.__id_proveedor = id_proveedor
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__ruc = ruc
        self.__tipo = tipo

#Clase usuario, del que heredaran atributos clases hijas como cliente y empleado.
class usuario:
    def __init__(self, id_usuario, nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno,
                 genero, direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email, telefono):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = nombre_usuario
        self.contrasenia= contrasenia
        self.__fecha_creacion = fecha_creacion
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__genero = genero
        self.__direccion = direccion
        self.__ubigeo = ubigeo
        self.__nacionalidad = nacionalidad
        self.__fecha_nacimiento = fecha_nacimiento
        self.__dni = dni
        self.__email = email
        self.__telefono = telefono

#Clase Cliente, hereda atributos de la clase usuario.
class cliente(usuario):
    def __init__(self, id_usuario, nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno,
                 genero, direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email, telefono,id_cliente,ruc,
                 servicio_cliente, num_familiares, servicio_familiar, pasatiempo,num_dispositivos, nivel_socioeconomico,
                 proveedor_anterior, tiempo_servicio):
        super().__init__(id_usuario, nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno,
                         genero, direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email, telefono )
        self.__id_cliente = id_cliente
        self.__ruc = ruc
        self.__servicio_cliente = servicio_cliente
        self.__num_familiares = num_familiares
        self.__servicio_familiar = servicio_familiar
        self.__pasatiempo = pasatiempo
        self.__num_dispositivos = num_dispositivos
        self.__nivel_socioeconomico = nivel_socioeconomico
        self.__proveedor_anterior = proveedor_anterior
        self.__tiempo_servicio = tiempo_servicio

    #Ingresa una tupla nueva en la tabla de clientes
    def in_data():
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
        mycursor.execute(sql, val)
        mydb.commit()



    #Se encarga de imprimier en pantalla los atributos de u cliente los cuales se reallizan con la busqueda mediante su ID o DNI
    def print_data(n, idem):
        # Busqueda por id del cliente
        if n == 1:
            mycursor.execute("SELECT * FROM cliente WHERE id_cliente=" + str(idem))
            myresult = mycursor.fetchall()

        # busqueda por DNI del cliente
        if n == 2:
            mycursor.execute("SELECT * FROM cliente WHERE dni=" + str(idem))
            myresult = mycursor.fetchall()

        else:
            print("Objetivo de busqueda inapropiado")

        print(myresult[0][3])
        for x in myresult:
            print(x)

    def mod_data(idem, nombre_usuario,contrasenia, apellido_paterno,apellido_materno,genero,direccion, ubigeo, nacionalidad, fecha_nacimiento, dni, email,
                 telefono, ruc,servicio_cliente,num_familiares,servicio_familiar,pasatiempo, num_dispositivos, nivel_socioeconomico,proveedor_anterior,tiempo_servicio):
        sql = "UPDATE cliente SET nombre_usuario = '"+nombre_usuario+"', contrasenia ='"+contrasenia+"', apellido_paterno ='"+apellido_paterno+"', apellido_materno ='"+apellido_materno+\
              "',  genero='"+genero+"',  direccion='"+direccion+"',  ubigeo='"+ubigeo+"', nacionalidad='"+nacionalidad+"', fecha_nacimiento='"+fecha_nacimiento+\
              "', dni='"+dni+"', email='"+email+"', telefono='"+telefono+"', ruc='"+ruc+"', servicio_cliente='"+servicio_cliente+"', num_familiares='"+str(num_familiares)+\
              "', servicio_familiar='"+servicio_familiar+"', pasatiempo='"+pasatiempo+"', num_dispositivos='"+str(num_dispositivos)+"', nivel_socioeconomico='"+nivel_socioeconomico+\
              "', proveedor_anterior='"+proveedor_anterior+"', tiempo_servicio='"+tiempo_servicio+"' WHERE id_cliente= "+str(idem)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "registros afectado/s")

class auditoria:
    def __init__(self, id_auditoria, nombre, valor_anterior, valor_actual, fecha_de_modificacion, autor):
        self.__id_auditoria =id_auditoria
        self.__nombre =nombre
        self.__valor_anterior =valor_anterior
        self.__valor_actual =valor_actual
        self.__fecha_de_modificacion =fecha_de_modificacion
        self.__autor =autor



#cnx = test_conexion
c=cliente
#c.in_data()

c.mod_data(1, 'nombre_usuario','contrasenia', 'apellido_paterno','Aapellido_materno','genero','direccion', 'ubigeo', 'nacionalidad', '2000-15-12', 'dni', 'email',
                 '65464', '131','servicio_cliente',2,'servicio_familiar','pasatiempo', 5, 'A','Claro','2 años')
c.print_data(1, 1)



