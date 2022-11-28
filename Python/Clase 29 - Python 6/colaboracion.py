class Cliente:
    def __init__(self, nombre):
        self.monto = 0
        self.nombre = nombre

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(f'{self.nombre} tiene depositada la suma de {self.monto}')


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Arturo")
        self.cliente2 = Cliente("Maria")
        self.cliente3 = Cliente("Yanina")

    def operar(self):
        self.cliente1.depositar(10000)
        self.cliente2.depositar(50000)
        self.cliente3.depositar(100000)
        self.cliente3.extraer(30000)

    def depositos_totales(self):
        total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() \
            + self.cliente3.retornar_monto()
        print(f"El total de depositos es ${total}")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1 = Banco()  # Con esto instanciamos Banco y tambien Cliente
banco1.operar()
banco1.depositos_totales()
