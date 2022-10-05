//Creacion de un objeto Literal

let perro = {
    nombre: "Firulais",
    edad: 5,
    color: "Negro",
    //metodo (funcion dentro de un objeto)

    ladrar(){
         return this.nombre + " dice Guau"
    }
}

//Llamado a un objeto

console.log(perro);
console.log(perro.ladrar())
document.write("El nombre de mi perro es ", perro.nombre);

//modificacion

perro.nombre = "Pepin"

document.write("<br>El nombre de mi perro es ", perro.nombre);

//objetos con new object

let miAuto = new Object()

//una vez creado el objeto tenemos que asignarle las propiedades que querramos

miAuto.marca = "Peugeot";
miAuto.tipo = "207";
miAuto.modelo = 2014;
//notacion corchetes
miAuto['color'] = "Rojo";  // es lo mismo que poner miAuto.color = "Rojo"

console.log(miAuto);
document.write("<br>Mi auto es un " , miAuto.marca+ " "+ miAuto.tipo+"del año "+miAuto.modelo + " y de color "+miAuto.color)


//Creacion de objetos mediante clases

class Alumno {
    constructor(id, nombre, grupo, evaluacion){
        this.id = id
        this.nombre = nombre
        this.grupo = grupo
        this.evaluacion = evaluacion
    }
}

//instanciar los distintos alumnos que tengo

let alumno1 = new Alumno(1,"Juan Peres", 15, 9)
let alumno2 = new Alumno(2,"Maria", 15, 9)
let alumno3 = new Alumno(3,"Ruben", 15, 9)


//Propiedades de los strings

let cadena1 = "Cadena creada de la manera correcta"
let cadena2 = new String ("Cadena creada un poco más largo")

document.write("<br>La longitud de la cadena 1 es de "+cadena1.length+ " caracteres")

document.write("En la posicion 7 de la cadena 2 la letra es:",cadena2.charAt(7))