-- subconsultas q devuelven escalares 
show tables;
-- listar todos los datos del ultimo libro publicado
select max(pubdate) from titles;

select * from titles;

select 	*
from	titles
where	pubdate = (select max(pubdate) from titles);

-- listar nombre , apellido y horas trabajadas durante 
-- un mes del empleado de menor antiguedad
describe employee;

select 	concat(fname, ' ', lname) as empleado,
		job_lvl 'cantidad de horas trabajadas'
from	employee
where	hire_date = (select max(hire_date) from employee);

-- listar nombre , apellido y telefono de los autores que publicaron
-- el libro mas caro.
select 		concat(au_fname, ' ',au_lname) as autor,
			phone telefono
from 		authors a
inner join 	titleauthor ta on ta.au_id = a.au_id 
inner join 	titles t on t.title_id = ta.title_id
where		price = (select max(price) from titles);

-- subconsultas q devuelven lista de valores
-- uso de predicados
create database comercio;

use comercio;

create table productos(numero int , precio double);
create table facturas(numero int , monto double);

insert into productos values
(1,100),(2,200),(3,300),(4,1000);

insert into facturas values
(1,300),(2,500),(3,600),(4,200);

select * from productos;
select * from facturas;

-- listar todos los productos cuyo precio supere todos los montos facturados.
select	*
from	productos
where	precio > all (select monto from facturas);

-- listar todos los productos cuyo precio supere a cualquier  monto facturado.
select	*
from	productos
where	precio > any (select monto from facturas);

-- listar todos los productos cuyo precio coincida con un monto facturado.
select	*
from	productos
-- where	precio = any (select monto from facturas);
where	precio in (select monto from facturas);

-- listar todos los productos cuyo precio coincida con un monto facturado.
select	*
from	productos
-- where	precio <> all (select monto from facturas);
where	precio not in (select monto from facturas);

-- ejercitacion base pubs
-- 41.	Listar el nombre de los libros junto a su categoría de precio. 
-- La categoría de precio se calcula de la siguiente manera: Si el precio 
-- está entre 0 y 10 la categoría es Económica. Si la categoría está entre 
-- 10 Y 20, Normal y si su valor es mayor a 20 la categoría es Caro. Colocar 
-- un apodo a las dos columnas. 
select	title libro,
		price precio,
        case
			when price < 10 then 'Economica'
            when price between 10 and 20 then 'Normal'
            when price > 20 then 'Cara'
        end as categoria
from	titles;



-- 49.	Mostrar el nombre de los libros junto a su categoría de precio de 
-- aquellos libros que son categorizados como "Normal". La categoría de los 
-- precios es la misma del ejercicio 41
SELECT	*
FROM	(
			select	title libro,
					price precio,
					case
						when price < 10 then 'Economica'
						when price between 10 and 20 then 'Normal'
						when price > 20 then 'Cara'
					end as categoria
			from	titles
		) as miTabla
WHERE	miTabla.categoria = 'Normal';









 












