# Crear una clase Cuenta y dos subclases CajaAhorro y PlazoFijo. Definir los atributos y métodos 
# comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.

# Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade 
# un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera 
# intereses.

# En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la 
# clase PlazoFijo.

class Cuenta:

    def __init__(self,titular,monto):
        self.titular=titular
        self.monto=monto

    def imprimir(self):
        print("Titular:",self.titular)
        print("Monto:",self.monto)


class CajaAhorro(Cuenta):

    def __init__(self,titular,monto):
        super().__init__(titular,monto)

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self,titular,monto,plazo,interes):
        super().__init__(titular,monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("Plazo en dias:",self.plazo)
        print("Interes:",self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):
        ganancia=self.monto*self.interes/100
        print("Importe del interes:",ganancia)

# bloque principal

cajaahorro=CajaAhorro("Juan", 2000)
cajaahorro.imprimir()

plazofijo=PlazoFijo("Carlos", 10000, 30, 0.75)
plazofijo.imprimir()