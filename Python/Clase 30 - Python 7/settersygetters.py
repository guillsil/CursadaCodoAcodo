class ListadoBebidas:

    def __init__(self):
        self.__bebida = "Gaseosa"

    @property
    def bebida(self):
        return "La bebida que no se podia modificar es: {}".format(self.__bebida)
        # return "La bebida     ----es", self.__bebida
        # return f"La bebida------- es {self.__bebida}""

    @bebida.setter
    def bebida(self, bebida):
        self.__bebida = bebida


bebida1 = ListadoBebidas()
print(bebida1.bebida)
bebida1.bebida = "Juguito"  # Modificar el atributo privado
print(bebida1.bebida)
