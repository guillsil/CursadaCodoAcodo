# Devolución de más de un valor con return

def elevacion(numero):
    return numero**2, numero**3


cuadrado, cubo = elevacion(3)  # Guardo el valor en 2 variables

print("3 al cuadrado es:", cuadrado)
print("3 al cubo es:", cubo)


# Me puede devolver tambien listas o tuplas

def tabla(numero):
    lista = []
    for i in range(11):
        lista.append(i*numero)
    return lista


print(tabla(5))

# Funcion anonima o lambda


def cubo(x): return x**3


print("2 elevado al cubo es igual a:", cubo(2))
