// JavaScript for/in Statement
// https://www.w3schools.com/jsref/jsref_forin.asp
// For in recorre las propiedades de un objeto

/*
var vec = ["a", "b", "c", "d"]

console.log(vec);

for (var i in vec) {
    console.log(i)  // 0, 1, 2, 3
}

for (var i in vec) {
    console.log(vec[i]) // a, b, c, d
}

// Otro ejemplo con Objetos
var persona = {
    nombre: "Ana",
    apellido: "Paz",
    edad: 25
};

var x;
for (x in persona) {
    console.log(x); // nombre, apellido, edad
}
for (x in persona) {
    console.log(x + ": " + persona[x]); // nombre: Ana, apellido: Paz, edad: 25
}
*/

/*
// JavaScript for/of Statement
// https://www.w3schools.com/jsref/jsref_forof.asp
// Recorre los valores de un iterable.
// Ejemplo 1

let cad = "hola";
for (let letra of cad) {
    console.log(letra); // h, o, l, a
}

// Ejemplo 2
let nombres = ["Juan", "Ana", "Luis"]
for (let item of nombres) {
    console.log(item);  // Juan, Ana, Luis
}

// Ejemplo 3
let numeros = [2, -4, 99]
for (let elem of numeros) {
    console.log(elem); // 2, -4, 99
}
*/