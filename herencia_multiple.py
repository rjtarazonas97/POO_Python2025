from os import system
system("cls")

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
    
                
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre,edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def mostrar_habilidad(self):
        print(" No tengo xd")
    
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
        
        
        
        
# herencia.py

roberto = EmpleadoArtista("Roberto", 30, "Peruano","cantar", "Ingeniero", 3000)

herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(roberto,EmpleadoArtista)

print(herencia)