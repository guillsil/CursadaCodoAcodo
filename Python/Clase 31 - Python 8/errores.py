# Syntax error ---> error de sintaxis

# print("Hola mundo con errores!"

# Error de indentacion

# def dejarIndentacion(self):
#print("Que tipo de error voy a tener aca?")

# type error --->error de tipo

#numero1 = 1
# numero2 = input("Ingrese un numero para sumar:")    #Si no lo transformamos devuelve string

#print("El resultado de la suma de num1 y num2 es :", numero1+numero2)

# Error de nombre

#ptint("Hola mundo!!!")

# Error matematico----> zerodivision
# print(5/0)    no podemos dividir por cero

# index error ----> error semantico

#lista = []
# lista.pop()


# Excepciones

while(True):
    try:
        n = float(input("Ingresa un numero:"))
        m = 50
        print("{}/{}={}", n, m, m/n)

    except:
        print("Se produjo un error, fijese bien los numeros que ingresa")
    else:
        print("La division fue correcta y sin errores")
        break
    finally:
        print("Finalizado de programa!")
