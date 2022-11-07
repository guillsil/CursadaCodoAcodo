import random
import sys
print("Estructura IF")

nombre = 'juan'
edad = 16
if edad < 18:
    print(nombre)
    print(' es menor de edad.')
print('Fin del programa')
# La tabulacion es la que indica el inicio de una estructura


sys.stdin.readline()
print("Estructura IF con else")

nombre = 'juan'
edad = 19
print(nombre)
if edad < 18:
    print(' es menor de edad.')
else:
    print(' es mayor de edad.')
print('Fin del programa')
# La tabulacion es la que indica el inicio de un bucle


sys.stdin.readline()
print("condicional con random")
# importe la libreria ramdom
print(random)
# miro la ruta de la libreria

x = random.randint(1, 20)
print(x)
print('----------------')

if x < 10:
    print('El valor generado tiene un digito')
else:
    print('El valor generado tiene dos digitos')


sys.stdin.readline()
print("otro condicional")
a = 4

if a < 5:
    print('1')
    print('2')
    print('3')
    print('4')
    print('5')
else:
    print('6')
    print('7')
    print('8')
    print('9')
    print('10')
print('-- fin estructura IF --')


# La tabulacion (Identacion) es obligatoria
sys.stdin.readline()
print("otro condicional mas")
a = 10

if a < 5:
    print('1')
print('2')
print('3')
print('4')
print('5')


sys.stdin.readline()
print("Estructura IF anidada")

print('')

x1 = random.randint(1, 100)
x2 = random.randint(1, 100)
x3 = random.randint(1, 100)
print(x1)
print('-')
print(x2)
print('-')
print(x3)
print('')
print('El mayor es:')
if x1 > x2:
    if x1 > x3:
        print(x1)
    else:
        print(x3)
else:
    if x2 > x3:
        print(x2)
    else:
        print(x3)


sys.stdin.readline()
print("Estructura IF anidada 2")
x = random.randint(1, 1000)
print(x)
print('')
if x < 10:
    print('Tiene 1 dígito')
else:
    if x < 100:
        print('Tiene 2 dígitos')
    else:
        if x < 1000:
            print('Tiene 3 dígitos')
        else:
            print('Tiene 4 dígitos')


sys.stdin.readline()
print("Uso de elif")
x = random.randint(1, 1000)
print(x)
print('')
if x < 10:
    print('Tiene 1 dígito')
elif x < 100:
    print('Tiene 2 dígitos')
elif x < 1000:
    print('Tiene 3 dígitos')
else:
    print('Tiene 4 dígitos')


sys.stdin.readline()
print("Uso de elif 2")
nota = 7
print('Nota:')
print(nota)
print('')
if nota >= 9:
    print('Promocionado')
elif nota >= 4:
    print('Regular')
else:
    print('Reprobado')
