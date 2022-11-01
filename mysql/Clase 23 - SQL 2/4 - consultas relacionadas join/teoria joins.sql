-- consultas relacionadas

create database relaciones;

use relaciones;

create table sucursales(suc_id int, suc_nombre varchar(30));
create table empleados(emp_id int, emp_nombre varchar(30), suc_id int);

insert into sucursales values (1,'Centro'),(2,'Congreso'),(3,'Palermo');
insert into empleados values (1,'Juan',1),(2,'Carlos',2),(3,'Jose',2),(4,'Maria',null);

select * from sucursales;
select * from empleados;

SELECT * FROM relaciones.empleados;

use relaciones;

-- inner join: devuelve los datos pedidos de aquellos registros
-- en los q coinciden los valores de los campos por los cuales
-- se relacionan las tablas

-- En este caso, las tablas se relacionan por suc_id, entonces el inner join
-- buscara los registros donde coincidan los suc_id de ambas tablas.

-- listar todos los datos de sucursales y de los empleados q trabajan en ellas
-- el orden de las tablas en el inner join(enlace interno) no es relevante
select 		s.*, e.emp_nombre
from		sucursales s
-- inner join	empleados e
join		empleados as e -- poner join solo es valido en mySQL, no en otros! 
on			s.suc_id = e.suc_id;
-- La clausula on nos dice a traves de que campos se relacionan las tablas

-- hacemos una variante(no usamos alias de tabla sino directamente el nombre de las tablas)
select 		sucursales.*, empleados.emp_nombre
from		sucursales 
inner join	empleados 
on			sucursales.suc_id = empleados.suc_id;

-- mysql --> inner join = join

-- variante del ANSI SQL
-- ANSI: estandares de Estados Unidos
-- Aca, no usamos inner join sino que separamos las tablas con una coma.
-- Tampoco usamos la clausula on sino que usamos la clausula where
select 		s.*, e.emp_nombre
from		empleados as e , sucursales s
where 		s.suc_id = e.suc_id;


-- producto cartesiano
-- todos los registros de una tabla se relacionan con todos los registros
-- de la otra tabla, esto nos devuelve el producto de los registros de una tabla
-- por los registros de la otra tabla.

-- version ANSI-SQL
select 		s.*, e.emp_nombre
from		empleados as e , sucursales s;
-- where 		s.suc_id = e.suc_id;

-- Para ver las coincidencias, agregariamos el where como en el ejemplo anterior
-- o sea, seria el inner join

-- variante(es la forma mas elegante de escribir el codigo)
select 		s.*, e.emp_nombre
from		empleados as e 
cross join	sucursales s;


-- listar el nombre de las sucursales donde No trabajan empleados.
-- uso un outer join(enlace externo)
-- El outer join nos devuelve TODO(coincidencias y no coincidencias de los valores de aquel
-- campo por el cual se relacionan las tablas, o sea, suc_id)

-- tabla ppal: sucursales(es aquella tabla de la cual quiero obtener datos)
-- tabla secundaria: empleados
select 				s.suc_nombre
					 -- ,e.*-- traemos todos los datos de la tabla secundaria, solo para darme cuenta de cuales son las NO coincidencias!, dsp lo elimino
-- from				 empleados e right outer join	sucursales s
from				  sucursales s left join  empleados e
-- from				 empleados e  right outer join	sucursales s
-- la tabla ppal queda a la izquierda de la palabra join. Join es el pivote. Ademas, no es obligatorio poner la palabra outer
on					s.suc_id = e.suc_id-- como se relacionan las tablas
where				emp_id is null;-- filtro y me quedo solo con las no coincidencias

-- en el where siempre usar la clave principal de la tabla secundaria(en este caso, emp_id) q sea nulo
-- la tabla principal(sucursales) va a quedar a la izquierda de la palabra join
-- outer es optativo

-- el valor Palermo es lo q va  a consumir Python por ejemplo

-- Ejemplos:listar nombre de libros que NO fueron vendidos --> tabla ppal: titles(titulos) y tabla secundaria: pubs(editoriales)
-- listar los autores que NO escribieron libros de cocina


-- listar el nombre de los empleados que No trabajan en ninguna sucursal.--> tengo q usar outer join xq hay una negacion
-- tabla ppal: empleados
select 					e.emp_nombre
						-- , s.* -- para ver las no coincidencias, dsp lo elimino
from					sucursales s right outer join empleados e
-- from					empleados e left outer join sucursales s 
on						s.suc_id = e.suc_id
where					s.suc_id is null;-- la clave ppal de la tabla secundaria q sea NULL

-- la tabla principal (empleados) ahora queda a la derecha de la palabra join
-- el valor Maria es lo q va  a consumir Python por ejemplo




















