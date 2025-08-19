# Metodo de resolucion de orden de metodos (MRO)
# El MRO es el orden en que Python busca los metodos y atributos de una clase
# En Python, el MRO se determina utilizando el algoritmo C3 linearization
# El MRO se puede ver utilizando el metodo mro() de una clase
from os import system
system("cls")

class A:
    def hablar(self):
        print("Hola desde A")
        
class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")


d = D()

print(D.mro())  # Muestra el orden de resolucion de metodos
d.hablar()  # Llama al metodo hablar de la clase D
F.hablar(d)  # Llama al metodo hablar de la clase F
