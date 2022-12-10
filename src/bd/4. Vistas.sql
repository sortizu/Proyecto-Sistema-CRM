USE db_crm_services_v3;

/*Vista para visualizar los datos de la propia tabla Cliente y de la tabla Usuario*/
DROP VIEW IF EXISTS data_general_cliente;
CREATE VIEW data_general_cliente
AS
	SELECT
    u.*,
    cl.ruc,
    cl.num_familiares,
    cl.pasatiempo,
    cl.numDispositivos,
    cl.nse,
    cl.tiempo_servicio
    FROM Cliente cl
    INNER JOIN Usuario u ON cl.id_usuario = u.dni;
    
SELECT * FROM data_general_cliente;
