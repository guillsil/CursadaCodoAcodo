# Definicion de funciones

def saludo_repetido(N):
    for i in range(N):
        print("Hola mundo desde funcion!")  # Definicion e instrucciones


cantidad = int(
    input("Ingrese la cantidad de veces quiere imprimir el mensaje"))

saludo_repetido(cantidad)


def saludar(nombre, apellido):
    print("El nombre ingresado es " + nombre +
          " y el apellido es "+apellido)


a = input("Ingrese su nombre")
b = input("Ingrese su apellido")

saludar(a, b)


def multiplicacion_n1_por_n2(n1, n2):
    print(f'El resultado de multiplicar {n1} por {n2} es: {n1*n2}')


multiplicacion_n1_por_n2(5, 3)


# parametros opcionales

def sumar(a=5, b=10):
    return a+b


print(sumar())
print(sumar(1, 1))

# Parametros posicionales


def potencia(base, exponente=2):
    return base**exponente


print(potencia(2))
print(potencia(base=2))
print(potencia(exponente=3, base=2))
print(potencia(3, 3))


def es_par(numero):
    if numero % 2 == 0:
        return print("Numero es par")
    else:
        return print("Numero no es par")


es_par(555)
