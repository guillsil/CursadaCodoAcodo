class Cliente:
    suspendidos = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def imprimir(self):
        print("Codigo: {}".format(self.codigo))
        print("Nombre: {}".format(self.nombre))
        self.esta_suspendido()

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("El cliente esta suspendido")
        else:
            print("El cliente no esta suspendido")
        print("-------------------------------")


cliente1 = Cliente(1, "Juan")
cliente2 = Cliente(2, "Pedro")
cliente3 = Cliente(3, "Maria")
cliente4 = Cliente(4, "Pablo")
cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print("Clientes suspendidos: {}".format(Cliente.suspendidos))
