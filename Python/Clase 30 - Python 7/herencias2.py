class Valores:

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.total = 0

    def cargar1(self):
        self.valor1 = int(input("Ingrese el primer valor: "))

    def cargar2(self):
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def imprimir(self):
        print("El resultado de la operacion es: ", self.total)

    def operacion(self):
        pass


class Suma(Valores):

    def operar(self):
        self.total = self.valor1 + self.valor2


class Resta(Valores):

    def operar(self):
        self.total = self.valor1 - self.valor2


suma1 = Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
suma1.imprimir()
