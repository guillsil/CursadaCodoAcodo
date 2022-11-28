class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def __del__(self):
        print("Se ha eliminado el empleado")

    def imprimir(self):
        print("Nombre del empleado: {}".format(self.nombre))
        print("Sueldo del empleado: {}".format(self.sueldo))

    def pagoImpuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("El empleado no debe pagar impuestos")


empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagoImpuestos()
