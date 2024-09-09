# Importamos la clase figura para heredarla
from Figura import Figura
# Math nos sirve para operaciones donde suamos pi, pede ser remplazado por directamente usar 3.1416 pero creo que esta es la manera mas limpia de usarlo
import math

# Clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        if not isinstance(radio, (int, float)):
            raise TypeError("El radio debe ser numérico.") # Exepcion por si intentas meter una letra
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0.") # Eepcion por si intentas poner un numero menor a 0
        self.radio = radio

    # Metodo para calcular el area de un circulo solo con el radio
    def area(self):
        return math.pi * (self.radio ** 2) # hacemos Pi * lo que esta adentro de los parentisis que es radio y el doble ** quiere decir al o elevacin o ^ en este caso al cuadrado

    # Metodo para calcular el perimetro de un circulo solo con el radio
    def perimetro(self):
        return 2 * math.pi * self.radio #
