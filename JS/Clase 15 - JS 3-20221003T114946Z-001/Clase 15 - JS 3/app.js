//Declaracion de una funcion        

function saludar(){
    document.write("Hola mundo desde una funcion!<br>")
}

//Implementar la funcion

saludar();
saludar();
saludar();

//funciones con parametros y argumentos


let numero1 = Number.parseInt(prompt("Ingrese el primer numero"));
let numero2 = Number.parseInt(prompt("Ingrese el segundo numero"));


function sumar(numero1,numero2){
    
    document.write("La suma de los dos numeros es:" , numero1+numero2)
}


function restar(numero1,numero2){
    document.write("La resta de los dos numeros es:" , numero1-numero2)
}



sumar(numero1,numero2);
resta(numero1,numero2);

let nombre = prompt("Ingrese su nombre:")

function saludar2(nombre){
    document.write("<br>Mucho gusto," + nombre + "bienvenido a la pagina")
}

saludar2(nombre);


//funcion con bucles

let valor = Number.parseInt(prompt("Ingrese el numero"));

function tablaDeMultiplicar(valor){
    for(var i=1; i<=10; i++){
        console.log(valor + "x" + i + "=", valor*i)
    }
}

tablaDeMultiplicar(valor);


//Funciones con return

var maximo = function numeroMaximo(a,b){
    if(a>b){
        return a
    }else{
        return b
    }
}

let a = parseInt(prompt("Ingrese el primer numero"));
let b = parseInt(prompt("Ingrese el segundo numero"));

console.log("El mayor de los dos numero es", maximo(a,b));


