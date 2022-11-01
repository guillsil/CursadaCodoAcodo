function mostrarPestaña (pesta) 
{
	//capturo todos los divs
	// div1 = document.getElementById('pest1');
	// div2 = document.getElementById('pest2');
	// div3 = document.getElementById('pest3');

	// //oculto todos los divs
	// div1.style.display = 'none';
	// div2.style.display = 'none';
	// div3.style.display = 'none';

	// //muestro solo el div pasado por argumento en la funcion mostrarPestaña
	// divSeleccionado = document.getElementById(pesta);
	// divSeleccionado.style.display = 'block';




	
	div1 = document.getElementById('pest1');
    div2 = document.getElementById('pest2');
    div3 = document.getElementById('pest3');
    div1.style.display = 'none';
    div2.style.display = 'none';
    div3.style.display = 'none';
    divSeleccionado = document.getElementById(pesta);
    divSeleccionado.style.display = 'block';
}