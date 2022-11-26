use crm_ventas;

create table oferta (
	id_oferta int unsigned auto_increment primary key,
    nombre varchar(30),
    descuento decimal(5,2),
    descripcion varchar(100)
);

create table accesorio (
	id_accesorio int unsigned auto_increment primary key,
    nombre varchar(30),
    precio decimal(5,2),
    stock int,
    descripcion varchar(100)
);

create table plan (
	id_plan int unsigned auto_increment primary key,
    nombre varchar(30),
    descuento decimal(5,2),
    descripcion varchar(100)
);

create table cliente (
	id_cliente int unsigned auto_increment primary key,
    nombre varchar(30),
    dni varchar(8),
    email varchar(100),
    datos_pago varchar(100)
);

create table vendedor (
	id_vendedor int unsigned auto_increment primary key,
    usuario varchar(20),
    contraseña varchar(30),
    nombre varchar(30)
);


#-----------------------tablas con llaves foraneas--------------------------

create table equipo (
	id_equipo int unsigned auto_increment primary key,
    nombre varchar(30),
    precio decimal(5,2),
    stock int,
    fk_equi_plan int unsigned not null,
    fk_equi_acces int unsigned not null,
    descripcion varchar(100),
    garantia int,
    foreign key (fk_equi_plan) references plan(id_plan)
    on delete cascade on update cascade,
    foreign key (fk_equi_acces) references accesorio(id_accesorio)
    on delete cascade on update cascade
);

create table producto (
	id_producto int unsigned, #auto_increment primary key,
    fk_producto_equipo int unsigned,# not null,
    fk_producto_oferta int unsigned,# not null,
    nombre varchar(30),
    precio decimal(5,2),
    stock int,
    descripcion varchar(800)
   # foreign key (fk_producto_equipo) references equipo(id_equipo)
  #  on delete cascade on update cascade,
  #  foreign key (fk_producto_oferta) references oferta(id_oferta)
   # on delete cascade on update cascade
);

insert into crm_ventas.producto (id_producto,fk_producto_equipo,fk_producto_oferta,nombre,precio,stock,descripcion)
SELECT *
FROM crm_ventas.pr pr

insert into crm_ventas.producto (nombre,precio,stock)
SELECT p.id_producto as id_producto,(concat(e.nombre,' + ',pl.nombre,if(o.nombre IS NULL OR o.nombre = '','',' + '),o.nombre)) as nombre, round(((e.precio + pl.precio)*(1-o.descuento)),1) as precio, e.stock as stock
FROM crm_ventas.producto p, crm_ventas.equipo e, crm_ventas.oferta o, crm_ventas.plan pl
where p.fk_producto_oferta = o.id_oferta
	and p.fk_producto_equipo = e.id_equipo
	and e.fk_equipo_plan = pl.id_plan
order by p.id_producto

alter table producto 
	add foreign key (fk_producto_equipo) references equipo(id_equipo) on update cascade on delete cascade,
	add foreign key (fk_producto_oferta) references oferta(id_oferta) on update cascade on delete cascade;

create table boleta (
	id_boleta int unsigned auto_increment primary key,
    fk_bol_cliente int unsigned not null,
    fk_bol_vendedor int unsigned not null,
    fk_bol_venta int unsigned not null,
    descripcionLocal varchar(100),
    descripcionBoleta varchar(100)
);

create table venta (
	id_venta int unsigned auto_increment primary key,
    monto_venta decimal(5,2),
    fecha date,
    fk_venta_vendedor int unsigned not null,
    fk_venta_cliente int unsigned not null,
    descripcion varchar(100),
    forma_pago varchar(100),
    fk_venta_boleta int unsigned not null,
    foreign key (fk_venta_vendedor) references vendedor(id_vendedor)
    on delete cascade on update cascade,
    foreign key (fk_venta_cliente) references cliente(id_cliente)
    on delete cascade on update cascade,
    foreign key (fk_venta_boleta) references boleta(id_boleta)
    on delete cascade on update cascade
);

create table detalle_venta (
	id_detalle int unsigned auto_increment primary key,
    fk_det_producto int unsigned not null,
    fk_det_venta int unsigned not null,
    precio_venta decimal(5,2),
    cantidad int,
    foreign key (fk_det_producto) references producto(id_producto)
    on delete cascade on update cascade,
    foreign key (fk_det_venta) references venta(id_venta)
    on delete cascade on update cascade
);

#llaves foraneas de boleta
alter table boleta 
	add foreign key (fk_bol_cliente) references cliente(id_cliente) on update cascade on delete restrict,
	add foreign key (fk_bol_vendedor) references vendedor(id_vendedor) on update cascade on delete restrict, 
	add foreign key (fk_bol_venta) references venta(id_venta) on update cascade on delete restrict;