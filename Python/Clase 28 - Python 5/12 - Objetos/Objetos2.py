# Crear una clase que permita cargar el nombre y la edad de una persona
# y que permita imprimir los datos de la persona.
# Ver si es mayor de edad o no

class Persona:  # Definimos la clase
    # Definimos los metodos inicializar, imprimir y es mayor
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre de la persona: ", self.nombre)
        print("Edad de la persona: ", self.edad)

    def esMayor(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona no es mayor de edad")

# Termino de definir la clase y los metodos, ingreso al bloque principal


persona1 = Persona()
persona1.inicializar("Arturo", 20)  # Inicializamos los datos
persona1.imprimir()
persona1.esMayor()

persona2 = Persona()
persona2.inicializar("Juana", 14)
persona2.imprimir()
persona2.esMayor()
