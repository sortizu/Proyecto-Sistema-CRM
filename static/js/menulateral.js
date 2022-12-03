/*Este codigo se encarga de darle el formato al menu lateral
ademas le permite abrir los paneles correspondientes a una 
funcionalidad*/
const btn=document.getElementsByClassName("BTNMENULATERAL")
Array.from(btn).forEach(function(element){
    if(element.getAttribute("panel")!=null)
        element.addEventListener("click",mostrarPanel)
})
/*Funcion para cargar un panel inicial para los botones del
menu lateral*/
function mostrarPanel(){
    actualizarMenuLateral(this)
    limpiarPantalla()
    const panel = document.getElementById(this.getAttribute("panel"))
    panel.style.display="block"
}

function actualizarMenuLateral(elemento){
    const btn=document.getElementsByClassName("BTNMENULATERAL")
    Array.from(btn).forEach(function(element){
        if(element.getAttribute("panel")!=null){
            element.style.color="#888888"
            element.style.backgroundColor="white"
        }
    })
        elemento.style.color="white"
        elemento.style.backgroundColor="purple"
}

function limpiarPantalla(){
    const paneles=document.getElementsByClassName("PANEL")
    Array.from(paneles).forEach(function(element){
        element.style.display="none"
    })
}