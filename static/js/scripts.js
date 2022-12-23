document.addEventListener("click", e => {
    if (e.target.getAttribute("name") == "detalles") {
        tr = e.target.parentElement.parentElement;
        th = tr.parentElement;
        consultaDetalles(th.getAttribute('id'));

    }

})

function consultaDetalles(id) {
    url = '/producto/' + id;
    xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.responseType = 'json';
    xhr.send();
    xhr.onload = function () {
        respuesta = xhr.response;
        llenarDetalles(respuesta);
    }
}
function llenarDetalles(respuesta) {
    console.log(respuesta);
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
    console.log(filas);}
