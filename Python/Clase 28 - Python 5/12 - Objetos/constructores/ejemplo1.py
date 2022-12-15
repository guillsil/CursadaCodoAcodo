# El método __init__ es un método especial de una clase en Python. 
# El objetivo fundamental del método __init__ es 
# inicializar los atributos del objeto que creamos.

# El método __init__ se llama automáticamente. 
# Se ejecuta inmediatamente luego de crear un objeto.
# El método __init__ no puede retornar dato.
# el método __init__ puede recibir parámetros que se utilizan normalmente para 
# inicializar atributos.

# Crear una clase que represente un empleado. Definir como atributos su nombre y su sueldo. En el método __init__ 
# cargar los atributos por teclado y luego en otro método imprimir sus datos y 
# por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 50000 $)

class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>50000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
