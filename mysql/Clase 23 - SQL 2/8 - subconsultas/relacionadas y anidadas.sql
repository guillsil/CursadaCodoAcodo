create database prueba
go
use prueba

CREATE TABLE cliente (
  id int  NOT NULL identity(1,1),
  nombre VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE pedido (
  id int NOT NULL identity(1,1),
  id_cliente int NOT NULL,
  comentario text NOT NULL,
  fecha datetime NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES cliente(id),
  PRIMARY KEY (id)
);

--1. Crear una consulta que busque todos los pedidos del mes actual, trayendo la fecha y el
-- comentario del pedido y el nombre del cliente.

SELECT		nombre,
			fecha,
			comentario
		
FROM		pedido p
INNER JOIN	cliente c
ON			(p.id_cliente=c.id)
WHERE		MONTH(fecha)= MONTH(GETDATE()) 

--2. Crear una consulta que devuelva la cantidad de pedidos por mes que hizo cada cliente, 
-- ordenando el resultado por mes y luego por nombre de cliente.


SELECT		nombre,
			MONTH(fecha) mes,
			COUNT(p.id)"cantidad de pedidos"
			
FROM		pedido p
INNER JOIN	cliente c
ON			(p.id_cliente=c.id)

GROUP BY	nombre,MONTH(fecha) 
ORDER BY	2,1

--3. Crear una consulta que devuelva todos los clientes que tienen más de 10 pedidos, 
-- ordenando el resultado por cantidad de pedidos.

SELECT		nombre,
			COUNT(p.id)"cantidad de pedidos"
		
FROM		pedido p
INNER JOIN	cliente c
ON			(p.id_cliente=c.id)
GROUP BY	nombre
HAVING		COUNT(p.id)>10
ORDER BY	2 DESC