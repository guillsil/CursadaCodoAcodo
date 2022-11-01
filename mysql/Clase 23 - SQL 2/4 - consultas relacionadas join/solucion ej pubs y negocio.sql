use pubs;

-- Mostrar los libros junto a su autor y su editorial. 
-- Se debe mostrar los datos en una unica columna de la siguiente manera con los siguientes textos literales: 
-- 'El libro XXXXXXXXXXXXX fue escrito por XXXXXXXXXXXXX y publicado por la editorial XXXXXXXXXXXXX' 


select        concat('El libro ',t.title,' fue escrito por ',a.au_fname,' ',a.au_lname,' y publicado por la editorial ',pub_name) Informacion
from        	authors a       
inner join    titleauthor ta on (a.au_id = ta.au_id)
inner join    titles t on ta.title_id = t.title_id
inner join    publishers p on t.pub_id = p.pub_id;


-- Mostrar el nombre de los libros que nunca fueron vendidos. 
-- outer join
-- tabla ppal: titles(de la cual quiero obtener datos)
-- tabla secundaria: sales
select				t.title libro
					 -- , s.*
from				sales s 
right join			titles t on t.title_id = s.title_id
where				s.stor_id is null;


-- 39 Mostrar el producto cartesiano entre los libros de negocio (business) y las tiendas ubicadas en California (CA). 
-- Mostrar el nombre de la tienda y el nombre del libro. Ordenar por nombre de tienda

-- Ansi - SQL
select		s.stor_name tienda,
			t.title libro,
			t.type categoria,
			s.state estado
from		titles t, stores s
where		type like '%busi%'
and			state = 'ca';

-- variante
select		s.stor_name tienda,
			t.title libro,
			t.type categoria,
			s.state estado
from		titles t
cross join	stores s
where		type like '%busi%'
and			state = 'ca';

select * from titles;
select * from stores;

-- 38 Mostrar el nombre y apellido de los empleados y la descripción del trabajo que 
-- realiza. Basar la relación en el nivel de trabajo. 
select		concat(e.fname,' ',e.lname) as empleado,
			j.job_desc 'descripcion del puesto'
from		jobs j
inner join	employee e on (e.job_id = j.job_id)
-- where		e.job_lvl between j.min_lvl and j.max_lvl;
where		e.job_lvl between 100 and 150;

describe authors;

use negocio;

-- 1 Listar la cantidad de clientes que hicieron alguna compra en el 
-- segundo semestre de 2017. 
select        	concat(nombre,'  ',apellido) Clientes
				,fecha Fecha
from        	clientes c
inner join    	facturas f
on            	c.idcliente = f.idcliente
where        	year(fecha) = 2017 and month(fecha) between 07 and 12
order by    	fecha desc;

  -- 2) Informar la cantidad de compras por cliente. Informar el nombre 
-- y apellido en una única columna de dichos clientes. Ordenar por 
-- cantidad de compras en forma descendente.
SELECT 	CONCAT(c.nombre,' ',c.apellido) 'Nombre y Apellido', 
		COUNT(f.idcliente) 'Cantidad Compra' 
FROM 	clientes c
JOIN 	facturas f
ON 		c.idcliente=f.idcliente
GROUP BY CONCAT(c.nombre,' ',c.apellido)
ORDER BY COUNT(f.idcliente) DESC;
 
  -- 3) Informar las ventas por artículo. Cuál es el artículo más 
-- comprado? Ordenar por cantidad de ventas del más vendido al menos 
-- vendido.
SELECT 	p.articulo, 
		COUNT(f.idproducto)'Cantidad Vendida'
FROM 	productos p
JOIN 	facturas f ON p.idproducto=f.idproducto
GROUP BY p.articulo
ORDER BY COUNT(f.idproducto) DESC
limit	1;

 -- 4) Ídem ejercicio anterior pero incluir solo los artículos con una 
-- cantidad de ventas mayor o igual a 2. No incluir a los clientes que 
-- compraron camisas.
SELECT 	p.articulo, 
		COUNT(f.idproducto)'Cantidad Vendida'
FROM 	productos p
JOIN 	facturas f ON p.idproducto=f.idproducto
-- where	articulo not like '%camisa%'
where	articulo <> 'camisa'
GROUP BY p.articulo
having	COUNT(f.idproducto) >=2
ORDER BY COUNT(f.idproducto) DESC;


 -- 5) Listar nombre y apellido (en una sola columna) y teléfono de los 
-- clientes que compraron pantalones. Indicar cuanto pagaron y cuando 
-- compraron. Ordenar por fecha de compra, mostrando primero la compra 
-- más antigua.
select		concat(c.nombre,' ',c.apellido) cliente,
			c.telefono,
			p.articulo,
			p.precio,
			f.fecha
from		clientes c, facturas f, productos p
where		c.idcliente = f.idcliente and f.idproducto = p.idproducto
and			p.articulo like '%pantalon%'
order by	f.fecha asc;

-- variante
select		concat(c.nombre,' ',c.apellido) cliente,
			c.telefono,
			p.articulo,
			p.precio,
			f.fecha
from		clientes c
inner join	facturas f on c.idcliente = f.idcliente 
inner join	productos p on f.idproducto = p.idproducto
where 		p.articulo like '%pantalon%'
order by	f.fecha asc;

			
			






