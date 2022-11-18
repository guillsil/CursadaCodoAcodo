# Definiciones de Listas (Los arrays de python)

cursos = ['HTML', 'JS', 'PYTHON']  # Arrancamos desde 0
numeros = [0, 59, 77, 6, 25, 0]
vacio = []

print(cursos[1])  # JavaScript
print(cursos[-1])  # Me va a ir al ultimo
print(cursos[-2])  # JS
# print(cursos[-4])  # Error
print(cursos)  # Lista completa

for i in numeros:
    print(i)

x = 0
while x < len(numeros):
    print(numeros[x])
    x += 1

# max, min y sum

print(min(numeros))
print(max(numeros))
print(sum(numeros))

# Agregar elementos append y insert (lugar,elemento)

cursos.append("DJANGO")
cursos.insert(1, "CSS")

print(cursos)

# Borrar elementos pop y remove

cursos.pop()
cursos.remove("HTML")

print(cursos)

#Count, reverse, index

print(numeros.count(0))  # Cuenta cuantos ceros hay
numeros.reverse()  # Me los invierte
print(numeros)

print(numeros.index(77))  # Me dice en que posicion está 77

# sort

numeros.sort()
print(numeros)

numeros.clear()

# Pasamos a diccionarios

diccionarios = {'Arturo': 36, 'Juan': 55, 'Betina': 18}

print(diccionarios.keys())

for i in diccionarios.keys():
    print(diccionarios[i])

for clave, valor in diccionarios.items():
    print(clave, ':', valor, end=';')


# Tuplas

tupla = (2, 5, 57, 46)

print(tupla[:])
