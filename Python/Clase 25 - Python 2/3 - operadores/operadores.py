import os
print('operadores aritmeticos: + - * /')

n1 = 10
n2 = 5

print('n1 + n2 = '+ str(n1 + n2))
print('n1 - n2 = ', n1 + n2)
print('n1 - n2 = ', n1 - n2)
print('n1 * n2 = ', n1 * n2)
print('n1 / n2 = ', n1 / n2)



print('operadores relacionales: >  <  >=  <=  ==   !=')

print (3==3)
print (3<3)
print (3<=3)
print (3!=4)

nombre1='juan'
nombre2='juana'
print (nombre1==nombre2)

nombre1='juan'
nombre2='JUAN'
print (nombre1==nombre2)

nombre1='juan'
nombre2='juan'
print (nombre1==nombre2)

# La comparacion no es case sensitive

print(5 == 5)#True
print(5 != 5)#False
print(5 >= 2)#True
print(5 < 1)#False


print('operadores incrementales: ')

n = 1
print('n = '+ str(n)) # n = 1

n += 1 # n = n + 1
print('n = '+ str(n)) # n = 2

n *= 6 # n = n * 6
print('n = '+ str(n)) # n = 12

n = n / 4 
print('n = '+ str(n)) # n = 3





print ('operadores logicos')
# Operadores Logicos
# Solo hay operadores Logicos

# and   (y)

# or    (o)

# not   (no)


# ------------------------------- 
#  tablas de verdad
# ------------------------------- 
# --------------------------
#   X   Y       Or      And
#   F   F       F       F
#   F   V       V       F
#   V   F       V       F
#   V   V       V       V


log1=True
log2=False
resultado=log1 and log2
print(resultado)

print(log1 or log2)
print(resultado or log2)
print(not log1)
log1 = not log2
print(log1)

# cuidado con el doble negado
print (not(not(True)))


print("mas operadores Logicos");
nro1 = 10
nro2 = 5
nro3 = 4
nro4 = 4
nro5 = 5
print(nro3 == nro4)
print(nro3 != nro4)
print(nro4 == nro5)

print("mas todavia")
print(nro3 > 4)
print(nro3 > 4 and nro1 > nro2)
print(nro3 > 0 and nro1 + nro2 == 10)

##Ingresar x teclado el dia de la semana y el clima.
##Si es un sabado lluvioso informar "Me quedo en casa",
##sino informar "Salgo"

## ingreso de datos
dia = input('decime el dia de la semana: ')

clima = input('lluvioso o despejado?: ')

#logica de decision
if(dia == 'sabado' and clima == 'lluvioso'):
    print('me quedo en casa!!')
#print('otra linea')
else:
    print('salgo de casa')
    
    
    
  





    




















































