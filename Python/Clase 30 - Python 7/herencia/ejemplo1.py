# La herencia significa que se pueden crear nuevas clases partiendo de clases existentes, que
# tendrá todas los atributos y los métodos de su 'superclase' o 'clase padre' y además se le
# podrán añadir otros atributos y métodos propios.

# Clase padre o Superclase
# Clase de la que desciende o deriva una clase. Las clases hijas (descendientes) heredan
# (incorporan) automáticamente los atributos y métodos de la la clase padre.

# Subclase
# Clase descendiente de otra. Hereda automáticamente los atributos y métodos de su superclase.
# Es una especialización de otra clase.
# Admiten la definición de nuevos atributos y métodos para aumentar la especialización de la
# clase.

# Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como
# responsabilidades la carga por teclado y su impresión.
# En el bloque principal del programa definir un objeto de la clase persona y llamar a
# sus métodos.

# Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un
# atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 30000)
# También en el bloque principal del programa crear un objeto de la clase Empleado.

# clase padre
class Persona:

    def __init__(self):
        self.nombre = input("Ingrese el nombre:")  # Atributos comunes
        self.edad = int(input("Ingrese la edad:"))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

# clase hija


class Empleado(Persona):  # hereda de la clase padre Persona

    # En el constructor de la clase hija invoco al constructor del padre
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo:"))  # Atributo particular

    def imprimir(self):
        super().imprimir()  # invoco al metodo imprimir del padre
        print("Sueldo:", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 30000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

persona1 = Persona()
persona1.imprimir()
print("-----------------------------------")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
