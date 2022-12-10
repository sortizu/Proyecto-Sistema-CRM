from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
from decoradoresUsuario import *
from usuario import *

app=Flask(__name__)

usuarioActual=ConcreteUsuario(74925387,"sortizu","1234",date.today(),"Sebastian","Ortiz","Urbai",1,"Av Hipolito Unanue #3","Condominio 'claro de luna'","Peruano","2001-11-18","mmm@gmail.com","939352147")
empleadoActual = AgenteAtencionCliente(usuarioActual,"Agente de atencion al cliente",3,"2018-3-20")

#Definicion de la ruta principal
@app.route('/')
def Index():
    return render_template('index.html')
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')
@app.route('/clientes/<funcion>',methods=['GET'])
def registro_clientes(funcion):
    return render_template('clientes.html',funcion=funcion)

@app.route('/clientes/ejecutarRegistro',methods=['POST'])
def obtener_datos_registro_clientes():
    usuario = ConcreteUsuario(request.form['dni'],request.form['nombreUsuario'],request.form['contraseña'],
    date.today(),request.form['nombre'],request.form['ApellidoP'],request.form['ApellidoM'],0,
    request.form['direccion1'],request.form['direccion2'],request.form['nacionalidad'],request.form['fechaNacimiento'],
    request.form['email'],request.form['telefono'])
    if(str(request.form['genero']).lower()=="femenino"):
        usuario.set_genero(0)
    else:
        usuario.set_genero(1)
    clienteARegistrar=Cliente(usuario,request.form['ruc'],request.form['numeroFamiliares'],request.form['pasatiempo'],
    request.form['numeroDispositivos'],request.form['nivelSoc'],0)
    empleadoActual.registrar_cliente(clienteARegistrar)
    return {}

if __name__ == '__main__':
    app.run(port=3000, debug=True)