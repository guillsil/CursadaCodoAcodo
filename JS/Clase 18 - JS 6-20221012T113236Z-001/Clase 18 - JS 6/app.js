//Metodo tradicional GetElementBy (id, tagname, className, etc) e innerHTML

function cambiarTexto(){
    let elementos = document.getElementsByClassName("elemento");
    elementos[0].innerHTML = "Hola mundo desde JS!!!"
}

function cambiarTextoTodos(){
    //let elementos = document.getElementsByClassName("elemento");
    let elementos = document.getElementsByTagName("div")
    for(i=0; i<elementos.length; i++)
    elementos[i].innerHTML = "Este es el elemento "+(i+1)
}

function cambiarTitulo(){
    let titulo = document.getElementById("hola")
    titulo.innerHTML = "Este es mi titulo nuevo"
}


//metodo moderno query selector

function agregarFondo(){
    document.querySelector(".ejemplo").style.backgroundColor = "pink";
    document.querySelector(".boton").innerHTML = "Cambiamos el color!"
}

//funcion creada desde js

function agregarBoton(){
    let btn = document.createElement("button")
    btn.innerHTML = "Boton creado con JS"
    document.body.appendChild(btn); 
}

agregarBoton();

function agregarTitulo(){
    let titulo = document.createElement("h2")
    let contenido = document.createTextNode("Soy un titulo creado con JS")
    titulo.appendChild(contenido);
    document.body.appendChild(titulo)
}

agregarTitulo()

//uso del addeventListener

let boton = document.getElementById("miBoton");
boton.addEventListener("click", mostrarFecha);

function mostrarFecha(){
    document.getElementById("fecha").innerHTML = Date()
}