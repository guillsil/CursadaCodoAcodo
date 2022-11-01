use pubs;

-- traer la fecha de ingreso del primer empleado
select min(hire_date) 'fecha de ingreso' from employee;

-- listar todos los datos del primer empleado
select 	*
from 	employee
where	hire_date = (select min(hire_date) from employee);
-- where	hire_date = '1989-10-09';

-- variante sin uso de subconsulta
select		*
from		employee
order by	hire_date asc
limit		1;

-- subconsultas q devuelven lista de valores
create database predicados;

use predicados;

create table productos(nro int, precio float);
create table facturas(nro int, monto float);

insert into productos values(1,100),(2,200),(3,300),(4,1000);
insert into facturas values(1,300),(2,500),(3,600),(4,200);

select * from facturas;
select * from productos;

-- listar los productos cuyo precio supera todos los montos facturados
select	*
from	productos
where	precio > all (select monto from facturas);

-- listar los productos cuyo precio supera algun monto facturado
select	*
from	productos
where	precio > any (select monto from facturas);

-- listar los productos cuyo precio sea igual a algun monto facturado
select	*
from	productos
-- where	precio = any (select monto from facturas);
where	precio in (select monto from facturas);

-- listar los productos cuyo precio no sea igual a algun monto facturado
select	*
from	productos
-- where	precio <> all (select monto from facturas);
where	precio not in (select monto from facturas);

-- listar los productos cuyo precio supera el precio promedio de todos los productos.
select	*
from 	productos
where	precio > (select avg(precio) from productos);

-- listar todos los datos de la ultima venta
use negocio;

select	*
from	facturas
where	fecha = (select max(fecha) from facturas);

-- traer nombre y apellido del primer cliente
select		nombre, apellido
from		clientes c
inner join 	facturas f on c.idcliente = f.idcliente
where 		 fecha = (select min(fecha) from facturas);

-- listar nombre y apellido de los clientes que compraron pantalones. 
-- Indicar cuanto pagaron y cuando lo compraron.
select		c.nombre, c. apellido, p.precio, f.fecha
from		clientes c
inner join	facturas f on c.idcliente = f.idcliente
inner join	productos p on f.idproducto = p.idproducto
where		p.articulo like '%pantalon%';


-- listar la cantidad de ventas del dia de hoy
describe facturas;

select		count(*) 'cantidad de ventas'
from		facturas
-- where		fecha = curdate();
where		fecha in (select curdate() from facturas);

select * from ventas;

-- listar la cantidad de ventas por marca.
select		marca,
			count(*) 'cantidad de ventas por marca'
from		productos p
inner join	facturas f on f.idproducto = p.idproducto
group by	marca
order by	marca;




