import sys
print('Ejercicios estructura While')

print('Ejercicio 1 Imprimir los números del 1 al 10 ')
contador = 1
while contador < 11:  # contador =< 10
    print(contador)
    contador = contador + 1

sys.stdin.readline()
print('Ejercicio 2 Imprimir los números del 1 al 10 salteando de a 2 ')
contador2 = 1
while contador2 < 11:
    print(contador2)
    contador2 = contador2 + 2

sys.stdin.readline()
print('Ejercicio 3 Imprimir los números del 10 al 1 ')
contador3 = 10
while contador3 > 0:
    print(contador3)
    contador3 = contador3 - 1  # contador3 -= 1

sys.stdin.readline()
print('Ejercicio 4 Imprimir los números del 1 al 10 sin imprimir números 2,5 y 9 ')
contador4 = 1
while contador4 <= 10:
    if contador4 != 2 and contador4 != 5 and contador4 != 9:
        print(contador4)
    contador4 += 1

sys.stdin.readline()
print('Ejercicio 5 Imprimir los números del 1 al 30 sin imprimir números entre el 10 y el 20 ')
contador5 = 1
while contador5 <= 30:
    if contador5 < 10 or contador5 > 20:
        print(contador5)
    contador5 += 1

sys.stdin.readline()
print('Ejercicio 6 Imprimir la suma de los números del 1 al 10')
contador6 = 1
acumulador = 0
while contador6 <= 10:
    acumulador = acumulador + contador6  # acumulador += contador6
    contador6 += 1
print('La suma del 1 al 10 es igual a: ', acumulador)

sys.stdin.readline()
# Ejercicios Estructura While
print('Ejercicio 7 Imprimir la suma de los números pares del 1 al 25')
n = 1
acu = 0
while n < 25:
    if n % 2 == 0:
        acu = acu + n
    n = n + 1
print('la suma es = ', acu)

sys.stdin.readline()
print('Ejercicio 8 Imprimir la multiplicación de números impares que se encuentran entre el -10 y 10')
m = -10
acu = 1
while m < 10:
    if m % 2 == 1:
        acu = acu * m
    m = m + 1
print('la multiplicacion es = ', acu)

sys.stdin.readline()
print('Ejercicio 9 Imprimir la suma de los números pares mayores a 9 y menores a 20 que se encuentran entre el 1 y el 30')
q = 1
acu = 0
while q < 30:
    if q % 2 == 0 and q > 9 and q < 20:
        acu = acu + q
    q = q + 1
print('la suma es = ', acu)
