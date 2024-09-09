# Importamos la clase figura para heredarla
from Figura import Figura

# Clase Triangulo que hereda de Figura
class Triangulo(Figura):
    def __init__(self, base, altura):
        if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
            raise TypeError("Base y altura deben ser numéricos.")
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que 0.")
        self.base = base
        self.altura = altura

    # Metodo para calcular el area de un triangulo solo con el radio
    def area(self):
        return (self.base * self.altura) / 2

    # Metodo para calcular el perimetro de un triangulo solo con el radio
    def perimetro(self):
        return 3 * self.base
