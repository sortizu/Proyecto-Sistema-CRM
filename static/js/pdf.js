

// Default export is a4 paper, portrait, using millimeters for units
var doc = new jsPDF();
var logo = new Image();
logo.src = '../resources/images/logo_pagina.png';
console.log("funciona");
doc.addImage(logo, 'PNG', 15, 40, 148, 210);
doc.text("Hello world!", 10, 10);
doc.save("a4.pdf");