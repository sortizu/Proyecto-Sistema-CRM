CREATE DATABASE atencion_cliente;
USE atencion_cliente;

DROP TABLE if EXISTS cliente;
CREATE TABLE cliente (
    id INT AUTO_INCREMENT,
    nombreCliente VARCHAR(50) NOT NULL,
    apellidoCliente  VARCHAR(50) NOT NULL,
    direccion VARCHAR(200),
	 natalicio DATE,
	 telefonoCel VARCHAR(9) NOT NULL,
	 telefonoFijo VARCHAR(9),
	 email VARCHAR(100),
	 servicioAdquirido VARCHAR(100) NOT NULL,	 
    PRIMARY KEY (id)
);

INSERT INTO cliente(nombreCliente, apellidoCliente, direccion,natalicio,telefonoCel,telefonoFijo, email, servicioAdquirido) 
VALUES('Carlos Ernesto', 'Rojas Paredes', 'Urb Girasoles Callao', '2000-05-25','989744612','015697412', 'carlos.rojas@gmail.com', 'telefonia movil prepago');

SELECT * from cliente;