# Creacion de una clase

class Persona:  # Clase va a ser el "sustantivo"
    def inicializar(self, nom):  # Metodo inicializar
        self.nombre = nom

    def imprimir(self):  # Metodo imprimir
        print(self.nombre)

# Termina nuestra clase con sus metodos


persona1 = Persona()
# Llamamos al metodo inicializar y le pasamos el parametro "Arturo"
persona1.inicializar("Arturo")
persona1.imprimir()

Persona2 = Persona()
Persona2.inicializar("Juan")
Persona2.imprimir()

Persona3 = Persona()
Persona3.inicializar("Laura")
Persona3.imprimir()
