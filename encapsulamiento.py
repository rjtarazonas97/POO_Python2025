from os import system
system("cls")

# Encapsulamiento en Python

class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"
        
    def __hablar(self): # Método privado con doble guion bajo
        print("Hola, soy un método privado")

objeto = MiClase()
print(objeto.__hablar())  # Acceso permitido, pero no recomendado


#Atributo privado con doble guion bajo

class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"
        
objeto = MiClase()
print(objeto.__atributo_privado)  # Esto generará un error