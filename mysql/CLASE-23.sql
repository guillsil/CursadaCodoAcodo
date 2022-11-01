
drop database IF EXISTS basenueva;
create database basenueva;
use basenueva;

#creacion de tabla
create table IF NOT EXISTS alumnos(
id_alumno int not null primary key,
Nombre varchar(40),
Apellido varchar(40),
Edad int not null
);

show tables;
describe alumnos;

insert into alumnos (id_alumno, Nombre, Apellido, Edad)
values
(01, "GUILLERMO", "Silva", 20),
(02, "Enzo", "Labrpvitta", 18),
(03, "Carlos", "Silva", 15),
(04, "Arturo", "Grotoli", 36),
(05, "Andres", "Silva", 20);

update alumnos
set 
Nombre = "Roberto"
where id_alumno = 2;

delete from alumnos
where id_alumno = 4;

SELECT * 
FROM alumnos

where Edad > 19;




