class Operacion:

    def __init__(self):
        self.valor1 = int(input("Ingrese el primer numero: "))
        self.valor2 = int(input("Ingrese el segundo numero: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def __del__(self):
        print("Se ha eliminado la operacion")

    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma de los 2 numeros es : {}".format(suma))

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta de los 2 numeros es : {}".format(resta))

    def multiplicar(self):
        producto = self.valor1 * self.valor2
        print("La multiplicacion de los 2 numeros es : {}".format(producto))

    def dividir(self):
        division = self.valor1 / self.valor2
        print("La division de los 2 numeros es : {}".format(division))


operacion1 = Operacion()
