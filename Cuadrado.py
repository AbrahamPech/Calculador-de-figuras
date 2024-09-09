# Importamos la clase figura para heredarla
from Figura import Figura

# Clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        if not isinstance(lado, (int, float)):
            raise TypeError("El valor del lado debe ser numérico.") # Exepcion por si intentas meter una letra
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que 0.") # Eepcion por si intentas poner un numero menor a 0
        self.lado = lado

    # Metodo para calcular el area de un cuadrado solo con el radio
    def area(self):
        return self.lado ** 2

    # Metodo para calcular el perimetro de un cuadrado  solo con el radio
    def perimetro(self):
        return 4 * self.lado
