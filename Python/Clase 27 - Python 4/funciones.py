# Funciones en Python

'''
def imprimir():
    print("Hola mundo")


imprimir()

print("--------------------------")


def imprimir_n_veces(N):  # Funcion con parametro N
    for i in range(N):
        print("Hola mundo  veces")


cantidad = int(input("Ingrese cantidad de veces a imprimir: "))
imprimir_n_veces(cantidad)


def imprimir_n_textos(N, texto):
    for i in range(N):
        print(texto)


numero = int(
    input("Ingrese cantidad de veces a imprimir(numero no sea negativo): "))
while numero <= 0:
    print("Ingrese un numero positivo")
    numero = int(
        input("Ingrese cantidad de veces a imprimir(numero no sea negativo): "))
frase = str(input("Ingrese frase a imprimir: "))
imprimir_n_textos(numero, frase)



def multiplicar_por_n(n1, n2):
    print(f'El resultado de multiplicar por {n1} por {n2} es: {n1*n2}')


multiplicar_por_n(2, 3)



def saludo(nombre="Arturo", mensaje="Es mi nombre"):
    print(nombre, mensaje)


saludo()
saludo("Juan", "Otro mensaje")




def raiz(n, raiz=2):
    print(n**(1/raiz))  # raiz cuadrada de n


raiz(9)
raiz(27, 3)




def saludos(nombre="Arturo", mensaje="Hola"):
    print(nombre, mensaje)


saludos(mensaje="Todo bien?", nombre="Juancito") #Modifica la copia de la funcion
saludos("Juan")                                  #Parametro original



def sumar(n1, n2):
    suma = n1 + n2
    return suma


sumar(2, 3)  # Ver que la variable es local
print(sumar(2, 3))  # Imprime todo lo que pasa en sumar

resultado = sumar(5, 7)  # Guarda el resultado en una variable
print(resultado)




def numero_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(numero_par(2))  # Es numero par True
print(numero_par(3))  # Es numero impar False




def cuadrado_y_cubo(n):
    return n**2, n**3


cuadrado, cubo = (cuadrado_y_cubo(2))
print("El cuadrado del numero es", cuadrado)
print("El cubo del numero es", cubo)



def imprime_variable(nombre):
    nombre = "Arturo"  # Varible Local
    print(nombre)


nombre = "pepe"  # Variable Global
imprime_variable()

print(nombre)  # Imprime la variable global

nombre = "Juan"  # Modifica la variable global
print(nombre)
imprime_variable()


'''


def cubo(n):
    """Esta funcion me devuelve el cubo de un numero"""
    return n**3


print(cubo(3))
