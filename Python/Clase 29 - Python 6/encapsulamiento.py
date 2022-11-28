class Encapsulamiento:
    __atributo_privado = "Es un atributo que no se puede acceder desde fuera"

    def __metodo_privado(self):
        print("Soy metodo inaccesible desde afuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado


objeto1 = Encapsulamiento()
print(objeto1.atributo_publico())
objeto1.metodo_publico()
objeto1.__metodo_privado()
