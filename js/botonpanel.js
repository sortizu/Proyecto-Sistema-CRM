/*Aqui se definen las funciones generales que ejecutaran los botones
dentro de los paneles*/
function cargarPanel(panelID){
    limpiarPantalla()
    const nuevoPanel = document.getElementById(panelID)
    nuevoPanel.style.display="block"
}

