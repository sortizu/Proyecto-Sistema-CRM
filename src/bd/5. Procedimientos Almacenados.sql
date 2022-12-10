USE db_crm_services_v3;

/*******--------Métodos de AgenteAtenciónCliente--------*******/
/*Registro de solo usuarios*/
DROP PROCEDURE IF EXISTS SP_registro_usuarios;

DELIMITER ||
CREATE PROCEDURE SP_registro_usuarios (IN v_dni VARCHAR(16), IN v_nombre_usuario VARCHAR(32), IN v_apellido_paterno VARCHAR(32),
									   IN v_apellido_materno VARCHAR(32), IN v_genero TINYINT, IN v_direccion_1 VARCHAR(64),
                                       IN v_direccion_2 VARCHAR(64), IN v_nacionalidad VARCHAR(32), IN v_fecha_nacimiento DATE,
                                       IN v_email VARCHAR(32), IN v_telefono VARCHAR(32))
BEGIN
	INSERT INTO Usuario (dni, nombre_usuario, apellido_paterno, apellido_materno, fecha_creacion, genero, direccion_1, direccion_2, nacionalidad,
							fecha_nacimiento, email, telefono)
	VALUES (v_dni, v_nombre_usuario, v_apellido_materno, NOW(), v_genero, v_direccion_1, v_direccion_2, v_nacionalidad, v_fecha_nacimiento,
			v_email, v_telefono);
END;
||
 -- Ejecución del procedimiento
/*CALL SP_registro_usuarios ([v_dni], [v_nombre_usuario], [v_apellido_paterno],
						[v_apellido_materno], [v_genero], [v_direccion_1],
					   [v_direccion_2], [v_nacionalidad], [v_fecha_nacimiento],
					   [v_email] , [v_telefono])*/

/*Registro de cliente*/
DROP PROCEDURE IF EXISTS SP_registro_clientes;

DELIMITER ||
CREATE PROCEDURE SP_registro_clientes (IN v_dni VARCHAR(16), IN v_nombre_usuario VARCHAR(32), IN v_apellido_paterno VARCHAR(32),
									   IN v_apellido_materno VARCHAR(32), IN v_genero TINYINT, IN v_direccion_1 VARCHAR(64),
                                       IN v_direccion_2 VARCHAR(64), IN v_nacionalidad VARCHAR(32), IN v_fecha_nacimiento DATE,
                                       IN v_email VARCHAR(32), IN v_telefono VARCHAR(32), IN v_ruc VARCHAR(32), IN v_num_familiares TINYINT,
                                       IN v_pasatiempo VARCHAR(64), IN v_numDispositivos TINYINT, IN v_nse VARCHAR(1), IN v_tiempo_servicio INT)
BEGIN
	INSERT INTO Usuario (dni, nombre_usuario, apellido_paterno, apellido_materno, fecha_creacion, genero, direccion_1, direccion_2, nacionalidad,
							fecha_nacimiento, email, telefono)
	VALUES (v_dni, v_nombre_usuario, v_apellido_materno, NOW(), v_genero, v_direccion_1, v_direccion_2, v_nacionalidad, v_fecha_nacimiento,
			v_email, v_telefono);
            
	INSERT INTO Cliente (id_usuario, ruc, num_familiares, pasatiempo, numDispositivos, nse, tiempo_servicio)
		VALUES (v_dni, v_ruc, v_num_familiares, v_pasatiempo, v_numDispositivos, v_nse, v_tiempo_servicio);
END;
||
 -- Ejecución del procedimiento
/*CALL SP_registro_clientes ([v_dni], [v_nombre_usuario], [v_apellido_paterno],
						[v_apellido_materno], [v_genero], [v_direccion_1],
					   [v_direccion_2], [v_nacionalidad], [v_fecha_nacimiento],
					   [v_email] , [v_telefono], [v_ruc] , [v_num_familiares],
					   [pasatiempo] , [v_numDispositivos], [v_nse], [v_tiempo_servicio])*/
                       
/*ACTUALIZAR CLIENTE*/
DROP PROCEDURE IF EXISTS SP_actualizar_cliente;

DELIMITER ||
CREATE PROCEDURE SP_actualizar_cliente (IN v_dni VARCHAR(16), IN v_ruc VARCHAR(32), IN v_num_familiares TINYINT,
										IN v_pasatiempo VARCHAR(64), IN v_numDispositivos TINYINT, IN v_nse VARCHAR(1),
                                        IN v_tiempo_servicio INT)
BEGIN
	UPDATE Cliente SET ruc = v_ruc, num_familiares = v_num_familiares, pasatiempo = v_pasatiempo, numDispositivos = v_numDispositivos,
						nse = v_nse, tiempo_servicio = v_tiempo_servicio
	WHERE id_usuario = v_dni;
END;
||

/*BUSCAR CLIENTE*/
/*Busca un cliente por su DNI*/
DROP PROCEDURE IF EXISTS SP_busqueda_cliente;

DELIMITER ||
CREATE PROCEDURE SP_busqueda_cliente (IN v_dni VARCHAR(16))
BEGIN
	SELECT * FROM data_general_cliente WHERE dni = v_dni;
END;
||

