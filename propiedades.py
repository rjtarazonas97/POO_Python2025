class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):          # propiedad
        return self.__nombre
    
    @nombre.setter             # setter de la misma propiedad
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre


# --- Prueba ---
dalto = Persona("Lucas", 21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "Jesus"

nombre= dalto.nombre
print(nombre)

