# Crear dos clases llamados Suma y Resta. Cada clase tiene como atributo valor1, valor2 y
# resultado. Los métodos a definir son cargar1 (que inicializa el atributo valor1), carga2
# (que inicializa el atributo valor2), operar (que en el caso de la clase "Suma" suma los
# dos atributos y en el caso de la clase "Resta" hace la diferencia entre valor1 y valor2),
# y otro método mostrar_resultado.

# Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos. En estos
# casos es bueno definir una clase padre que agrupe dichos atributos y responsabilidades comunes.

class Operacion:  # Superclase

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar1(self):
        self.valor1 = int(input("Ingrese primer valor:"))

    def cargar2(self):
        self.valor2 = int(input("Ingrese segundo valor:"))

    def mostrar_resultado(self):
        print(self.resultado)

    def operar(self):
        pass


class Suma(Operacion):

    def operar(self):
        self.resultado = self.valor1+self.valor2


class Resta(Operacion):

    def operar(self):
        self.resultado = self.valor1-self.valor2


# bloque princpipal

suma1 = Suma()
suma1.cargar1()
suma1.cargar2()
suma1.operar()
print("La suma de los dos valores es")
suma1.mostrar_resultado()

resta1 = Resta()
resta1.cargar1()
resta1.cargar2()
resta1.operar()
print("La resta de los valores es:")
resta1.mostrar_resultado()
