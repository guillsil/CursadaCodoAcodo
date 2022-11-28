class Familia:

    def __init__(self, padre, madre, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        cadena = self.padre+","+self.madre
        for hijo in self.hijos:
            cadena = cadena+","+hijo
        return cadena

# Programa principal


familia1 = Familia("Juan", "Maria", ["Pedro", "Juanita"])
familia2 = Familia("Jorge", "Sandra")
familia3 = Familia("Luis", "Maria", ["Marcos", "Juan", "Pedro", "Alberto"])

print(familia1)
print(familia2)
print(familia3)
