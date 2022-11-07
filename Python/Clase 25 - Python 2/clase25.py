# Vamos a hacer nuestro primer Hola Mundo!

print("Hola mundo desde Python!")

# Tipo de variables

'''esto es un
comentario que puede ser 
de mas de una linea'''

"""Esto tambien
Es un comentario en bloque"""

# Hola esto
# es un comentario

cadena = "Hola Mundo desde Variable!"  # Variable String
numero = 10  # Variable entero
flotante = 20.5  # Variable es float (Numero decimal)
booleando = False  # Variable booleana

print(cadena)

# Se respetan el +,-,*,/,%, **

multiplicacion = numero*flotante  # Variable flotante

print("El resultado de la multiplicacion es:",
      multiplicacion)

a = 10 + 52 + 54 + 26 + 26 \
    + 20 + 30 + 15 + 26 \
    + 25 + 15 + 35

print("El resultado de la suma es:", a)

lado = input("Ingrese el lado de un cuadrado:")

lado = int(lado)

area = lado*lado

print("El area de tu cuadrado es: ", area)


# Estructuras secuenciales

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

# num1 = int(num1)  alternativa

suma = num1 + num2

print("La suma de los dos numeros es:", suma)


# Estructuras condicionales

persona = input("ingrese el nombre de la persona:")
edad = int(input("ingrese la edad de la persona:"))

if edad < 18:
    print(persona)
    print("Es menor de edad")
else:
    print(persona)
    print("Es mayor de edad")

print("Se termino el programa!")
