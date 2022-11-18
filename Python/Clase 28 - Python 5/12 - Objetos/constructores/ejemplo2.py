# Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar 
# el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado),
# imprimir su perímetro y su superficie.

class Cuadrado:
    # constructor parametrizado
    def __init__(self,lado):
        self.lado=lado

    def mostrar_perimetro(self):
        per=self.lado*4
        print("El perimetro del cuadrado es:",per, "cms.")

    def mostrar_superficie(self):
        sup=self.lado*self.lado
        print("La superficie del cuadrado es:",sup,"cms. cuadrados")


# bloque principal

cuadrado1=Cuadrado(int(input('Ingrese el valor del lado:')))
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()