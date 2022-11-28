import abc
from abc import ABC, abstractmethod


class Animal:
    def __init__(self, nombre):
        self.setNombre(nombre)

    def setNombre(self, nombre):
        self.nombre = nombre

    @abc.abstractmethod
    def tipoDeSonido(self):
        pass

    def __str__(self):
        return "El nombre del animal es: " + self.nombre


class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def tipoDeSonido(self):
        print(" Miau miau ")

    def __str__(self):
        return super().__str__() + " raza " + self.raza


gato1 = Gato("Pocho", "Siames")
gato1.tipoDeSonido()
print(gato1)
