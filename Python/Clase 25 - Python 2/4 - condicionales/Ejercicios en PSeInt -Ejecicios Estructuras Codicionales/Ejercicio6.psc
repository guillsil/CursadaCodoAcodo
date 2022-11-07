Algoritmo Ejercicio6
	Escribir "Personas = "
	Leer personas
	
	Si personas>200 y personas<=300
		Escribir "Costo = " , personas * 85, " $"
	SiNo
		Si personas > 300
			Escribir "Costo = " , personas * 75 , " $"
		SiNo
			Escribir "Costo = " , personas * 95 ," $"
		FinSi
	FinSi
	
FinAlgoritmo
