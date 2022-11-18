class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre del alumno: {}".format(self.nombre))
        print("Nota del alumno: {}".format(self.nota))

    def esAprobado(self):
        if self.nota >= 7:
            print("El alumno está aprobado")
        else:
            print("El alumno está reprobado")

# Termina la parte de definicion


alumno1 = Alumno()
alumno1.inicializar("Laura", 7)
alumno1.imprimir()
alumno1.esAprobado()

alumno2 = Alumno()
alumno2.inicializar("Juan", 3)
alumno2.imprimir()
alumno2.esAprobado()
