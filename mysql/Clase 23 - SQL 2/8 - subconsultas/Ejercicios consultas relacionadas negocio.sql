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


--2. Crear una consulta que devuelva la cantidad de pedidos por mes que hizo cada cliente, 
-- ordenando el resultado por mes y luego por nombre de cliente.


--3. Crear una consulta que devuelva todos los clientes que tienen más de 10 pedidos, 
-- ordenando el resultado por cantidad de pedidos.

--4. traer nombre y apellido de la primer venta


--5. listar nombre y apellido de los clientes que compraron remeras. 

--6. Indicar cuanto pagaron y cuando la compraron.

--7. listar la cantidad de ventas del dia de hoy

--8. listar la cantidad de ventas por marca.



