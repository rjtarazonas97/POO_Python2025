from os import system
system("cls")

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
        
        
        
# herencia.py

roberto = Empleado("Roberto", 30, "Peruano", "Ingeniero", 3000)

#print(f"Nombre: {roberto.nombre}, Edad: {roberto.edad}, Nacionalidad: {roberto.nacionalidad}")

roberto.hablar()