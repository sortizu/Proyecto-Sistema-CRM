use crm_ventas;

create table accesorio (
	id_accesorio int unsigned primary key,
    nombre varchar(100) not null,
    precio decimal(6,2) not null,
    stock int not null,
    descripcion varchar(100) not null
);

insert into accesorio(id_accesorio,nombre,precio,stock,descripcion)
select id_acc,nombre_acc,precio_acc,stock_acc,descripcion_acc
from v3crm
where id_acc is not null
group by nombre_acc;

create table plan (
	id_plan int unsigned primary key not null,
    nombre varchar(100) not null,
    precio decimal(5,2) not null,
    descripcion varchar(200) not null
);

insert into plan(id_plan,nombre,descuento,descripcion)
select id_pl,nombre_pl,replace(precio_pl,',','.'),descripcion_pl
from v3crm
where id_pl is not null
group by nombre_pl;

create table equipo (
	id_equipo int unsigned primary key,
    nombre varchar(100) not null,
    precio decimal(6,2) not null,
    stock int not null,
    fk_equipo_plan int unsigned not null,
    fk_equipo_accesorio int unsigned null,
    descripcion varchar(400) not null,
    garantia int not null,
    link varchar(100) not null,
    foreign key (fk_equipo_plan) references plan(id_plan)
    on delete cascade on update cascade,
    foreign key (fk_equipo_accesorio) references accesorio(id_accesorio)
    on delete cascade on update cascade
);

insert into equipo(id_equipo,nombre,precio,stock,fk_equipo_plan,fk_equipo_accesorio,descripcion,garantia,link)
select id_eq,nombre_eq,replace(precio_eq,',','.'),stock_eq,id_pl,id_acc,descripcion_eq,grarantia,concat("../static/resources/images/producto/",id_eq,".png")
from v3crm
group by nombre_eq;

create table oferta (
	id_oferta int unsigned primary key,
    nombre varchar(30) not null,
    descuento decimal(5,2) not null,
    descripcion varchar(100) not null
);

insert into oferta(id_oferta,nombre,descuento,descripcion)
select id_of,nombre_of,replace(descuento_of,',','.'),descripcion_of
from v3crm
where id_of is not null
group by nombre_of;

create table producto (
	id_producto int unsigned primary key,
    fk_producto_equipo int unsigned not null,
    fk_producto_oferta int unsigned,
    nombre varchar(200) not null,
    precio decimal(6,2) not null,
    stock int not null,
    descripcion varchar(600) not null,
    foreign key (fk_producto_equipo) references equipo(id_equipo)
    on delete cascade on update cascade,
	foreign key (fk_producto_oferta) references oferta(id_oferta)
    on delete cascade on update cascade
);

insert into producto(id_producto,fk_producto_equipo,fk_producto_oferta,nombre,precio,stock,descripcion)
select N,id_eq,id_of,nombre_pr,replace(precio_pr,',','.'),stock_pr,descripcion_pr
from v3crm
where N is not null
group by nombre_pr;

create table marca (
	id_marca int unsigned auto_increment primary key,
    nombre varchar(30) not null
);

insert into marca(nombre)
select substring_index(nombre," ",1) marca
from crm_ventas.equipo
group by marca
order by marca;