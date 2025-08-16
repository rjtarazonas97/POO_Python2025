from os import system as sistema_limpio
sistema_limpio("cls")

""" celular1_marca = "Samsung"
celular2_marca = "Apple"
celular3_marca = "huawei"

celular1_modelo = "Galaxy S21"
celular2_modelo = "iPhone 13"
celular3_modelo = "P40 Pro"

celular1_camaraF = "108 MP"
celular2_camaraF = "12 MP"
celular3_camaraF = "50 MP"

celular1_camaraT = "10 MP"
celular2_camaraT = "12 MP"
celular3_camaraT = "8 MP" """

""" celulares = []

celulares[0] = [ "Samsung", "Galaxy S21", "108 MP", "10 MP" ] """

""" # Defini la clase con PascalCase y los atributos con snake_case
# Utiliza el constructor __init__ para inicializar los atributos
class Celular():
    # Atributos
    marca = "Samsung"
    modelo = "Galaxy S21"
    camara = "108 MP"

# Esto es el objeto de la clase Celular
# Se crea una instancia de la clase Celular 
celular1 = Celular()
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

print(celular3.modelo) """


# Clase celular 
# Es un constructor que se utiliza para crear objetos de la clase Celular
# Las clases se definen con la palabra clave class y el nombre
class Celular:
    # Self hace referencia al objeto que se está creando a si mismo
    # Esto es un metodo especial que se utiliza para inicializar los atributos de la clase
    # Toda funcion que creemos dentro de una clase es un metodo de la clase
    def __init__(self, marca, modelo, camara):
        # marca, modelo y camara son los atributos de la clase Celular
        # Se inicializan los atributos con los valores que se pasan al crear el objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas haciendo una llamada desde un: {self.modelo} " )

    def cortar(self):
        print(f"Estas cortando la llamada desde un: {self.modelo} " )

#Objetos 
celular1 = Celular("Samsung", "Galaxy S21", "108 MP")
celular2 = Celular("Apple", "iPhone 13", "12 MP")
celular3 = Celular("Huawei", "P40 Pro", "50 MP")

celular2.cortar()