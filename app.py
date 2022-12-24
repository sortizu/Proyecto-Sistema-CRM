from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL
from config import config
# Instancias Flask
app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Conexion MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'crm_ventas'
# credenciales fabricio

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '50bb11b76'
app.config['MYSQL_DB'] = 'crm_ventas'

mysql = MySQL(app)


# @app.route('/')
# def index():
#     return redirect(url_for('llenar_catalogo'))


@app.route('/')
def index():
    return redirect(url_for('llenar_catalogo', id=1))


@app.route('/catalogo')
def index2():
    return redirect(url_for('llenar_catalogo', id=1))


@app.route('/catalogo/<id>')
def llenar_catalogo(id):
    try:
        cursor = mysql.connection.cursor()

        sql = "SELECT DISTINCT procesador FROM equipo order by procesador"
        cursor.execute(sql)
        procesadores = cursor.fetchall()

        sql = "SELECT id_plan, nombre FROM plan order by nombre"
        cursor.execute(sql)
        planes = cursor.fetchall()
    except Exception as ex:
        print(ex)
    return render_template('modulo_ventas.html', data_procesador=procesadores, data_plan=planes)


@app.route('/boleta/<id>')
def llenar_boleta(id):
    try:
        cursor = mysql.connection.cursor()

        sql = f"""select producto.nombre, cantidad, precio, concat(descuento*100,'%'), total
                from boleta, venta, detalle_venta, producto, oferta
                where id_boleta = {id}
                    and fk_boleta_venta = id_venta
                    and id_venta = fk_detventa_venta
                    and fk_detventa_producto = id_producto
                    and fk_producto_oferta = id_oferta"""

        cursor.execute(sql)

        detalles_venta = cursor.fetchall()

        sql = f"""select id_boleta, monto from boleta, venta where id_boleta = {id} and fk_boleta_venta = id_venta"""

        cursor.execute(sql)

        detalle_monto = cursor.fetchone()

        sql = f"""select EXTRACT(DAY FROM fecha), EXTRACT(month FROM fecha), EXTRACT(year FROM fecha)
                from boleta where id_boleta = {id}"""

        cursor.execute(sql)

        boleta_fecha = cursor.fetchone()

    except Exception as ex:
        print(ex)
    return render_template('boleta.html', data_detalles_venta=detalles_venta, data_detalle_monto=detalle_monto, data_boleta_fecha=boleta_fecha)


@app.route('/cotizacion/<id>')
def llenar_cotizacion(id):
    try:
        cursor = mysql.connection.cursor()

        sql = f"""select producto.nombre, cantidad, precio, concat(descuento*100,'%'), total
                from boleta, venta, detalle_venta, producto, oferta
                where id_boleta = {id}
                    and fk_boleta_venta = id_venta
                    and id_venta = fk_detventa_venta
                    and fk_detventa_producto = id_producto
                    and fk_producto_oferta = id_oferta"""

        cursor.execute(sql)

        detalles_venta = cursor.fetchall()

        sql = f"""select id_boleta, monto from boleta, venta where id_boleta = {id} and fk_boleta_venta = id_venta"""

        cursor.execute(sql)

        detalle_monto = cursor.fetchone()

        sql = f"""select EXTRACT(DAY FROM CURDATE()), EXTRACT(month FROM CURDATE()), EXTRACT(year FROM CURDATE())
                from boleta where id_boleta = {id}"""

        cursor.execute(sql)

        boleta_fecha = cursor.fetchone()

    except Exception as ex:
        print(ex)
    return render_template('cotizacion.html', data_detalles_venta=detalles_venta, data_detalle_monto=detalle_monto, data_boleta_fecha=boleta_fecha)


@app.route('/productos', methods=['POST'])
def productosjson():
    try:
        limite = request.form['pagina']
        offset = 10*(int(limite)-1)
        if (offset == 0):
            sql = "SELECT * FROM producto LIMIT 10"
        else:
            sql = "SELECT * FROM producto LIMIT 10 OFFSET "+str(offset)+";"
        cursor = mysql.connection.cursor()

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


# @app.route('/boleta/<id>')
# def llenar_boleta(id):
#     try:
#         cursor = mysql.connection.cursor()

#         sql = f"""select producto.nombre, cantidad, precio, concat(descuento*100,'%'), total
#                 from boleta, venta, detalle_venta, producto, oferta
#                 where id_boleta = {id}
#                     and fk_boleta_venta = id_venta
#                     and id_venta = fk_detventa_venta
#                     and fk_detventa_producto = id_producto
#                     and fk_producto_oferta = id_oferta"""

#         cursor.execute(sql)

#         detalles_venta = cursor.fetchall()

#         sql = f"""select id_boleta, monto from boleta, venta where id_boleta = {id} and fk_boleta_venta = id_venta"""

#         cursor.execute(sql)

#         detalle_monto = cursor.fetchone()

#         sql = f"""select EXTRACT(DAY FROM fecha), EXTRACT(month FROM fecha), EXTRACT(year FROM fecha)
#                 from boleta where id_boleta = {id}"""

#         cursor.execute(sql)

#         boleta_fecha = cursor.fetchone()

#     except Exception as ex:
#         print(ex)
#     return render_template('boleta.html', data_detalles_venta=detalles_venta, data_detalle_monto=detalle_monto, data_boleta_fecha=boleta_fecha)


# @app.route('/cotizacion/<id>')
# def llenar_cotizacion(id):
#     try:
#         cursor = mysql.connection.cursor()

#         sql = f"""select producto.nombre, cantidad, precio, concat(descuento*100,'%'), total
#                 from boleta, venta, detalle_venta, producto, oferta
#                 where id_boleta = {id}
#                     and fk_boleta_venta = id_venta
#                     and id_venta = fk_detventa_venta
#                     and fk_detventa_producto = id_producto
#                     and fk_producto_oferta = id_oferta"""

#         cursor.execute(sql)

#         detalles_venta = cursor.fetchall()

#         sql = f"""select id_boleta, monto from boleta, venta where id_boleta = {id} and fk_boleta_venta = id_venta"""

#         cursor.execute(sql)

#         detalle_monto = cursor.fetchone()

#         sql = f"""select EXTRACT(DAY FROM CURDATE()), EXTRACT(month FROM CURDATE()), EXTRACT(year FROM CURDATE())
#                 from boleta where id_boleta = {id}"""

#         cursor.execute(sql)

#         boleta_fecha = cursor.fetchone()

#     except Exception as ex:
#         print(ex)
#     return render_template('cotizacion.html', data_detalles_venta=detalles_venta, data_detalle_monto=detalle_monto, data_boleta_fecha=boleta_fecha)


@app.route('/consultaclientes/<id_producto>')
def devolver_clienteproductojson(id_producto):
    try:
        cursor = mysql.connection.cursor()
        sql = f"SELECT id_cliente FROM venta, detalle_venta where fk_detventa_producto={id_producto} and id_venta = fk_detventa_venta;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        clientesxprod = []
        for fila in datos:
            clientexprod = {'id_cliente': fila[0]}
            clientesxprod.append(clientexprod)
    except Exception as ex:
        print(ex)
    return jsonify(clientesxprod)


@app.route('/consultaprod/<id_cliente>/<fecha_inicio>/<fecha_fin>')
def devolver_prodxclientejson(id_cliente, fecha_inicio, fecha_fin):
    try:
        cursor = mysql.connection.cursor()
        sql = f"SELECT id_venta, cantidad, total, id_vendedor, fecha FROM venta, detalle_venta where id_cliente={id_cliente} and id_venta = fk_detventa_venta and fecha >= '{fecha_inicio}' and fecha <= '{fecha_fin}'"
        cursor.execute(sql)
        datos = cursor.fetchall()
        prodsxcliente = []
        for fila in datos:
            prodxcliente = {'id_venta': fila[0], 'cantidad': fila[1],
                            'monto': fila[2], 'id_vendedor': fila[3], 'fecha': fila[4]}
            prodsxcliente.append(prodxcliente)
    except Exception as ex:
        print(ex)
    return jsonify(prodsxcliente)

# venta idventa
# detallesdeventa


@app.route('/producto/<id>')
def devolver_productojson(id):
    try:
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM producto WHERE id_producto='{id}'"
        cursor.execute(sql)
        datos_producto = cursor.fetchall()
        datos_equipo = devolver_equipo(datos_producto[0][1])
        datos_oferta = devolver_oferta(datos_producto[0][2])
        producto = {'idproducto': datos_producto[0][0], 'equipo': datos_equipo, 'oferta': datos_oferta, 'nombre': datos_producto[0][3],
                    'precio': datos_producto[0][4], 'stock': datos_producto[0][5]}

    except Exception as ex:
        print(ex)
    return jsonify(producto)


@app.route('/equipo/<id>', methods=['get'])
def devolver_equipojson(id):
    try:
        plan = {}
        accesorio = {}
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM equipo where id_equipo='{id}'"
        cursor.execute(sql)
        datos_equipo = cursor.fetchall()
        if datos_equipo[0][13] != None:
            id_plan = datos_equipo[0][13]
            sql = f"SELECT * FROM plan WHERE id_plan= '{id_plan}'"
            cursor.execute(sql)
            datos_plan = cursor.fetchall()
            plan = {'id_plan': datos_plan[0][0], 'nombre': datos_plan[
                0][1], 'precio': datos_plan[0][2], 'descripcion': datos_plan[0][3]}

        if datos_equipo[0][14] != None:
            id_accesorio = datos_equipo[0][14]
            sql = f"SELECT * FROM accesorio WHERE id_accesorio= '{id_accesorio}'"
            cursor.execute(sql)
            datos_accesorio = cursor.fetchall()
            accesorio = {'id_accesorio': datos_accesorio[0][0], 'nombre': datos_accesorio[0][1],
                         'precio': datos_accesorio[0][2], 'stock': datos_accesorio[0][3], 'descripcion': datos_accesorio[0][4]}

        equipo = {'id_equipo': datos_equipo[0][0], 'nombre': datos_equipo[0][1], 'memoria_ram': datos_equipo[0][2], 'memoria_interna': datos_equipo[0][3], 'pantalla': datos_equipo[0][4], 'camara_principal': datos_equipo[0][5], 'procesador': datos_equipo[0]
                  [6], 'bateria': datos_equipo[0][7], 'color': datos_equipo[0][8], 'garantia': datos_equipo[0][9], 'precio': datos_equipo[0][10], 'stock': datos_equipo[0][11], 'descripcion': datos_equipo[0][12], 'plan': plan, 'accesorio': accesorio}
    except Exception as ex:
        print(ex)
    return jsonify(equipo)


def generar_dbventa():
    try:
        cursor = mysql.connection.cursor()
        monto = 230
        id_vendedor = 1
        id_cliente = 747
        forma_pago = "efectivo"
        sql = f"insert into venta(monto, fecha, id_vendedor, id_cliente, forma_pago) values ({monto},DATE(NOW()),{id_vendedor},{id_cliente},{forma_pago})"
        cursor.execute(sql)
        mysql.connection.commit()
    except Exception as ex:
        print(ex)
    return "intento"


@app.route('/ofertas/<id>', methods=['get'])
def devolver_ofertajson(id):
    oferta = {}
    try:
        if id != None:
            cursor = mysql.connection.cursor()
            sql = f"SELECT * FROM oferta WHERE id_oferta= '{id}'"
            cursor.execute(sql)
            datos_oferta = cursor.fetchall()
            oferta = {'id_oferta': datos_oferta[0][0], 'nombre': datos_oferta[0][1],
                      'descuento': datos_oferta[0][2], 'descripcion': datos_oferta[0][3]}
    except Exception as ex:
        print(ex)
    return jsonify(oferta)


@app.route('/ventas/<id>', methods=['GET'])
def entregar_ventas(id):
    try:
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM venta where id_cliente='{id}'"
        cursor.execute(sql)
        datos_venta = cursor.fetchall()
        ventas = []
        for fila in datos_venta:
            sql = f"SELECT * FROM detalle_venta WHERE fk_detventa_venta='{fila[0]}'"
            cursor.execute(sql)
            detalles_venta = cursor.fetchall()
            detalles = []
            for row in detalles_venta:
                sql = f"SELECT * FROM producto WHERE id_producto='{row[1]}'"
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


def devolver_equipo(id):
    try:
        plan = {}
        accesorio = {}
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM equipo where id_equipo='{id}'"
        cursor.execute(sql)
        datos_equipo = cursor.fetchall()
        if datos_equipo[0][13] != None:
            id_plan = datos_equipo[0][13]
            sql = f"SELECT * FROM plan WHERE id_plan= '{id_plan}'"
            cursor.execute(sql)
            datos_plan = cursor.fetchall()
            plan = {'id_plan': datos_plan[0][0], 'nombre': datos_plan[
                0][1], 'precio': datos_plan[0][2], 'descripcion': datos_plan[0][3]}

        if datos_equipo[0][14] != None:
            id_accesorio = datos_equipo[0][14]
            sql = f"SELECT * FROM accesorio WHERE id_accesorio= '{id_accesorio}'"
            cursor.execute(sql)
            datos_accesorio = cursor.fetchall()
            accesorio = {'id_accesorio': datos_accesorio[0][0], 'nombre': datos_accesorio[0][1],
                         'precio': datos_accesorio[0][2], 'stock': datos_accesorio[0][3], 'descripcion': datos_accesorio[0][4]}

        equipo = {'id_equipo': datos_equipo[0][0], 'nombre': datos_equipo[0][1], 'memoria_ram': datos_equipo[0][2], 'memoria_interna': datos_equipo[0][3], 'pantalla': datos_equipo[0][4], 'camara_principal': datos_equipo[0][5], 'procesador': datos_equipo[0][6],
                  'bateria': datos_equipo[0][7], 'color': datos_equipo[0][8], 'garantia': datos_equipo[0][9], 'precio': datos_equipo[0][10], 'stock': datos_equipo[0][11], 'descripcion': datos_equipo[0][12], 'plan': plan, 'accesorio': accesorio, 'link': datos_equipo[0][15]}
    except Exception as ex:
        print(ex)
    return equipo


def devolver_oferta(id):
    oferta = {}
    try:
        if id != None:
            cursor = mysql.connection.cursor()
            sql = f"SELECT * FROM oferta WHERE id_oferta= '{id}'"
            cursor.execute(sql)
            datos_oferta = cursor.fetchall()
            oferta = {'id_oferta': datos_oferta[0][0], 'nombre': datos_oferta[0][1],
                      'descuento': datos_oferta[0][2], 'descripcion': datos_oferta[0][3]}
    except Exception as ex:
        print(ex)
    return oferta


if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.run(debug=True)
