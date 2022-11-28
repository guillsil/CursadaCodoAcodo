# Python soporta la creación de clases abstractas, no al menos de forma nativa. Por ello
# desde la versión la 2.6 se agrego el modulo abc (Abstract base classes) a la librería
# estándar de Python.

# Las librerías que utilizamos son una serie de archivos con código, a los cuales tenemos
# acceso. Esto en ocasiones es un problema, ya que el cliente (el que utiliza la librería)
# podría alterar de alguna manera un objeto primordial.

# Al crear una librería, estamos creando una relación con el usuario, el cual la utilizara
# para crear un programa u otra librería. En toda relación es importante tener fronteras que
# todas las partes respeten.

# Para ello es importante utilizar la Abstracción de Datos, una caracteristica muy importante
# de la Programación Orientada a Objetos.

# Una clase abstracta no puede crear objetos(se la suele usar para organizar el arbol de
# herencia). Por eso, necesita extender o heredar en otras clases hijas que puedan instanciar
# objetos.

# Ejemplo:
# Para crear las clases abstractas, antes debemos importar la librería abc y la clase ABC.

# Como se puede ver en el ejemplo, a la clase con la que se trabajara (Animal), se hereda
# la clase ABC, esto es necesario para decirle a Python que la clase Animal es abstracta y
# no se podrán crear instancias de estas.

# Luego, para definir que los métodos sean abstractas utilizamos el decorador de abc
# @abc.abstractmethod, esto para todos los métodos que sean necesarios.

import abc
from abc import ABC

# Declaramos nuestra clase


class Animal(ABC):

    # Primer método
    # Decorador para métodos absctractos
    @abc.abstractmethod
    def setName(self, name):
        self.name = name

    # Segundo método
    # Decorador para métodos absctractos
    @abc.abstractmethod
    def getName(self):
        return self.name

    # Bloque principal
    animal = Animal()
    print("Hola")

    # Al intentar crear una instancia, Python nos lanza un error, indicándonos que no se
    # puede crear una instancia de Animal ya que esta es una clase abstracta.
