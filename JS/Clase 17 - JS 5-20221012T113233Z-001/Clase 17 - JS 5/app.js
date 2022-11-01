//Creación de arrays o arreglos

let numeros = new Array(20,1,45,10,88,6)

console.log(numeros)

let colores = ["Verde", "Azul", "Gris", "Marron"]

let vacio = []

let mixto = [25, "Casa", false]

document.write("En la tercera posicion se encuentra el color ", colores[2])

document.write("<br>Que pasa si quiero imprimir en pantalla lo siguiente", colores[10])
console.log(vacio[1])

document.write("<br>Mi Array de numeros tiene ",numeros.length," elementos")

document.write("<br>Los elementos de mi array de colores son :")
for(let i=0; i<colores.length;i++){
    document.write("<br>En el lugar "+i,"del vector colores se encuentra el " +colores[i])
}

//Ingresar elementos al array

//push y el pop

colores.push("Rojo", "Violeta")  //agrega elementos al final

console.log(colores)

colores.pop() //me quita el ultimo elemento del array

console.log(colores)

//con unshift se añaden elementos al princio
//con shit se quitan elementos al princio

colores.unshift("Violeta")
console.log(colores)

colores.shift()
console.log(colores)

//comando sort sirve para ordenar alfabeticamente 

colores.sort()
document.write("<br>Los colores ordenados alfabeticamente: ", colores)

//comando reverse

colores.reverse()
document.write("<br>Los colores ordenados al inverso del alfabeto: ", colores)

//for in y for of

for (numero in numeros){
    console.log(numero)
    console.log(numeros[numero])
}


let vocales = ["a","e","i","o","u"]

for(let vocal of vocales){
    console.log(vocal)
    
}

//local storage y session storage


if(typeof(Storage) !== undefined){

localStorage.setItem("Comision", 22509)
localStorage.setItem("Horario","18.30")
console.log("Los datos se guardaron con exito!")
}else{
    console.log("Su navegador no soporta el localStorage")
}


if(typeof(Storage) !== undefined){

    sessionStorage.setItem("Comision", 22509)
    sessionStorage.setItem("Horario","18.30")
    console.log("Los datos se guardaron con exito!")
    }else{
        console.log("Su navegador no soporta el sessionStorage")
    }



















