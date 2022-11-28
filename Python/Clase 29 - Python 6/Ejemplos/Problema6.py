class Alumnos:
    def __init__(self):
        self.nombre = []
        self.nota = []

    def __del__(self):
        print("Se ha terminado este programa")

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1-Cargar alumnos")
            print("2-Listar alumnos")
            print("3-Alumnos con nota mayor o igual a 7")
            print("4-Salir")
            opcion = int(input("Ingrese la opcion requerida: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.nota_mayor()
            else:
                self.finalizar()

    def cargar(self):
        for x in range(3):
            nombre = input("Ingrese el nombre del alumno: ")
            self.nombre.append(nombre)
            nota = int(input("Ingrese la nota del alumno: "))
            self.nota.append(nota)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(3):
            print(self.nombre[x], self.nota[x])
        print("-----------------")

    def nota_mayor(self):
        print("Listado de alumnos con nota mayor o igual a 7")
        for x in range(3):
            if self.nota[x] >= 7:
                print(self.nombre[x], self.nota[x])
        print("-----------------")

    def finalizar(self):
        print("Gracias por usar este programa")


lista1 = Alumnos()
lista1.menu()
