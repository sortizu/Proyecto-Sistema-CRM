CREATE DATABASE atencion_cliente;
USE atencion_cliente;

DROP TABLE if EXISTS cliente;
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    
	 id_usuario INT,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasenia VARCHAR(50) NOT NULL,
    fecha_creacion DATE,
    apellido_paterno VARCHAR(50) NOT NULL,
    apellido_materno VARCHAR(50) NOT NULL,
    genero VARCHAR(10) NOT NULL,
    direccion VARCHAR(200),
    ubigeo VARCHAR(6) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    dni VARCHAR(8) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(9) NOT NULL,
    
    ruc  VARCHAR(11),
    servicio_cliente VARCHAR(100) NOT NULL,
    num_familiares INT,
    servicio_familiar VARCHAR(50),
    pasatiempo VARCHAR(50),
    num_dispositivos INT,
    nivel_socioeconomico VARCHAR(1),
    proveedor_anterior VARCHAR(50),
    tiempo_servicio  VARCHAR(100)
);

SELECT * from cliente;
INSERT INTO cliente( nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno, genero, direccion, ubigeo, 
							nacionalidad, fecha_nacimiento, dni, email, telefono,  ruc, servicio_cliente, num_familiares, servicio_familiar,
							 pasatiempo, num_dispositivos, nivel_socioeconomico, proveedor_anterior, tiempo_servicio) 
VALUES( 'ssSergio Francisco', '123456789', NOW(), 'Ruiz', 'Cortez', 'Masculino', 'Av. Callao 1546', '141226',
		'Peruana', '2001-02-12','49181534', 'cortez.sergio@gmail.com', '959766301','98745632198', 'Telefonia prepago', 2, 'telefonia fija',
		'No precisa', 2, 'C', 'Movistar', '2 meses');
/*
INSERT INTO cliente( nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno, genero, direccion, ubigeo, 
							nacionalidad, fecha_nacimiento, dni, email, telefono,  ruc, servicio_cliente, num_familiares, servicio_familiar,
							 pasatiempo, num_dispositivos, nivel_socioeconomico, proveedor_anterior, tiempo_servicio) 
VALUES( 'Carlos Ernesto', 'micontrasenia', '2000-05-25', 'Rojas', 'Paredes', 'Masculino', 'Urb Girasoles Callao', '101546',
		'Peruana', '2000-05-25','08164975', 'carlos.rojas@gmail.com', '989744612','12345678935', 'Telefonia postpago', 2, 'telefonia fija',
		'Videojuegos', 5, 'B', 'Claro', '20 meses');

SELECT * from cliente;

INSERT INTO cliente( nombre_usuario, contrasenia, fecha_creacion, apellido_paterno, apellido_materno, genero, direccion, ubigeo, 
							nacionalidad, fecha_nacimiento, dni, email, telefono,  ruc, servicio_cliente, num_familiares, servicio_familiar,
							 pasatiempo, num_dispositivos, nivel_socioeconomico, proveedor_anterior, tiempo_servicio) 
VALUES( 'ssSergio Francisco', '123456789', NOW(), 'Ruiz', 'Cortez', 'Masculino', 'Av. Callao 1546', '141226',
		'Peruana', '2001-02-12','49181534', 'cortez.sergio@gmail.com', '959766301','98745632198', 'Telefonia prepago', 2, 'telefonia fija',
		'No precisa', 2, 'C', 'Movistar', '2 meses');

SELECT * from cliente;

SELECT * from cliente WHERE id=2;
REPLACE INTO cliente VALUES (2,'49481564','Marco Antonio', 'Soza Guerra', 'Av. colonial', '2011-05-25','916544612','015297434',
 'juan.soza@gmail.com', 'telefonia movil prepago');
 
SELECT * from cliente;
SELECT * from cliente WHERE dni= 08164975;*/