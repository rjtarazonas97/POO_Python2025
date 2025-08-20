from os import system
system("cls")

class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
        
class Murcielago(Ave, Mamifero):
    pass

murcielago = Murcielago()

murcielago.comer()  # Llama al metodo comer de la clase Animal
murcielago.volar()  # Llama al metodo volar de la clase Ave
murcielago.amamantar()  # Llama al metodo amamantar de la clase Mamifero

print(Murcielago.mro())  # Muestra el orden de resolucion de metodos