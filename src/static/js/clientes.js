/*Funcionalidades especificas del modulo de clientes*/
function registrarCliente(){
    var dni=document.getElementById("R-DNI").value;
    var nombre=document.getElementById("R-NOMBRE").value;
    var apellidoP=document.getElementById("R-APP").value;
    var apellidoM=document.getElementById("R-APM").value;
    var genero=document.getElementById("R-GENERO").value;
    var fechaNacimiento=document.getElementById("R-FN").value;
    var nacionalidad=document.getElementById("R-NAC").value;
    var email=document.getElementById("R-EMAIL").value;
    var telefono=document.getElementById("R-TEL").value;
    var direccion1=document.getElementById("R-DIR1").value;
    var direccion2=document.getElementById("R-DIR2").value;
    var ruc=document.getElementById("R-RUC").value;
    var numeroFamiliares=document.getElementById("R-NFAM").value;
    var pasatiempo=document.getElementById("R-PASAT").value;
    var numeroDispositivos=document.getElementById("R-NDISP").value;
    var nivelSoc=document.getElementById("R-NSOC").value;
    var nombreUsuario=document.getElementById("R-NOMBREUSUARIO").value;
    var contraseña=document.getElementById("R-CONTRASEÑA").value;
    if(dni){
        if(nombre){
            if(apellidoP && apellidoM){
                if(nombreUsuario&&contraseña){
                    $.ajax({
                        url:'/clientes/ejecutarRegistro',
                        type: 'POST',
                        data:{
                            dni: dni,
                            nombre: nombre,
                            ApellidoP: apellidoP,
                            ApellidoM: apellidoM,
                            genero: genero,
                            fechaNacimiento: fechaNacimiento,
                            nacionalidad: nacionalidad,
                            email: email,
                            telefono: telefono,
                            direccion1: direccion1,
                            direccion2: direccion2,
                            ruc: ruc,
                            numeroFamiliares: numeroFamiliares,
                            pasatiempo: pasatiempo,
                            numeroDispositivos: numeroDispositivos,
                            nivelSoc: nivelSoc,
                            nombreUsuario: nombreUsuario,
                            contraseña: contraseña
                        },
                        success: function(response){
                            window.alert("Se ha registrado el cliente correctamente.")
                        },
                        error: function(response){
                            window.alert("Algo ha salido mal.\nNo se pudo registrar al cliente")
                        }
                    })
                }else{
                    window.alert("Debe ingresar las credenciales del cliente")
                }
            }else{
                window.alert("Debe ingresar ambos apellidos")
            }   
        }else{
            window.alert("Debe ingresar un nombre")
        }
    }else{
        window.alert("Debe ingresar un dni")
    }
    
}

function buscarCliente(){
    cargarPanel("DATOSDECLIENTE1")
}
function eliminarCliente(){

}
function exportarReporte(){
}
function generarReporte(){
}