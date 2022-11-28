class Producto:
    def __init__(self, referencia, nombre, descripcion, precio):
        self.referencia = referencia
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return "Producto: {} - {} - {} - {}".format(self.referencia, self.nombre, self.descripcion, self.precio)


class Adorno(Producto):
    pass

# Comienza el programa


adorno = Adorno("2020", "Vasos", "Vasos de plástico", 10)
print(adorno)
