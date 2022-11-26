from flask import Flask,render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crm_ventas'
mysql = MySQL(app)


#Configuraciones
app.secret_key = 'mysecretkey'


#Funciones
@app.route('/')
def index():
    return redirect(url_for('catalogo', i = 1))


@app.route('/catalogo/<i>')
def catalogo(i):
    cur = mysql.connection.cursor()
    cur.execute('select nombre from oferta')
    data_ofertas = cur.fetchall()
    cur.execute('select nombre from plan')
    data_planes = cur.fetchall()
    cur.execute('select nombre from marca')
    data_marcas = cur.fetchall()
    cur.execute('select nombre from accesorio')
    data_accesorios = cur.fetchall()
    i = int(i)
    pos = 8*(i-1)+1
    cur.execute("select * from producto where id_producto >= '{0}' limit 8".format(pos))
    data_productos = cur.fetchall()
    print (data_productos)
    return render_template('catalogo.html', ofertas = data_ofertas, planes = data_planes, marcas = data_marcas, accesorios = data_accesorios, productos = data_productos)

@app.route('/detalles/<i>')#creo que está mal, que debe ser una url previa
def ver_detalles(i):
    cur = mysql.connection.cursor()
    cur.execute("select * from produto where id_producto = '{0}'".format(i))
    data_producto = cur.fetchall()
    cur.execute("select o.nombre, o.descripcion from oferta o, producto p where p.id_producto = {0} and p.fk_producto_oferta = o.id_oferta".format(i))
    data_plan = cur.fetchall()
    cur.execute("select o.nombre, o.descripcion from oferta o, producto p where p.id_producto = {0} and p.fk_producto_oferta = o.id_oferta".format(i))
    data_accesorio = cur.fetchall()
    cur.execute("select o.nombre, o.descripcion from oferta o, producto p where p.id_producto = {0} and p.fk_producto_oferta = o.id_oferta".format(i))
    data_oferta = cur.fetchall()
    return render_template('detalles.html', producto = data_producto, plan = data_plan, accesorio = data_accesorio, oferta = data_oferta)

"""
@app.route('/catalogo/<int: id>')   #BUSQUEDA POR ID
def busq_id(id):
    cur = mysql.connection.cursor()
    cur.execute('select nombre from oferta')
    data_ofertas = cur.fetchall()
    cur.execute('select nombre from plan')
    data_planes = cur.fetchall()
    cur.execute('select nombre from marca')
    data_marcas = cur.fetchall()
    cur.execute('select nombre from accesorio')
    data_accesorios = cur.fetchall()
    cur.execute('select * from producto where id_producto = id')
    data_productos = cur.fetchall()
    print (data_productos)
    return render_template('catalogo.html', ofertas = data_ofertas, planes = data_planes, marcas = data_marcas, accesorios = data_accesorios, productos = data_productos)


@app.route('/catalogo', methods = ['POST'])
def filtro_precios(min_precio,max_precio):
    if request.method == 'POST':
        min_precio = request.form['min_precio']
        max_precio = request.form['max_precio']
        cur = mysql.connection.cursor()
        cur.execute('select * from producto where precio between %s and %s limit 1', format(min_precio, max_precio))
        data_productos = cur.fetchall()
        print (data_productos)
        return render_template('catalogo.html', productos = data_productos)


@app.route('/catalogo/<int: min>/<int: max>', methods = ['POST'])
def filtro_precios2(min,max):
    if request.method == 'POST':
        min_precio = request.form['min_precio']
        max_precio = request.form['max_precio']
        cur = mysql.connection.cursor()
        cur.execute('select * from producto where precio between %s and %s limit 1', format(min_precio, max_precio))
        data_productos = cur.fetchall()
        print (data_productos)
        return render_template('catalogo.html', productos = data_productos)


@app.route('/detalles/<int: id>')#creo que está mal, que debe ser una url previa
def ver_detalles(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from producto where id = %s',id)
    data_producto = cur.fetchall()
    return render_template('detalles.html', producto = data_producto)


@app.route('/carrito')
def ver_carrito():
    return 'Viendo carrito'


#Main
if __name__ == '__main__':
    app.run(port = 3000, debug = True)

"""