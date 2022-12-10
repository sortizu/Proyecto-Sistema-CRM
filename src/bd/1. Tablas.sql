DROP DATABASE IF EXISTS DB_CRM_services_v3;
CREATE DATABASE DB_CRM_services_v3;

USE DB_CRM_services_v3;
    
CREATE TABLE Usuario(
	dni VARCHAR(16) NOT NULL PRIMARY KEY,
    nombre_usuario VARCHAR(32) NOT NULL,
    contraseña varchar(20) NOT NULL,
    nombre varchar(50) NOT NULL,
    apellido_paterno VARCHAR(32) NOT NULL,
    apellido_materno VARCHAR(32) NOT NULL,
    fecha_creacion DATE NOT NULL,
    genero TINYINT, -- 0: Femenino, 1: Masculino
    direccion_1 VARCHAR(64),
    direccion_2 VARCHAR(64),
    nacionalidad VARCHAR(32),
    fecha_nacimiento DATE,
    email VARCHAR(32) UNIQUE,
    telefono VARCHAR(32) UNIQUE
);

CREATE TABLE Cliente(
	id_usuario VARCHAR(16) NOT NULL UNIQUE,
    ruc VARCHAR(32) UNIQUE,
    num_familiares INT,
    pasatiempo VARCHAR(64),
    numDispositivos TINYINT UNSIGNED,
    nse VARCHAR(1),
    tiempo_servicio INT UNSIGNED
);

ALTER TABLE Cliente
	ADD CONSTRAINT fk_cliente_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario (dni) ON DELETE CASCADE;
    
CREATE TABLE Empleado(
	id_usuario VARCHAR(16) NOT NULL UNIQUE,
    sueldo FLOAT NOT NULL,
    rango VARCHAR(16) NOT NULL,
    tiempo_contratacion INT NOT NULL,
    fecha_contratacion DATE NOT NULL
);

ALTER TABLE Cliente
	ADD CONSTRAINT fk_empleado_usuario FOREIGN KEY (id_usuario) REFERENCES Usuario (dni) ON DELETE CASCADE;

CREATE TABLE Auditoria_Clientes(
	operacionID INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    tipo_dml VARCHAR(32) NOT NULL, -- INSERCIÓN, ELIMINACIÓN O MODIFICACIÓN
    fecha_y_hora_operacion DATETIME,
    id_empleado_autor VARCHAR(32) NOT NULL,
    id_cliente VARCHAR(16),
    ruc_nuevo VARCHAR(32),
    num_familiares_nuevo TINYINT,
    pasatiempo_nuevo VARCHAR(64),
    numDispositivos_nuevo TINYINT UNSIGNED,
    nse_nuevo VARCHAR(1),
    tiempo_servicio_nuevo INT UNSIGNED
);
CREATE TABLE Auditoria(
	id_auditoria INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nombre_valor VARCHAR(45) NOT NULL,
    valor_anterior VARCHAR(45) NOT NULL,
    nuevo_valor VARCHAR(45) NOT NULL,
    fecha_modificacion DATETIME NOT NULL,
    id_cliente VARCHAR(16),
    id_empleado VARCHAR(16)
);
ALTER TABLE Auditoria
	ADD CONSTRAINT fk_auditoria_cliente FOREIGN KEY (id_cliente) REFERENCES Usuario (dni) ON DELETE CASCADE;
ALTER TABLE Auditoria
	ADD CONSTRAINT fk_auditoria_empleado FOREIGN KEY (id_empleado) REFERENCES Usuario (dni) ON DELETE CASCADE;
    select * from Usuario;
    select * from Cliente;
    select * from Auditoria_Clientes;