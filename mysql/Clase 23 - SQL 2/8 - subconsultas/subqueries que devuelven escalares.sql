-- listar todos los datos del libro mas caro
select round(max(price), 2) from titles;

select 	* 
from 	titles 
where 	price = (select max(price) from titles);

-- listar todos los datos del primer empleado
select 	* 
from 	employee 
where 	hire_date = (select min(hire_date) from employee);



