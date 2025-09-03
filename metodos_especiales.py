from os import system
system("cls")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Personal(nombre ={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)
    
        # Sobre carga de operadores hay mas modelos de diferentes formas de hacer
        
dalto = Persona("Lucas",21)
pedro = Persona("Pedro",30)
maria = Persona("maria",30)

nueva_persona = dalto + pedro + maria
print(nueva_persona.edad)