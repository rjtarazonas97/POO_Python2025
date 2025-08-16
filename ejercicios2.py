from os import system as sistema_limpio
sistema_limpio("cls")

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando...")
        
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)
print(f""" 
      Datos del estudiante: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
        
      """)
while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()