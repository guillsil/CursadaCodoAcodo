class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto+monto

    def extraer(self, monto):
        self.monto = self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre, self.monto))


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Pedro")
        self.cliente3 = Cliente("Maria")

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(2000)
        self.cliente3.depositar(3000)
        self.cliente1.extraer(500)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto()+self.cliente2.retornar_monto() + \
            self.cliente3.retornar_monto()
        print("El total de depositos es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1 = Banco()  # Tambien estamos llamando a la clase Cliente
banco1.operar()  # Tambien llamamos a depositar y extraer
banco1.depositos_totales()  # Tambien estamos llamando a retornar_monto e imprimir
