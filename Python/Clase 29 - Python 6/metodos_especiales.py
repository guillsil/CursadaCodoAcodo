class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f'{self.nombre} hace guau'

    def __str__(self):
        return f'{self.nombre} es un perro que ladra y que tiene {self.edad} años'


perro1 = Perro("Pochito", 6)
print(perro1.nombre)
print(perro1)  # Es el relacionado con __str__
print(perro1.ladrar())
print(type(perro1))

perro1.__del__()
print(perro1)
