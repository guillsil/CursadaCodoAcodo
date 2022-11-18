print("Ejercicio 1")
# Crear una función que le enviemos como parámetro el valor del lado de un cuadrado y 
# nos retorne su superficie

# definicion de la funcion
def retornar_sup(lado):
    sup=lado*lado
    return sup

# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuadrado: "))
superficie=retornar_sup(va)
print("La superficie del cuadrado es ",superficie)


import sys
sys.stdin.readline()
# espera a presionar una tecla para continuar
print("Ejercicio 2")
# Crear una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor


valor1=int(input("Ingrese el primer valor: "))
valor2=int(input("Ingrese el segundo valor: "))
print("El mayor es: ",retornar_mayor(valor1,valor2))

sys.stdin.readline()
print("Ejercicio 3")
# Crear una función que le enviemos como parámetro un string y nos retorne la cantidad 
# de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado 
# y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras 
# tiene más caracteres.
def largo(cadena):
    return len(cadena)


nombre1=input("Ingrese primer nombre: ")
nombre2=input("Ingrese segundo nombre: ")
la1=largo(nombre1)
la2=largo(nombre2)
if la1==la2:
    print("Los nombres: ",nombre1,nombre2," tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nombre1," es mas largo")
    else:
        print(nombre2," es mas largo")


sys.stdin.readline()
print("Ejercicio 4")
# Crear una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
def retornar_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)//3
    return promedio


valor1=int(input("Ingrese primer valor: "))
valor2=int(input("Ingrese segundo valor: "))
valor3=int(input("Ingrese tercer valor: "))
print("Valor promedio de los tres numeros: ", retornar_promedio(valor1,valor2,valor3))

sys.stdin.readline()
print("Ejercicio 5")
# Crear una función que nos retorne el perímetro de un cuadrado pasando como parámetros el 
# valor de un lado.
def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


lado=int(input("Lado del cuadrado: "))
print("El perimetro es: ",retornar_perimetro(lado))


sys.stdin.readline()
print("Ejercicio 6")
# En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual 
# de los dos tiene una superficie mayor.
def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


print("Primer rectangulo")
lado1=int(input("Ingrese lado menor del rectangulo: "))
lado2=int(input("Ingrese lado mayor del rectangulo: "))
print("Segundo rectangulo")
lado3=int(input("Ingrese lado menor del rectangulo: "))
lado4=int(input("Ingrese lado mayor del rectangulo: "))

if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los dos rectangulos tiene la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")




sys.stdin.readline()
print("Ejercicio 7")
# Crear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad 
# de letras 'a' o 'A'.
def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant


palabra=input("Ingrese una palabra: ")
print("La palabra ",palabra," tiene ",cantidad_vocal_a(palabra)," a")


sys.stdin.readline()
print("Ejercicio 8")
# Crear una función que reciba el nombre de un operario, el pago por hora y la cantidad de 
# horas trabajadas. Debe mostrar su sueldo y el nombre. 
def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre," trabajo ",cantidadhoras," y cobra un sueldo de ",sueldo)


calcular_sueldo("juan",10,120)
# le paso a la funcion parametros por defecto
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7)


