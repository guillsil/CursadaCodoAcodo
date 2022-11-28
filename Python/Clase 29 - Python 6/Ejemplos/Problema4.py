class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print("Se ha eliminado el punto")

    def imprimir(self):
        print("Las coordenadas del punto: ({},{})".format(self.x, self.y))

    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("Estoy en el primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print("Estoy en el segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print("Estoy en el tercer cuadrante")
        else:
            print("Estoy en el cuarto cuadrante")


punto1 = Punto(-1, -2)
punto1.imprimir()
punto1.imprimir_cuadrante()
