Algoritmo Ejercici7
	
	Escribir "Ingrese tipo de uva (a-b): "
	Leer ti
	Escribir "Ingrese tamaño de uva (1-2): "
	Leer ta
	Escribir "Ingrese cantidad de kilos: "
	Leer k
	Escribir "Ingrese precio por kilo: "
	Leer p
	
	g = 0
	
	Si ti== "a" 		
		Si ta == 1
			g = ( p + 0.2 ) * k
		SiNo
			g = ( p + 0.3 ) * k
		FinSi		
	SiNo
		Si ta == 1
			g = ( p - 0.3 ) * k
		SiNo
			g = ( p - 0.5 ) * k
		FinSi
	FinSi
	
	Escribir "Ganancia = ", g , " $"
	
FinAlgoritmo
