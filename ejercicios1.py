from os import system as sistema_limpio
sistema_limpio("cls")

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
Pedro = Estudiante ("Pedro", 20, "10th")
print(f"Nombre: {Pedro.nombre}, Edad: {Pedro.edad}, Grado: {Pedro.grado}")