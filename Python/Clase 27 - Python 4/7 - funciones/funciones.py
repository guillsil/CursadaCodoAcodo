##funciones
## defino la funcion
def saludar():
    print('Hola Mundo!!!')

## uso o invoco o llamo a la funcion
saludar()
saludar()
saludar()

print('--------------------------------')

def saludar2(quien):
    print('Hola ' + quien + ' !!')

saludar2('Juan Perez')
saludar2('Maria Garcia')

print('--------------------------------')

def saludar3(nombre,apellido):
    print('Tu nombre es: '+ nombre + ' y tu apellido es: '+ apellido)

saludar3('Carlos','Gomez')
saludar3('Carla','Gimenez')

print('--------------------------------')

def saludar4(nombre,apellido,edad):
    print('Tu nombre es: '+ nombre + '  tu apellido es: '+ apellido+ ' y tu edad es de: '+ str(edad)+ ' años')

saludar4('Carlos','Gomez',20)
saludar4('Carla','Gimenez',30)


print('--------------------------------')

def saludar5(nombre,apellido,edad):
    print('Tu nombre es: '+ nombre + '  tu apellido es: '+ apellido+ ' y tu edad es de: '+ str(edad)+ ' años')

n = input('Cual es tu nombre?: ')
a = input('Cual es tu apellido?: ')
e = int(input('Cual es tu edad?: '))

saludar5(n,a,e)

print('--------------------------------')

def saludar6():
    nombre = input('Cual es tu nombre?: ')
    apellido = input('Cual es tu apellido?: ')
    edad = int(input('Cual es tu edad?: '))
    print('Tu nombre es: '+ nombre + '  tu apellido es: '+ apellido+ ' y tu edad es de: '+ str(edad)+ ' años')

saludar6()


print('--------------------------------')

def saludar7(nombre):
    print('Hola')
    return 'Hola '+ nombre + ' !!'
    print('Chau')

##print(saludar7('Luis'))

resultado = saludar7('Luis')
print(resultado)























