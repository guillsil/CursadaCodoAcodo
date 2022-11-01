function alternar () 
{
	//capturo en  variables el div y el a
	contenedor = document.getElementById('caja');
	link = document.getElementById('vinculo');
	
	//si el div esta oculto...
	if (contenedor.style.display == 'none') 
	{
		//...entonces,  hago visible el div
		contenedor.style.display = 'block';
		//modifico la etiqueta del vinculo
		link.innerHTML = 'Ocultar Div';
	} 
	
	else
	{
		//...sino, oculto el div
		contenedor.style.display = 'none';
		//modifico la etiqueta del vinculo
		link.innerHTML = 'Mostrar Div';
	}
}

