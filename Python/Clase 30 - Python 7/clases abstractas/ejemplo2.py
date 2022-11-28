
import abc
# from abc import ABC
from abc import ABC, abstractmethod

# clase padre


class Animal:
    def __init__(self, nombre):
        self.setNombre(nombre)

    def setNombre(self, nombre):
        self.nombre = nombre


# Decorador para métodos abstractos


    @abc.abstractmethod
    def tipoDeSonido(self):
        pass

    def __str__(self):
        return "Nombre: " + self.nombre

    # pass, que tal como su nombre lo indica es una operación nula, o sea que no pasa
    # nada cuando se ejecuta. Se utiliza cuando se requiere por sintaxis una declaración
    # pero no se quiere ejecutar ningún comando o código.

    # clase hija


class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

        # Aqui la clase hija implmenta el cuerpo del metodo abstracto tipoDeSonido
        # de la clase padre.

    def tipoDeSonido(self):
        print("Ladrido")

    def __str__(self):
        return super().__str__() + " Raza: " + self.raza


class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    # Aqui la clase hija implmenta el cuerpo del metodo abstracto tipoDeSonido
    # de la clase padre.

    def tipoDeSonido(self):
        print("Maullido")

    def __str__(self):
        return super().__str__() + " Raza: " + self.raza


    # Bloque principal
p = Perro("Fito", "Golden Retriever")
p.tipoDeSonido()
print(p)

print("------------------------------")

p = Gato("Garfield", "Burmes")
p.tipoDeSonido()
print(p)
