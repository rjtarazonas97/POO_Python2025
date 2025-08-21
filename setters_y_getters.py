from os import system
system("cls")

# Setters y Getters en Python

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

jesus = Persona("Jesús", 28) # Esto es un objeto de la clase Persona

nombre = jesus.get_nombre()
print(nombre)  # Salida: Jesús

jesus.set_nombre("Juan")

nombre = jesus.get_nombre()
print(nombre)  # Salida: Juan