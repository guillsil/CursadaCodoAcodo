class Mama:
    def llevar(self):
        print("Mamá me lleva a todos lados")


class Papa:
    def cocinar(self):
        print("Papá me cocina todas las noches")


class Hijo(Mama, Papa):
    def atributos(self):
        print("Tengo atributos y metodos propios, de Mama y de Papa")


hijo1 = Hijo()
hijo1.cocinar()
