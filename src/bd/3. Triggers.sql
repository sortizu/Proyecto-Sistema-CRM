/*Triggers para auditoría*/
-- 1. Registro de Clientes
USE DB_CRM_services_v3;

DROP TRIGGER IF EXISTS audit_registro_clientes;
DELIMITER || 

CREATE TRIGGER audit_registro_clientes AFTER INSERT ON DB_CRM_services_v3.Cliente FOR EACH ROW
BEGIN
    
	INSERT INTO Auditoria_Clientes (tipo_dml, fecha_y_hora_operacion, id_empleado_autor, id_cliente, 
									ruc_nuevo, num_familiares_nuevo, pasatiempo_nuevo,
                                    numDispositivos_nuevo, nse_nuevo, tiempo_servicio_nuevo) 
	VALUES ('REGISTRO', NOW(), SUBSTRING_INDEX(USER(), '@', 1), NEW.id_usuario, NEW.ruc, NEW.num_familiares, NEW.pasatiempo, 
			NEW.numDispositivos, NEW.nse, NEW.tiempo_servicio);
END
|| 
DELIMITER ;

-- 2. Modificacion de Clientes
DROP TRIGGER IF EXISTS audit_modificacion_clientes
DELIMITER || 
CREATE TRIGGER audit_modificacion_clientes AFTER UPDATE ON DB_CRM_services_v3.Cliente FOR EACH ROW
BEGIN
	INSERT INTO Auditoria_Clientes (tipo_dml, fecha_y_hora_operacion, id_empleado_autor, id_cliente, 
									ruc_nuevo, num_familiares_nuevo, pasatiempo_nuevo,
                                    numDispositivos_nuevo, nse_nuevo, tiempo_servicio_nuevo) 
	VALUES ('MODIFICACIÓN', NOW(), SUBSTRING_INDEX(USER(), '@', 1), NEW.id_usuario, NEW.ruc, NEW.num_familiares, NEW.pasatiempo, 
			NEW.numDispositivos, NEW.nse, NEW.tiempo_servicio);
END
|| 
DELIMITER ;

-- 3. Eliminacion de Clientes
DROP TRIGGER IF EXISTS audit_eliminacion_clientes
DELIMITER ||
CREATE TRIGGER audit_eliminacion_clientes AFTER DELETE ON DB_CRM_services_v3.Cliente FOR EACH ROW
BEGIN
    
	INSERT INTO Auditoria_Clientes (tipo_dml,
									fecha_y_hora_operacion,
                                    id_empleado_autor,
									id_cliente) 
	VALUES ('ELIMINACIÓN', NOW(), SUBSTRING_INDEX(USER(), '@', 1), OLD.id_usuario);
END || 
DELIMITER ;