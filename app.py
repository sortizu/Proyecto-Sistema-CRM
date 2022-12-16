from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from config import config
# Instancias Flask
app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '50bb11b76'
app.config['MYSQL_DB'] = 'crm_ventas'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('modulo_ventas.html')


@app.route('/intento')
def llenar_catalogo():
    try:
        cursor = mysql.connection.cursor()

        sql = "SELECT nombre, id_producto, stock, precio FROM producto"
        cursor.execute(sql)
        productos = cursor.fetchall()

        sql = "SELECT DISTINCT memoria_ram FROM equipo"
        cursor.execute(sql)
        rams = cursor.fetchall()

        sql = "SELECT DISTINCT procesador FROM equipo"
        cursor.execute(sql)
        procesadores = cursor.fetchall()

        sql = "SELECT DISTINCT camara_principal FROM equipo"
        cursor.execute(sql)
        camaras = cursor.fetchall()

        sql = "SELECT id_plan, nombre FROM plan"
        cursor.execute(sql)
        planes = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return render_template('modulo_ventas.html', data_productos=productos, data_ram=rams, data_procesador=procesadores, data_camara=camaras, data_plan=planes)


def query_string():
    print(request)


@app.route('/productos')
def listar_productos():
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM producto"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            producto = {'id_producto': fila[0], 'fk_producto_equipo': fila[0], 'fk_producto_oferta': fila[2],
                        'nombre': fila[3], 'precio': fila[4], 'stock': fila[5]}
            productos.append(producto)
    except Exception as ex:
        print(ex)
    return jsonify(productos)


def devolver_equipo(id):
    try:
        plan = {}
        accesorio = {}
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM equipo where id_equipo='{0}'".format(id)
        cursor.execute(sql)
        datos_equipo = cursor.fetchall()
        if datos_equipo[0][13] != None:
            id_plan = datos_equipo[0][13]
            sql = "SELECT * FROM plan WHERE id_plan= '{0}'".format(id_plan)
            cursor.execute(sql)
            datos_plan = cursor.fetchall()
            plan = {'id_plan': datos_plan[0][0], 'nombre': datos_plan[
                0][1], 'precio': datos_plan[0][2], 'descripcion': datos_plan[0][3]}

        if datos_equipo[0][14] != None:
            id_accesorio = datos_equipo[0][14]
            sql = "SELECT * FROM accesorio WHERE id_accesorio= '{0}'".format(
                id_accesorio)
            cursor.execute(sql)
            datos_accesorio = cursor.fetchall()
            accesorio = {'id_accesorio': datos_accesorio[0][0], 'nombre': datos_accesorio[0][1],
                         'precio': datos_accesorio[0][2], 'stock': datos_accesorio[0][3], 'descripcion': datos_accesorio[0][4]}

        equipo = {'id_equipo': datos_equipo[0][0], 'nombre': datos_equipo[0][1], 'memoria_ram': datos_equipo[0][2], 'memoria_interna': datos_equipo[0][3], 'pantalla': datos_equipo[0][4], 'camara_principal': datos_equipo[0][5], 'procesador': datos_equipo[0]
                  [6], 'bateria': datos_equipo[0][7], 'color': datos_equipo[0][8], 'garantia': datos_equipo[0][9], 'precio': datos_equipo[0][10], 'stock': datos_equipo[0][11], 'descripcion': datos_equipo[0][12], 'plan': plan, 'accesorio': accesorio}
    except Exception as ex:
        print(ex)
    return equipo


def devolver_oferta(id):
    oferta = {}
    try:
        if id != None:
            cursor = mysql.connection.cursor()
            sql = "SELECT * FROM oferta WHERE id_oferta= '{0}'".format(id)
            cursor.execute(sql)
            datos_oferta = cursor.fetchall()
            oferta = {'id_oferta': datos_oferta[0][0], 'nombre': datos_oferta[0][1],
                      'descuento': datos_oferta[0][2], 'descripcion': datos_oferta[0][3]}
    except Exception as ex:
        print(ex)
    return oferta


@app.route('/ventas/<id>', methods=['GET'])
def entregar_ventas(id):
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM venta where id_cliente='{0}'".format(id)
        cursor.execute(sql)
        datos_venta = cursor.fetchall()
        ventas = []
        for fila in datos_venta:
            sql = "SELECT * FROM detalle_venta WHERE fk_detventa_venta='{0}'".format(
                fila[0])
            cursor.execute(sql)
            detalles_venta = cursor.fetchall()
            detalles = []
            for row in detalles_venta:
                sql = "SELECT * FROM producto WHERE id_producto='{0}'".format(
                    row[1])
                cursor.execute(sql)
                prod = cursor.fetchall()
                equipo = devolver_equipo(prod[0][1])
                oferta = devolver_oferta(prod[0][2])
                producto = {'id_producto': prod[0][0], 'equipo': equipo, 'oferta': oferta, 'nombre': prod[0]
                            [3], 'precio': prod[0][4], 'stock': prod[0][5], }
                detalle = {'id_detalle_venta': row[0], 'producto': producto,
                           'id_venta': row[2], 'cantidad': row[3], 'total': row[4]}
                detalles.append(detalle)
            venta = {'id_venta': fila[0], 'monto': fila[1], 'fecha': fila[2], 'id_vendedor': fila[3],
                     'id_cliente': fila[4], 'forma_pago': fila[5], 'detalles_venta': detalles}
            ventas.append(venta)
        print(datos_venta)
    except Exception as ex:
        print(ex)
    return jsonify(ventas)


if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.run(debug=True)
# Funciones
# @app.route('/')
# def index():
#     return redirect(url_for('catalogo_default', i=1))


# @app.route('/catalogo')
# def index2():
#     return redirect(url_for('catalogo_default', i=1))


# @app.route('/catalogo/<i>')
# def catalogo_default(i):

#     cur = mysql.connection.cursor()

#     i = int(i)
#     pos = 8*(i-1)+1
#     cur.execute(
#         f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo and id_producto >= '{pos}' order by id_producto limit 8;")
#     data_productos = cur.fetchall()

#     cur.execute('select nombre from oferta')
#     data_ofertas = cur.fetchall()

#     cur.execute('select nombre from plan')
#     data_planes = cur.fetchall()

#     cur.execute('select nombre from accesorio')
#     data_accesorios = cur.fetchall()

#     return render_template('modulo_ventas.html', productos=data_productos, ofertas=data_ofertas, planes=data_planes, accesorios=data_accesorios)


# @app.route('/catalogo/producto', methods=['GET', 'POST'])
# def catalogo_idproducto():

#     #    if request.method == "POST":
#     #        i=request.form['id']
#     if request.method == "GET":
#         i = request.args['id']

#     cur = mysql.connection.cursor()

#     cur.execute(
#         f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo and id_producto = '{i}';")
#     data_productos = cur.fetchall()

#     cur.execute('select nombre from oferta')
#     data_ofertas = cur.fetchall()

#     cur.execute('select nombre from plan')
#     data_planes = cur.fetchall()

#     cur.execute('select nombre from accesorio')
#     data_accesorios = cur.fetchall()

#     return render_template('modulo_ventas.html', productos=data_productos, ofertas=data_ofertas,
#                            planes=data_planes, accesorios=data_accesorios)


# @app.route('/catalogo', methods=['GET', 'POST'])
# def catalogo_ordenado():

#     if request.method == "POST":
#         opcion_ordenar = request.form['opcion_ordenar']
#         print(opcion_ordenar)

#         cur = mysql.connection.cursor()

#         cur.execute(
#             f"select p.*,e.link from crm_ventas.producto p, crm_ventas.equipo e where fk_producto_equipo = id_equipo order by '{opcion_ordenar}' asc;")
#         data_productos = cur.fetchall()

#         cur.execute('select nombre from oferta')
#         data_ofertas = cur.fetchall()

#         cur.execute('select nombre from plan')
#         data_planes = cur.fetchall()

#         cur.execute('select nombre from accesorio')
#         data_accesorios = cur.fetchall()

#     return render_template('modulo_ventas.html', productos=data_productos, ofertas=data_ofertas,
#                            planes=data_planes, accesorios=data_accesorios)


# @app.route('/detalles/<i>')  # creo que está mal, que debe ser una url previa
# def ver_detalles(i):
#     cur = mysql.connection.cursor()

#     cur.execute(
#         f"select pr.precio, pr.stock from producto pr where pr.id_producto = {i};")
#     data_producto = cur.fetchone()

#     cur.execute(
#         f"select e.nombre, e.descripcion, e.garantia, e.link from producto pr, equipo e where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo;")
#     data_equipo = cur.fetchone()

#     cur.execute(
#         f"select p.nombre, p.precio, p.descripcion from producto pr, equipo e, plan p where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo and e.fk_equipo_plan = p.id_plan;")
#     data_plan = cur.fetchone()

#     cur.execute(
#         f"select a.nombre, a.descripcion from producto pr, equipo e, accesorio a where pr.id_producto = '{i}' and pr.fk_producto_equipo = e.id_equipo and e.fk_equipo_accesorio = a.id_accesorio;")
#     data_accesorio = cur.fetchone()

#     cur.execute(
#         f"select o.nombre, concat(o.descuento*100,'%'), o.descripcion from oferta o, producto p where p.id_producto = {i} and p.fk_producto_oferta = o.id_oferta;")
#     data_oferta = cur.fetchone()

#     return render_template('modulo_ventas.html', producto=data_producto, equipo=data_equipo, plan=data_plan, accesorio=data_accesorio, oferta=data_oferta)


# @app.route('/carrito')
# def carrito():
#     return render_template('modulo_ventas.html')
