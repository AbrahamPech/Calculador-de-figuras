from abc import ABC, abstractmethod

# Clase principal que creamos para todas las figuras geometricas
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
