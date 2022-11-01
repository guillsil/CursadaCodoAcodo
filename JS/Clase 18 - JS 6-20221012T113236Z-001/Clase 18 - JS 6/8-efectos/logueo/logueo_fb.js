function limpiar (campo) 
{
	if (campo.value == 'Usuario') 
	{
		campo.value = '';
		campo.style.color = 'black';
	}

	if (campo.value == 'Clave') 
	{
		campo.value = '';
		campo.style.color = 'black';
		campo.type = 'password';
	}
}


function llenar () 
{
	//capturo los inputs de usuario y contraseña
	user = document.getElementById('usuario');
	pass = document.getElementById('clave');

	//si el campo de texto esta vacio...
	if (user.value == '') 
	{
		user.value = 'Usuario';
		user.style.color = '#888';
		pass.value = 'Clave';
		pass.style.color = '#888';
		
	}
}

