-- consultas relacionadas

/*
inner join
left outer join
right outer join
full outer join
cross join
self join
*/
-- estructura
SELECT column_name(s)
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;

-- ejemplo
create database relaciones;

use relaciones;

create table empleados
(
	emp_id int,
	emp_nombre varchar(20),
	suc_id int
);

create table sucursales
(
	suc_id int,
	suc_nombre varchar(20)
);


insert into empleados values
(1,'Juan',1),
(2,'Carlos',2),
(3,'Jose',2),
(4,'Maria',null);

insert into sucursales values
(1,'Centro'),
(2,'Congreso'),
(3,'Almagro'),
(4,'Palermo');

truncate table empleados;
truncate table sucursales;

-- delete fom empleados;

select * from sucursales;
select * from empleados;

-- listar el nombre de los empleados y de las sucursales 
-- dnd trabajan
-- se usa inner join--> devuelve los datos(nombre de empleados y sucursales)
-- de aquellos registros en los cuales coincidan los valores de los campos
-- por los cuales se relacionan ambas tablas.(suc_id de ambas tablas).
select 		emp_nombre, 
			suc_nombre
from 		empleados
-- JOIN 		sucursales
inner join		sucursales
-- ON 		(empleados.suc_id = sucursales.suc_id);
on 			empleados.suc_id = sucursales.suc_id
where		emp_nombre <> 'Juan'
order by	emp_nombre desc;

/*listar los datos de los empleados q NO trabajan en ninguna sucursal
nota: debido a la negacion que hay en el enunciado, se que se resuelve
con outer join(left o right, da lo mismo) y no inner join.

El outer left join o el right outer join devuelve TODO(coincidencias y NO coincidencias)
pero a mi me interesa quedarme solo con las NO coincidencias(es decir, aquellos registros
en los cuales los valores de suc_id de ambas tablas NO coincidan).

tabla ppal:empleados(xq en el enunciado me pide los "datos de los empleados")*/

select 		e.emp_nombre 
/*todos los campos de la tabla secundaria(s.*) --> solo lo uso para 
"darme cuenta" cuales son los registros en los cuales no coinciden
los valores de suc_id de ambas tablas*/
			-- ,s.*
from 		empleados as e-- la tabla ppal queda a la "izquierda" de la palabra join
left join	sucursales s-- la tabla secundaria queda a la "derecha" de la palabra join
on 			e.suc_id = s.suc_id
/*hacemos null a la clave principal de la tabla secundaria
para obtener los datos de los empleados que no trabajan 
en ninguna sucursal.*/
where		s.suc_id is null;

