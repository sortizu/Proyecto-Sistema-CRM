/*Creacion de usuarios*/
USE DB_CRM_services_v3;

DROP USER IF EXISTS 'oalex.rs'@'localhost', 'sebastian.ou'@'localhost', 'frankj.lv2'@'localhost', 'jluis.m2'@'localhost', 'yeysons.c2'@'localhost';
CREATE USER 'oalex.rs'@'localhost' IDENTIFIED BY 'fisi202';
CREATE USER 'sebastian.ou'@'localhost' IDENTIFIED BY 'fisi202';
CREATE USER 'frankj.lv2'@'localhost' IDENTIFIED BY 'fisi202';
CREATE USER 'jluis.m2'@'localhost' IDENTIFIED BY 'fisi202';
CREATE USER 'yeysons.c2'@'localhost' IDENTIFIED BY 'fisi202';

/*Asignacion de permisos*/
GRANT ALL PRIVILEGES ON DB_CRM_services_v3.* TO 'oalex.rs'@'localhost';
GRANT CREATE, SELECT, DELETE, INSERT, CREATE, UPDATE, TRIGGER ON DB_CRM_services_v3.* 
	TO 'sebastian.ou'@'localhost', 'frankj.lv2'@'localhost', 'jluis.m2'@'localhost', 'yeysons.c2'@'localhost';