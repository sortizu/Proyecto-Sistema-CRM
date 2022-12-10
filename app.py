from flask import Flask,render_template, request, url_for, redirect
from flask_mysqldb import MySQL

#Instancias Flask
app = Flask(__name__)
app.secret_key = 'mysecretkey'

#Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crm_ventas'
mysql = MySQL(app)


#Funciones
@app.route('/')
def index():
    return redirect(url_for('catalogo_default', i = 1))

@app.route('/catalogo')
def index2():
    return redirect(url_for('catalogo_default', i = 1))

@app.route('/catalogo/<i>')
def catalogo_default(i):

    cur = mysql.connection.cursor()

    i = int(i)
    pos = 8*(i-1)+1
    cur.execute(f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo and id_producto >= '{pos}' order by id_producto limit 8;")
    data_productos = cur.fetchall()

    cur.execute('select nombre from oferta')
    data_ofertas = cur.fetchall()

    cur.execute('select nombre from plan')
    data_planes = cur.fetchall()

    cur.execute('select nombre from marca')
    data_marcas = cur.fetchall()

    cur.execute('select nombre from accesorio')
    data_accesorios = cur.fetchall()

    return render_template('catalogo.html', productos = data_productos, ofertas = data_ofertas, planes = data_planes, marcas = data_marcas, accesorios = data_accesorios)


@app.route('/catalogo/producto',methods=['GET','POST'])
def catalogo_idproducto():
    
#    if request.method == "POST":
#        i=request.form['id']
    if request.method == "GET":
        i=request.args['id']

    cur = mysql.connection.cursor()
    
    cur.execute(f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo and id_producto = '{i}';")
    data_productos = cur.fetchall()

    cur.execute('select nombre from oferta')
    data_ofertas = cur.fetchall()

    cur.execute('select nombre from plan')
    data_planes = cur.fetchall()

    cur.execute('select nombre from marca')
    data_marcas = cur.fetchall()

    cur.execute('select nombre from accesorio')
    data_accesorios = cur.fetchall()

    return render_template('catalogo.html', productos = data_productos, ofertas = data_ofertas,
        planes = data_planes, marcas = data_marcas, accesorios = data_accesorios)



@app.route('/catalogo',methods=['GET','POST'])
def catalogo_ordenado():
    
    if request.method == "POST":
        opcion_ordenar=request.form['opcion_ordenar']
        print(opcion_ordenar)

        cur = mysql.connection.cursor()
        
        cur.execute(f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo order by '{opcion_ordenar}' asc;")
        data_productos = cur.fetchall()

        cur.execute('select nombre from oferta')
        data_ofertas = cur.fetchall()

        cur.execute('select nombre from plan')
        data_planes = cur.fetchall()

        cur.execute('select nombre from marca')
        data_marcas = cur.fetchall()

        cur.execute('select nombre from accesorio')
        data_accesorios = cur.fetchall()

    return render_template('catalogo.html', productos = data_productos, ofertas = data_ofertas,
        planes = data_planes, marcas = data_marcas, accesorios = data_accesorios)




@app.route('/detalles/<i>')#creo que está mal, que debe ser una url previa
def ver_detalles(i):
    cur = mysql.connection.cursor()

    cur.execute(f"select pr.precio, pr.stock from producto pr where pr.id_producto = {i};")
    data_producto = cur.fetchone()

    cur.execute(f"select e.nombre, e.descripcion, e.garantia, e.link from producto pr, equipo e where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo;")
    data_equipo = cur.fetchone()

    cur.execute(f"select p.nombre, p.precio, p.descripcion from producto pr, equipo e, plan p where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo and e.fk_equipo_plan = p.id_plan;")
    data_plan = cur.fetchone()

    cur.execute(f"select a.nombre, a.descripcion from producto pr, equipo e, accesorio a where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo and e.fk_equipo_accesorio = a.id_accesorio;")
    data_accesorio = cur.fetchone()

    cur.execute(f"select o.nombre, concat(o.descuento*100,'%'), o.descripcion from oferta o, producto p where p.id_producto = {i} and p.fk_producto_oferta = o.id_oferta;")
    data_oferta = cur.fetchone()
    
    return render_template('detalles.html', producto = data_producto, equipo = data_equipo, plan = data_plan, accesorio = data_accesorio, oferta = data_oferta)


@app.route('/carrito')
def carrito():
    return render_template('carrito.html')



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