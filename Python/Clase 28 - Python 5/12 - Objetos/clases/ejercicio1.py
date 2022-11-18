# Una clase es una plantilla (molde), que define atributos (variables) y métodos (funciones).

# La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada 
# objeto tendrá sus propios valores y compartirán las mismas funciones.

# Debemos declarar una clase antes de poder crear objetos (instancias) de esa clase. Al crear 
# un objeto de una clase, se dice que se crea una instancia de la clase o un objeto propiamente 
# dicho.

# Creamos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos 
# (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método 
# mostrará en la pantalla el contenido del mismo.

# Todo método tiene como primer parámetro el identificador self que tiene la referencia del 
# objeto que llamó al método.

# Luego dentro del método diferenciamos los atributos del objeto antecediendo el identificador 
# self.

# Con la asignación previa almacenamos en el atributo nombre el parámetro nom, los atributos 
# siguen existiendo cuando finaliza la ejecución del método. Por esto, cuando se ejecuta el 
# método imprimir podemos mostrar el nombre que cargamos en el primer método.

# self (Python) = this (Java)

class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre:",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()