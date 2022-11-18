# creación de una clase cargando nombre y tambien edad
# imprimir datos en pantalla
# ver si las personas son mayor de edad o no

class Persona:  # Clase es el sustantivo "Persona"
    def inicializar(self, nombre, edad):  # Definiendo el primer metodo
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):  # Metodo para imprimir a las personas
        print("El nombre de la persona es:", self.nombre)
        print(f"La edad de la persona es: {self.edad}")

    def esMayor(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor.")


# Termina nuestra clase y va a tener 2 metodos


persona1 = Persona()
# Llamar al metodo inicializar para pasar el parametro
# Y luego utilizar el metodo imprimir para renderizarlo en la consola

persona1.inicializar("Arturo", 36)
persona1.imprimir()
persona1.esMayor()

persona2 = Persona()
persona2.inicializar("Leandro", 15)
persona2.imprimir()
persona2.esMayor()

persona3 = Persona()
persona3.inicializar("Flavia", 25)
persona3.imprimir()
persona3.esMayor()


persona1.nombre = "Juancito"
persona1.imprimir()
