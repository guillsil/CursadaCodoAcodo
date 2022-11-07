Algoritmo Ejercicio4
	Escribir "Usuario = "
	Leer usuario
	Escribir "Clave = "
	Leer clave
	
	Si usuario = "pepito" y clave = 1243
		Escribir "Bienvenido pepito"	
	FinSi
		
	Si usuario = "pepito" y clave <> 1243
		Escribir "Clave incorreta"	
	FinSi
		
	Si usuario <> "pepito" y clave = 1243
		Escribir "Usuario incorrecto"	
	FinSi
	
FinAlgoritmo
