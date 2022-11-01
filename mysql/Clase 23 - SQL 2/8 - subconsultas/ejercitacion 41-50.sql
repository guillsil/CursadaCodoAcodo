-- Ejercitacion.doc
-- Consultas anidadas

-- 41.	Listar el nombre de los libros junto a su categoría de 
-- precio. La categoría de precio se calcula de la siguiente 
-- manera: Si el precio está entre 0 y 10 la categoría es 
-- Económica. Si la categoría está entre 10 Y 20, Normal y si 
-- su valor es mayor a 20 la categoría es Caro. 
-- Colocar un apodo a las dos columnas.
use pubs; 
select		title libro,
			price precio,
            case 
            
				when price < 10 then 'Economica'
                when price between 10 and 20 then 'Normal'
                when price > 20 then 'Caro'
                else 'No categorizado'
             end as categoria
from		titles;

-- 42. Listar los 5 libros de mayor precio.
select		*
from		titles
order by	price desc
limit 		5;
-- variante usando subquery
select		*
from		titles
where		price in (select price from titles)
order by	price desc
limit 		5;

 
-- 43. Listar la mitad de los empleados. 
SET @inicio=0; SET @cantidadRegistros=(select (count(*) div 2 + 1) from employee);
PREPARE sentencia FROM 'SELECT * FROM employee LIMIT ? , ?';
EXECUTE sentencia USING @inicio, @cantidadRegistros;

select * from employee;


-- 44.	Listar todos los libros vendidos, su nombre y la cantidad vendida por cada uno. 
-- Los apodos para las columnas son las siguientes: "Código del libro", "Nombre del libro" y "Cantidad vendida" .


select		t.title_id 'Codigo del libro',
			title 'Nombre del libro',
			qty 'Cantidad vendida'
from		titles t
inner join	sales s on (t.title_id = s.title_id)
order by	3 desc;

-- 45.	Listar todos los libros cuyo precio sea inferior al precio promedio de todos los
--  libros. 
select		*
from		titles
where		price < (select avg(price) from titles)
order by	price desc;

-- 46.	Listar los empleados de aquellas editoriales que residan en USA. No usar relaciones para su resolución.
select	*
from	employee
where	pub_id in (select pub_id from publishers where country = 'usa');

-- variante
select	e.*, p.country
from	employee e 
inner join publishers p on e.pub_id = p.pub_id
where	e.pub_id in (select p.pub_id from publishers)
and		p.country = 'usa';

-- 47.	Listar la cantidad de libros vendidos por cada tienda, sólo de aquellas tiendas que su cantidad de venta sea mayor al promedio de venta general. 
select		stor_name tienda,
			sum(qty) 'ventas por tienda'
from		titles t
inner join	sales s on (t.title_id = s.title_id)
inner join	stores st on (s.stor_id = st.stor_id)
group by	stor_name
having		sum(qty) > (select avg(qty) from sales)
order by	2 desc;

-- 48.	Listar todos los comprobantes de ventas emitidos para la venta del libro "Sushi, Anyone?". No utilizar relaciones.

 -- usando join
select		s.ord_num 'comprobantes de ventas',
			title libro
from		titles t
inner join	sales s on (t.title_id = s.title_id)
where		title = 'Sushi, Anyone?'
order by	1;

-- usando subconsulta
select		ord_num 'comprobante de ventas'
from		sales s
where		s.title_id in (select t.title_id from titles t where title = 'Sushi, Anyone?')
order by	1;


-- 49.	Mostrar el nombre de los libros junto a su categoría de precio de aquellos libros que son categorizados como "Normal". La categoría de los precios es la misma del ejercicio 41. 
SELECT		*
FROM		(			
				select		title libro,
							price precio,
							case 
								when price < 10 then 'Economica'
								when price between 10 and 20 then 'Normal'
								when price > 20 then 'Caro'
								else 'No categorizado'
							 end as categoria
				from		titles
            ) as tabla
WHERE		tabla.categoria='Normal';

-- 50.	Listar título del libro, categoría de precio, precio unitario y cantidad ejemplares vendidos. Mostrar sólo aquellos libros que sean económicos y cuya cantidad de ejemplares vendidos sea mayor a cero. Se deben apodar las columnas de la siguiente manera: 'Tít", "Cat", "Pr", "Cant". La categoría de los precios es la misma del ejercicio 41.
SELECT		*
FROM		(			
				select		title libro,
							price precio,
                            qty 'cantidad de ejemplares vendidos',
							case 
								when price < 10 then 'Economica'
								when price between 10 and 20 then 'Normal'
								when price > 20 then 'Caro'
								else 'No categorizado'
							 end as categoria
				from		titles t
                inner join	sales s on (t.title_id = s.title_id)
                where		qty > 0
            ) as tabla
WHERE		tabla.categoria='Economica';
