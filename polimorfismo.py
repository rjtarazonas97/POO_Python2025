from os import system
system("cls")

class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido()) 

gato = Gato()
perro = Perro()
""" 
print(gato.sonido())  # Salida: Miau
print(perro.sonido())  # Salida: Guau """

hacer_sonido(gato)  # Salida: Miau
hacer_sonido(perro)  # Salida: Guau
