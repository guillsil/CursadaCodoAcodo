# El encapsulamiento consiste en denegar el acceso a los atributos y métodos internos de la clase 
# desde el exterior. En Python no existe, pero se puede simular precediendo atributos y métodos 
# con dos barras bajas __ 

# En el caso de los atributos quedarían así:

# class Ejemplo:
#     __atributo_privado = "Soy un atributo innacesible desde otra clase."

# e = Ejemplo()
# print(e.__atributo_privado)

# Y en los métodos...

# class Ejemplo:
#     def __metodo_privado(self):
#         print("Soy un método inalcanzable desde fuera.")

# e = Ejemplo()
# e.__metodo_privado()

# En Python no tiene sentido, porque se pierde la esencia del lenguaje: flexibilidad

# Para acceder a esos datos se deberían crear métodos públicos que hagan de interfaz. 
# En otros lenguajes les llamaríamos getters y setters y es lo que da lugar a las propiedades, 
# que no son más que atributos protegidos con interfaces de acceso.

class Ejemplo:
    __atributo_privado = "Soy un atributo innacesible desde fuera."

    def __metodo_privado(self):
        print("Soy un método innacesible desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()