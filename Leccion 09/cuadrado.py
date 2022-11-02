from color import Color
from figuraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica,Color):
    """
    constructor de clase llamando a los atributos de las clases figuraGeometrica
    y Color
    """
    def __init__(self, alto,ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self,color)
    """
    definicion de metodo str llamando al metodo str de figuraGeometrica y Color
    """
    def __str__(self) -> str:
        return f'''{FiguraGeometrica.__str__(self)}
{Color.__str__(self)}'''

    def calcular_area(self):
        return self._alto * self._ancho



if __name__ == '__main__':
    cuadrado1 = Cuadrado(4,4,'rojo')
    cuadrado1.color = 'violeta'
    print(cuadrado1.calcular_area())
    