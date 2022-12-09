# Polimorfismo

class Animal:
    def hablar(self):
        pass


class Gato(Animal):
    def hablar(self):
        print("Miau miau")


class Vaca(Animal):
    def hablar(self):
        print("Muuuuuuuuuuuuuuuuuuuuuu")


class Perro(Animal):
    def hablar(self):
        print("Guau guau")


for animal in [Gato(), Vaca(), Perro()]:
    animal.hablar()
