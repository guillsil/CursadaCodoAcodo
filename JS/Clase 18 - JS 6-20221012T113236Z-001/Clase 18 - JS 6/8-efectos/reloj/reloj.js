function mostrarHora () 
{
	//instancio la hora de la PC y la guardo en una variable
	reloj = new Date();

	//separo en variables la hora, los minutos y los segundos de la hora del sistema
	hora = reloj.getHours();
	minutos = reloj.getMinutes();
	segundos = reloj.getSeconds();

	//agrego los ceros si el valor e menor a 10
	if(hora < 10) hora = '0' + hora;
	if(minutos < 10) minutos = '0' + minutos;
	if(segundos < 10) segundos = '0' + segundos;

	//capturo el div en el cual mostrare la hora
	contenedor = document.getElementById('caja');

	//escribo dentro del div
	contenedor.innerHTML = hora + ' : ' + minutos + ' : ' + segundos;
}

//invoco o llamo (uso) la funcion setInterval
//Ejecuta la funcion mostrarHora cada 1000 milisegundos(o sea, cada segundo)
window.setInterval('mostrarHora()',1000);