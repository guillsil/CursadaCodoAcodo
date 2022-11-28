class Animal:
    def hablar(self):
        pass


class Gato(Animal):
    def hablar(self):
        print("Miau")


class Perro(Animal):
    def hablar(self):
        print("Guau")

# Arranca el programa


for animal in [Gato(), Perro()]:
    animal.hablar()
