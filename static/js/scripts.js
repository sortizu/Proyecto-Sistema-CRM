function llenarCatalogo() {

}
consultaProductos();
document.addEventListener("click", e => {
    if (e.target.getAttribute("name") == "detalles") {
        var tr = e.target.parentElement.parentElement;
        var th = tr.parentElement;
        consultaDetalles(th.getAttribute('id'));
    }
    if (e.target.getAttribute("name") == "agregar") {
        var tr = e.target.parentElement.parentElement;
        var th = tr.parentElement;
        agregarCarrito(th.getAttribute('id'));
    }

})
function agregarCarrito(id) {
    url = '/producto/' + id;
    xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.responseType = 'json';
    xhr.send();
    xhr.onload = function () {
        respuesta = xhr.response;
        llenarCarrito(respuesta);
    }
}
function llenarCarrito(respuesta) {
    const carrito = document.getElementById('carrito');
    for (i = 1; i < carrito.children.length; i++) {
        idfil = carrito.children[i].children[0].children[0].textContent;
        if (respuesta.idproducto == idfil) {
            tr = carrito.children[i].children[0];
            sumarCantidad(tr);
            return;
        }
    }
    carrito.innerHTML += '<tr id="fila' + respuesta.idproducto + '"><th style="width:10%;">' + respuesta.idproducto + '</th><th><label name="producto">' + respuesta.nombre + '</label></th><th><button onclick="restarCantidad(fila' + respuesta.idproducto + ')" class="btn-secondary" name="cantidad"> - </button><label>1</label><button onclick="sumarCantidad(fila' + respuesta.idproducto + ')" class="btn-secondary">+</button></th><th><label name="unidad">' + respuesta.precio + '</label></th><th><label name="total">' + respuesta.precio + '</label></th></tr>';
    calcularImporteSub();
}
function sumarCantidad(id) {
    cantidad = id.children[2].children[1].textContent;
    cantidad = parseInt(cantidad);
    id.children[2].children[1].textContent = cantidad + 1;
    calcularTotal(id);
}
function restarCantidad(id) {
    cantidad = id.children[2].children[1].textContent;
    cantidad = parseInt(cantidad);
    if (cantidad == 1) {
        tabla = document.getElementById('carrito');
        tbody = id.parentElement;
        tabla.removeChild(tbody);
        calcularImporteSub();
    } else {
        id.children[2].children[1].textContent = cantidad - 1;
        calcularTotal(id);
    }
}
function calcularTotal(id) {
    cantidad = id.children[2].children[1].textContent;
    cantidad = parseFloat(cantidad);
    precio = id.children[3].children[0].textContent;
    precio = parseFloat(precio);
    total = precio * cantidad;
    id.children[4].children[0].textContent = total;
    calcularImporteSub();
}
function calcularImporteSub() {
    let total = 0;
    tabla = document.getElementById('carrito');
    importe = tabla.nextElementSibling;
    hijos = tabla.children.length;
    for (i = 1; i < hijos; i++) {
        precio = parseFloat(tabla.children[i].children[0].children[4].children[0].textContent);
        if (precio != null) {
            total = total + precio;
        }
    }
    total = parseInt(total);
    importe.children[1].textContent = total;
    descuento = importe.children[3].textContent;
    descuento = parseInt(descuento);
    importe.children[5].textContent = total - descuento;

}
function consultaDetalles(id) {
    url = '/producto/' + id;
    xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.responseType = 'json';
    xhr.send();
    xhr.onload = function () {
        respuesta = xhr.response;
        console.log(typeof (respuesta));
        llenarDetalles(respuesta);
    }
}
function llenarDetalles(respuesta) {
    detalles = document.getElementById('secciondetalles');
    detalles.style.display = 'block';
    detalles.children[0].children[2].textContent = 'S/.' + respuesta.precio;
    detalles.children[0].children[4].textContent = respuesta.stock;
    detalles.children[1].children[0].children[1].children[0].children[0].children[0].src = respuesta.equipo.link;
    detalles.children[1].children[0].children[1].children[0].children[1].children[0].textContent = "Nombre: " + respuesta.equipo.nombre;
    detalles.children[1].children[0].children[1].children[0].children[1].children[2].textContent = "Descripcion: " + respuesta.equipo.descripcion;
    detalles.children[1].children[0].children[1].children[0].children[1].children[4].textContent = "Garantia: " + respuesta.equipo.garantia + ' meses';
    //detalles plan
    detallesPlan = detalles.children[1].children[1].children[0].children[1].children[0].children[0];
    detallesPlan.children[0].textContent = respuesta.equipo.plan.nombre;
    detallesPlan.children[2].textContent = 'Precio: S/.' + respuesta.equipo.plan.precio;
    detallesPlan.children[4].textContent = respuesta.equipo.plan.descripcion;
    //detalles acc
    detallesAcc = detalles.children[1].children[1].children[1].children[1].children[0].children[0];
    detallesAcc.children[0].textContent = respuesta.equipo.accesorio.nombre;
    detallesAcc.children[2].textContent = 'Precio: S /.' + respuesta.equipo.accesorio.precio;
    detallesAcc.children[4].textContent = respuesta.equipo.accesorio.descripcion;
    detallesOfer = detalles.children[1].children[1].children[2].children[1].children[0].children[0];
    detallesOfer.children[0].textContent = respuesta.oferta.nombre;
    detallesOfer.children[2].textContent = respuesta.oferta.descuento;
    detallesOfer.children[4].textContent = respuesta.oferta.descripcion;

}
function consultaProductos() {
    url = '/productos';
    xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.responseType = 'json';
    xhr.send();
    xhr.onload = function () {
        respuesta = xhr.response;
        console.log(respuesta);
    }
}
function openForm(id) {
    document.getElementById(id).style.display = "block";
}

function closeForm(id) {
    document.getElementById(id).style.display = "none";
}
function filtrarprecio() {
    // let maximo = document.getElementById(maximo).value;
    // let minimo = document.getElementById(minimo).value;
    var filas = document.getElementById('tabla');
    console.log(filas);
}
