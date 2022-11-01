create database concesionaria;

use concesionaria;

create table autos
(
	codigo   int primary key auto_increment,
	marca    VARCHAR(255),
	modelo   VARCHAR(255),
	color    VARCHAR(255),
	año     INTEGER,
	precio   DOUBLE
);                            
         
-- 2. Cargar la tabla con 15 autos.
insert into autos values
(null,'Ford','Focus','Azul',2010,250000),
(null,'Renault','Sandero','Blanco',2012,160000),
(null,'Chevrolet','Meriva','Gris',2010,170000),
(null,'Chevrolet','Corsa','Rojo',2004,90000),
(null,'Ford','Ka','Beige',2010,120000),
(null,'Renault','Duster','Blanco',2016,280000),
(null,'Ford','Galaxy','Gris',2001,85000),
(null,'Peugeot','307','Blanco',2007,100000),
(null,'Ford','Fiesta','Azul',1999,70000),
(null,'Fiat','Uno','Blanco',1998,65000),
(null,'Ford','Mondeo','Azul',2000,90000),
(null,'Fiat','Palio','Verde',2012,150000),
(null,'Ford','Falcon','Rojo',1980,50000);

select * from autos order by precio desc;

-- 3) Luego, obtener:
-- a) El precio mayor
SELECT MAX(precio) 'Mayor Precio' FROM autos;
-- b) El precio menor
SELECT min(precio) 'Menor Precio' FROM autos;

-- c) El precio menor dentro del periodo del 2000 y el 2008
SELECT min(precio) FROM autos where año between 2000 and 2008;
SELECT min(precio) FROM autos where año >= 2000 and año <= 2008;

-- d) El promedio de los precios de los autos
SELECT truncate(avg(precio),2) promedio FROM autos;

-- e) El promedio de los precios de los autos para el año 2012
SELECT truncate(avg(precio),2) promedio FROM autos where año = 2012;

-- f) La cantidad de registros de la tabla
select count(codigo) 'cantidad de autos' from autos;

-- g) La cantidad de registros de la tabla con un costo de entre 100 y 200 mil pesos
select count(codigo) 'cantidad de autos' from autos where precio between 100000 and 200000;

-- h) La cantidad de autos agrupada por cada año
select		año,
			count(codigo) 'cantidad de autos por año' 
from		autos
where		año <> 2011
group by	año
having		count(codigo) > 1
-- order by	count(codigo) desc;
order by	2 desc
limit		1;

-- where condiciona campos y filtra registros de la tabla original
-- having condiciona funciones agrupadas y filtra registros de la agrupacion

-- i) Sumarle al punto anterior el costo promedio de los autos en cada año
select		año,
			count(codigo) 'cantidad de autos por año' ,
			round(avg(precio)) as promedio
from		autos
group by	año
order by	3 desc;


-- j) La suma y el promedio de los precios de los autos por marca
select		marca,
			sum(precio) total ,
			round(avg(precio)) as promedio
from		autos
group by	marca
order by	3 desc;



































-- ejercitacion base pubs
use pubs;
-- 21. Contar la cantidad de autores que su estado de residencia sea California (CA). 
-- Poner un apodo al nombre de columna. 
select count(au_id) 'cantidad de autores' from authors;-- 23 autores

-- 22. Mostrar la fecha de inicio de facturación y el último número de comprobante emitido. 
-- Poner un apodo a cada columna. 
select	min(ord_date) 'fecha de inicio de facturación',
		max(ord_num) 'último número de comprobante'
from	sales;

-- 23.  Contar la cantidad de países que residen alguna editorial.
 select count(distinct(country)) from publishers;

-- variante(cantidad de editoriales por pais)
SELECT country 'Pais',
COUNT(pub_id) 'Cantidad de Editoriales'
FROM publishers
GROUP BY country;

-- 24. Listar las categorías de libros y el valor promedio para cada tipo de libro. 
select 		type as categoria,
			round(avg(price)) 'promedio de precio'
from 		titles
group by	type
order by	2 desc;

-- 25. ldem ejercicio 24 pero no incluir dentro de la lista los libros que no 
-- tienen decidida una categoría. 
select 		type as categoria,
			round(avg(price)) 'promedio de precio'
from 		titles
where		type != ''
group by	type
order by	2 desc;

-- 26.  Listar los locales que hayan vendido más de 100 libros.
select 		stor_id tienda,
			sum(qty) 'ventas x tienda'
from 		sales
group by	stor_id
having		sum(qty) > 100;

 
-- 27. Listar la cantidad de ejemplares vendidos de cada libro en cada tienda. Poner apodos a las columnas.
select * from sales;

select 		stor_id tienda,
			title_id titulo,
			sum(qty) 'ventas x tienda'
from 		sales
group by	stor_id,title_id
order by	stor_id;


-- 28.	  Listar el valor promedio de los libros agrupados por tipo de libro cuyo promedio esté entre 12 y 14. Poner alias a los encabezados. Ordenar la consulta por promedio. 
-- 29.	  Listar las categorías de libros junto con el precio del libro más caro, el más barato y la cantidad de libros existentes para esa categoría. Mostrar solo aquellas categorías de libros cuyo precio de los libros económicos sea inferior a $10 Y cuya cantidad de libros pertenecientes sean mayor a 2. 
-- 30.	 Contar la cantidad de empleados que trabajen en la compañía.
