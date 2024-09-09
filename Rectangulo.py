# Importamos la clase figura para heredarla
from Figura import Figura

# Clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, base=0, altura=0):
        if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
            raise TypeError("Base y altura deben ser numéricos.")
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que 0.")
        self.base = base
        self.altura = altura

    # Metodo para calcular el area de un Rectangulo solo con el radio
    def area(self):
        return self.base * self.altura

    # Metodo para calcular el perimetro de un Rectangulo solo con el radio
    def perimetro(self):
        return 2 * (self.base + self.altura)
