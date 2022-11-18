# creación de una clase

class Persona:  # Clase es el sustantivo "Persona"
    def inicializar(self, nom):  # Definiendo el primer metodo
        self.nombre = nom

    def imprimir(self):  # Metodo para imprimir a las personas
        print(self.nombre)

# Termina nuestra clase y va a tener 2 metodos


persona1 = Persona()
# Llamar al metodo inicializar para pasar el parametro
# Y luego utilizar el metodo imprimir para renderizarlo en la consola

persona1.inicializar("Arturo")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Leandro")
persona2.imprimir()

persona3 = Persona()
persona3.inicializar("Flavia")
persona3.imprimir()
