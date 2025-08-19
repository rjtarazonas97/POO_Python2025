from os import system
system("cls")

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")
        
        
Estudiante1 = Estudiante("Jesus", 28, "Noveno ciclo")
Estudiante1.mostrar_datos()
Estudiante1.mostrar_grado()