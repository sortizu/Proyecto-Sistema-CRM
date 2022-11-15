from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
#Conexion con la base de datos

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='atencion_cliente'
mysql = MySQL(app)

#Definicion de la ruta principal
@app.route('/')
def Index():
    return render_template('index.html')
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)