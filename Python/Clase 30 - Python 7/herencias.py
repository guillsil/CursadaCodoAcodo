# Clase Padre = Superclase ----------> Pasa metodos y atributos a sus hijos
# Clase Hijo = Subclase -----------> Hereda metodos y atributos de su padre o crea los suyos

class Persona:

    def __init__(self):
        self.nombre = input("Ingrese su nombre")
        self.apellido = input("Ingrese su apellido")

    def imprimir(self):
        print(f"El nombre ingresado es {self.nombre} {self.apellido}")


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese su sueldo"))

    def imprimir(self):
        super().imprimir()
        print("El sueldo es: ", self.sueldo)

    def ganancias(self):
        if self.sueldo > 300000:
            print("El empleado debe pagar ganancias")
        else:
            print("No debe pagar ganancias")


persona1 = Persona()
persona1.imprimir()

empleado1 = Empleado()
empleado1.imprimir()
empleado1.ganancias()
