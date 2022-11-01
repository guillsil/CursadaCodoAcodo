-- Consultas relacionadas 
use pubs;
-- 31.Seleccionar todos los libros junto a todos los datos 
-- de la editorial la cual lo publicó. Es una coincidencia
-- entonces, uso inner join 
select		*
from		titles as t 
inner join	publishers p
on			t.pub_id = p.pub_id;-- muestra todos los campos de ambas tablas. Como puse * 
-- en el Select entonces primero muestra los campos de titles y luego de publishers


-- 32 Mostrar el nombre del libro y el nombre de la editorial 
-- la cual lo publicó sólo de las editoriales que tengan 
-- residencia en USA. Mostrar un apodo para cada columna. 
select		t.title as libro,
			p.pub_name editorial,
			p.country as pais -- para verificar que son de USA
from		titles t
inner join	publishers p
on			t.pub_id = p.pub_id
where		p.country = 'usa';

-- 33 Listar los autores que residan en el mismo estado que 
-- las tiendas. Mostrar el nombre y apellido del autor en 
-- una columna y el nombre de la tienda en otra. Apodar 
-- ambas columnas. Ordenar por la columna 1. 
select		concat(a.au_fname,' ',a.au_lname) autor,-- columna 1
			s.stor_name as libreria -- columna 2
from		stores s
inner join	authors a
on			a.state = s.state
order by	1;-- 1 es la primera columna del SELECT, o sea, por autor

-- 34 Mostrar el nombre y apellido del autor y el nombre 
-- de los libros publicados por el mismo. Mostrar un apodo 
-- para cada columna. Ordenar por la primera columna de la 
-- consulta. 
select		concat(a.au_fname,' ',a.au_lname) autor,-- columna 1
			t.title libro
from		titles t
inner join	titleauthor ta on t.title_id = ta.title_id
inner join	authors a on ta.au_id = a.au_id
order by	1;

-- ahora un triple join

-- 35.  Mostrar los libros junto a su autor y su editorial. 
-- Se debe mostrar los datos en una unica columna de la 
-- siguiente manera con los siguientes textos literales: 
-- 'El libro XXXXXXXXXXXXX fue escrito por XXXXXXXXXXXXX y 
-- publicado por la editorial XXXXXXXXXXXXX' 
select		concat('El libro ', t.title,' fue escrito por ', 
			a.au_fname,' ',a.au_lname,' y publicado por la '
            ,'editorial ',p.pub_name) as busqueda
from		authors a 
inner join	titleauthor ta on (a.au_id = ta.au_id)
inner join	titles t on (ta.title_id = t.title_id)
inner join	publishers p on (p.pub_id = t.pub_id);


-- 36. Mostrar el nombre de las editoriales que no hayan publicado 
-- ningún libro. Hay que utilizar outer join porque hay una negativa
-- tabla principal: editoriales(publishers)
select		p.pub_name editorial
			 -- , t.* -- solo uso esto para darme cuenta de las no coincidencias
-- o sea, todos los campos de la tabla secundaria(t.*)
from		publishers p left join	titles t on (t.pub_id = p.pub_id)
where		t.title_id is null;

-- la tabla principal queda a la izquierda de la palabra join
-- en el where siempre filtrar por la clave principal de la tabla secundaria(t.title_id)

show databases;


-- 37. Mostrar el nombre de los libros que nunca fueron vendidos.
-- otra vez, hay q usar outer join 
-- tabla principal: libros (titles)
select		t.title libro
			-- , s.*
from		sales s right join	titles t on (t.title_id = s.title_id)
where		s.ord_num is null;

-- ord_num: nro de factura y forma parte de la clave primaria de la tabla sales(ventas)



-- 38. Mostrar el nombre y apellido de los empleados y la 
-- descripción del trabajo que realiza. Basar la relación en 
-- el nivel de trabajo. 
-- 
select		concat(e.fname,' ',e.lname) empleado,
			j.job_desc puesto
from		jobs j
inner join	employee e on e.job_id = j.job_id
-- where		e.job_lvl between j.min_lvl and j.max_lvl;
-- todos los empleados trabajan entr un minimo y un maximo
where	 	e.job_lvl between 100 and 200;

-- job_lvl: nivel de trabajo: es la cantidad de horas trabajadas durante un mes
		
-- 39. Mostrar el producto cartesiano entre los libros de negocio 
-- (business) y las tiendas ubicadas en California (CA). 
-- Mostrar el nombre de la tienda y el nombre del libro. Ordenar por 
-- nombre de tienda. 
select		stor_name tienda,
			title libro,
			type categoria,
			state estado
from		titles
cross join	stores
where		state = 'ca' and type like '%busi%'
order by	1;





































