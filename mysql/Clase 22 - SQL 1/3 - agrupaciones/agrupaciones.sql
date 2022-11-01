-- funciones de agrupacion o agregacion

use pubs;

select * from employee;

-- cuento registros nulos y NO nulos
select 	count(*) as 'cantidad de empleados' 
from 	employee;-- *: cuenta nulos y no nulos

-- cuento registros NO nulos
select 	count(emp_id) as 'cantidad de empleados' 
from 	employee;-- cuando ponemos un campo dentro de la funcion count --> cuenta no nulos!


-- listo todos los campos de la tabla de titulos
select * from titles;

-- listar todos los titulos que tengo
select 	count(*) 
from 	titles;-- 19 registros

-- listar todos los titulos no nulos en el precio
select 	count(price) 
from 	titles;-- 16 registros

-- totalizar la columna de precio de los libros
select truncate(sum(price),3) as total from titles;


-- selecciono la base negocio
use negocio;


select * from productos;

-- veo la estructura de la tabla productos
describe productos;

-- contar productos de stock = 10
select 	count(idproducto) 'cantidad de productos con stock de 10' 
from 	productos
where	stock = 10;



use pubs;

-- informar la mayor cantidad de horas trabajadas por un empleado
-- job_lvl(nivel de trabajo): cantidad de horas trabajadas durante un mes
select 	max(job_lvl) as 'mayor cantidad de horas trabajadas'
from	employee;-- 127 horas

-- informar la menor cantidad de horas trabajadas por un empleado
select 	min(job_lvl) as 'menor cantidad de horas trabajadas'
from	employee;-- 30 horas

-- promedio general de ventas
-- avg: average(promedio)
-- qty: cantidad de ventas por titulo
select  avg(qty) from sales;

-- promedio de precios de todos los titulos
select round(avg(price),2) 'promedio de precios' from titles;

-- informar el promedio de horas trabajadas por todos los empleados
select 	avg(job_lvl) as 'promedio de horas trabajadas'
from	employee;

-- integro las funciones agrupadas en una unica consulta(query)
select	max(price) as maximo,
		min(price) minimo,
		round(avg(price),2) promedio,
		count(title_id) maximo,
		round(sum(price),2) total
from	titles;



-- Agrupaciones
-- listar la cantidad de titulos no nulos por categoria de libro 
select 		type as categoria,
			count(title_id) 'cantidad de titulos'
from 		titles
group by	type;

-- listar la cantidad de titulos por categoria de libro q no sean de deporte
select 		type as categoria,
			count(title_id) 'cantidad de titulos'
from 		titles
where		type  not like '%sport%'
group by	type;

-- listar la cantidad de titulos por categoria de libro
-- que sean mayor a 2 ordenados por cantidad en forma descendente
-- y que no sean de deporte
select 		type as categoria,
			count(title_id) 'cantidad de titulos'
from 		titles
where		type  not like '%sport%'
group by	type
having		count(title_id) > 2
-- order by	count(title_id) desc;
order by	2 desc -- 2 es el nro de columna del SELECT(en este caso, count(title_id))
limit		3;

-- CUANDO DEBO AGRUPAR?
-- cuando en las columnas del SELECT mezclo campos con funciones agrupadas. Entonces
-- debo obligatoriamente agrupar por los campos

-- DIFERENCIA ENTRE HAVING y where:
-- WHERE: filtra registros de la tabla original, condicionando campos.
-- HAVING: filtra registros de una agrupacion, condicionando funciones agrupadas.










