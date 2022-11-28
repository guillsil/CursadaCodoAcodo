
# Atributos de instancia: Los atributos son independientes por cada objeto o instancia de la 
# clase, es decir si definimos tres objetos de la clase Persona, todas las personas tienen un 
# atributo nombre pero cada uno tiene un valor independiente:
import sys

class Persona:
    
    def __init__(self,nombre):
        self.nombre=nombre #atributo de instancia


# bloque principal

persona1=Persona("Juan")
persona2=Persona("Ana")
persona3=Persona("Luis")

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis

sys.stdin.readline()

# En algunas situaciones necesitamos almacenar datos que sean compartidos por todos los objetos 
# de dicha clase(por ejemplo, que todos los autos tengan la misma velocidad maxima), en esas 
# situaciones debemos emplear variables de clase.

# Para definir una variable de clase lo hacemos dentro de la clase pero fuera de sus métodos:
class Cliente:

    variable=20
    
    def __init__(self,nombre):
        self.nombre=nombre


# bloque principal

c1=Cliente("Juan")
c2=Cliente("Ana")
c3=Cliente("Luis")

print(c1.nombre) # Juan
print(c2.nombre) # Ana
print(c3.nombre) # Luis

print(c1.variable) # 20

#accedo a un atributo estatico a traves de la clase, sin crear ningun objeto
Cliente.variable=5 

print(Cliente.variable) # 5


