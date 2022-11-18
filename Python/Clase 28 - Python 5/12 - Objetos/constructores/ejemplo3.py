# Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el 
# método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, 
# imprimir dichos resultados.

class Operaciones:
    # constructor vacio
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es",resta)

    def multiplicar(self):
        producto=self.valor1*self.valor2
        print("El producto es",producto)

    def division(self):
        division=self.valor1/self.valor2
        print("La division es",division)


# bloque principal

operacion1=Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()