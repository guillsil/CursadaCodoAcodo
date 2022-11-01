-- create database Agrupacionesclientes;
create database Agrupacionesclientes;

use Agrupacionesclientes;

-- Creación de la tabla clientes:

 create table clientes(
  nombre varchar(30),
  edad tinyint unsigned,
  sexo char(1),
  domicilio varchar(30),
  ciudad varchar(20),
  telefono varchar(11),
  montocompra decimal (6,2) unsigned
 );

-- Ingreso de registros:

 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Susana Molina', 28,'f','Colon 123','Cordoba',null,45.50); 
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Marcela Mercado',36,'f','Avellaneda 345','Cordoba','4545454',0);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Alberto Garcia',35,'m','Gral. Paz 123','Alta Gracia','03547123456',25); 
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Teresa Garcia',33,'f','Gral. Paz 123','Alta Gracia','03547123456',0);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Roberto Perez',45,'m','Urquiza 335','Cordoba','4123456',33.20);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Marina Torres',22,'f','Colon 222','Villa Dolores','03544112233',25);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Julieta Gomez',24,'f','San Martin 333','Alta Gracia','03547121212',53.50);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Roxana Lopez',20,'f','Triunvirato 345','Alta Gracia',null,0);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Liliana Garcia',50,'f','Paso 999','Cordoba','4588778',48);
 insert into clientes (nombre,edad, sexo,domicilio,ciudad,telefono,montocompra)
  values ('Juan Torres',43,'m','Sarmiento 876','Cordoba','4988778',15.30);
  
-- Consultamos todos los registros:
  select * from clientes;

-- 1- Informar la cantidad de clientes por ciudad
select 		ciudad,
			count(nombre) 'cantidad de clientes x ciudad'
from		clientes
group by	ciudad;

-- 2- Cantidad de clientes por ciudad, que no sean de Villa Dolores
select 		ciudad,
			count(nombre) 'cantidad de clientes x ciudad'
from		clientes
where		ciudad <> 'Villa Dolores'-- <> significa distinto, es lo mismo que poner !=
group by	ciudad;

-- 3- Cual es la cantidad de clientes con teléfono no nulo, de cada ciudad, ordenados por ciudad en 
-- forma alfabética:
select 		ciudad,
			count(nombre) 'cantidad de clientes x ciudad'
from		clientes
where		telefono is not null
group by	ciudad
order by	ciudad  asc;-- asc: de la A a la Z

-- 4- Informar el total de las compras agrupadas por sexo:
select 		sexo,
			sum(montocompra) as 'total de compras'
from		clientes
group by	sexo;

-- 5- Obtener el máximo y mínimo valor de compra agrupados por sexo:
select 		sexo,
			min(montocompra) as minimo,
			max(montocompra) as maximo
from		clientes
group by	sexo;

-- 6- Informar el promedio del valor de compra (redondeado a 2 decimales) agrupados por ciudad 
-- (No incluir a la ciudad de La Falda) cuyo promedio sea superior a 20 $. Ordenar por promedio en 
-- forma descendente:
select 		ciudad,
			round(avg(montocompra),2) as promedio
from		clientes
where		ciudad <> 'La Falda'
group by	ciudad
having		promedio > 20;-- en el having puedo usar el alias de columna


-- 7- Informar la cantidad de clientes que no residan en la ciudad de Córdoba, ordenados por cantidad 
-- de clientes, de mayor a menor:
SELECT 	ciudad,
		COUNT(nombre) 'Cantidad de Clientes'
FROM 	clientes
WHERE 	ciudad NOT LIKE '%cordoba%'
GROUP BY ciudad
-- ORDER BY 'Cantidad de Clientes' DESC;
ORDER BY COUNT(nombre) DESC;


-- diferencia round y truncate
/*
	valor original: 12,374
	truncate a 2 decimales -->  12,37
	redondeo a 2 decimales -->  12,37 --> de 0-4 redondea para abajo y de 5-9 redondea para arriba

	valor original: 12,378
	truncate a 2 decimales -->  12,37
	redondeo a 2 decimales -->  12,38

*/


