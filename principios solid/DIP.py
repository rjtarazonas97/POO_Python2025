# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar palabaras
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass
from os import system as sistema_limpio
sistema_limpio("cls") 
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
     
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #usamor el verificador para corregir texto
        pass
    
corrector = CorrectorOrtografico(Diccionario())