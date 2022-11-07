import sys

print("Ejercicio 1")
# Realizar un programa que imprima en pantalla los números del 0 al 20.
for x in range(21):
    print(x)

sys.stdin.readline()
print("Ejercicio 2")
# Realizar un programa que imprima en pantalla los números del 10 al 20.
for x in range(10,21):
    print(x)

sys.stdin.readline()
print("Ejercicio 3")
# Imprimir todos los números impares que hay entre 1 y 30
for x in range(1,30,2):
    print(x)


sys.stdin.readline()
print("Ejercicio 4")
# Desarrollar un programa que permita la carga de 10 valores por teclado y nos 
# muestre posteriormente la suma de los valores ingresados y su promedio.
suma=0
for f in range(10):
    valor=int(input("Ingrese valor: "))
    suma=suma+valor
print("La suma es ",suma)

promedio=suma/10
print("El promedio es: ",promedio)


sys.stdin.readline()
print("Ejercicio 5")
# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe 
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.
aprobados=0
reprobados=0

for f in range(10):
    nota=int(input("Ingrese la nota: "))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1

print("Cantidad de aprobados: ",aprobados)
print("Cantidad de reprobados: ",reprobados)


sys.stdin.readline()
print("Ejercicio 6")
# Codificar un programa que lea n números enteros y calcule la cantidad de 
# valores mayores o iguales a 50 
cantidad=0
n=int(input("Cuantos valores ingresará: "))
for f in range(n):
    valor=int(input("Ingrese el valor: "))
    if valor>=50:
        cantidad=cantidad+1
print("La cantidad de valores ingresados mayores o iguales a 50 son ",cantidad)












