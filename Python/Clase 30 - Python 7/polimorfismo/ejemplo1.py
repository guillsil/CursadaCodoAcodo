# El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases 
# pueden responder a una misma acción.

# El polimorfismo es implícito en Python, ya que todas las clases son subclases de una 
# superclase común llamada Object.

# clase padre
class Auto:

    def __init__(self,marca,velocidad):
        self.marca = marca
        self.velocidad = velocidad
        

    def imprimir(self):
        print("Marca:",self.marca)
        print("Velocidad:",self.velocidad)

    def acelerar(self):
            self.velocidad = self.velocidad + 10
        
        

# clase hija
class AutoCarrera(Auto):

    # En el constructor de la clase hija invoco al constructor del padre
    def __init__(self,marca,velocidad,tipoDeAleron):
        super().__init__(marca,velocidad)
        self.tipoDeAleron = tipoDeAleron

    def imprimir(self):
        super().imprimir() #invoco al metodo imprimir del padre
        print("Tipo de Aleron:",self.tipoDeAleron)

    # Aca aplicamos polimorfismo. Es decir, redefinimos el cuerpo de un metodo
    # heredado desde la clase padre.(En este caso, el metodo acelerar), ya que
    # un auto de carrera acelera mas que un auto comun.
    def acelerar(self):
            self.velocidad = self.velocidad + 50


# bloque principal
print("Datos del auto")

marca = input("Ingrese la marca:")
velocidad = int(input("Ingrese la velocidad:"))

auto1 = Auto(marca,velocidad)

auto1.acelerar()
auto1.imprimir()

print("-----------------------------------")

print("Datos del auto de carrera")

marca = input("Ingrese la marca:")
velocidad = int(input("Ingrese la velocidad:"))
tipoDeAleron = input("Ingrese el tipo de aleron:")

auto2 = AutoCarrera(marca,velocidad,tipoDeAleron)

auto2.acelerar()
auto2.imprimir()

