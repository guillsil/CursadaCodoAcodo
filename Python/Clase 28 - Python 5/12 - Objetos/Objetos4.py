class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f'{self.nombre} hace guau guau'

    def __str__(self):
        return f'{self.nombre} es un perro que ladra y que tiene {self.edad} años'

# Temrina la definicion de la clase y de los metodos


perro1 = Perro('Firulais', 8)


print(perro1.nombre)
print(perro1.ladrar())
print(type(perro1))
print(perro1)
