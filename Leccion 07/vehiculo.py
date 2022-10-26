""""
definir una clase padre llamada vehiculo y dos clases hijas llamadas auto y bicicleta, las cuales
heredan de la clase padre llamada vehiculo, la clase padre debe tener los sig atributos

vehiculo (clase padre)
atrib = color, ruedas
metodos = init, str

auto = hija de vehiculo
atrib = vel km/h
metodos = init str

bicicleta = hija vehiculo
atrib = tipo de bicicleta
metodos = init str

crear una instancia de cada clase
"""

class Vehiculo():
    def __init__(self,color,ruedas):
        self._color = color
        self._ruedas = ruedas
    def __str__(self) -> str:
        return f"""Cantidad de ruedas : {self._ruedas}
Color: {self._color}
"""
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color = value
    
    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self,value):
        self._ruedas = value


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self._tipo = tipo
    
    def __str__(self) -> str:
        return f"""{super().__str__()}tipo : {self._tipo} 
        """
    
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,value):
        self._tipo = value


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self._velocidad = velocidad
    
    def __str__(self) -> str:
        return f"""{super().__str__()}velocidad = {self._velocidad}km/h
"""
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,value):
        self._velocidad = value
    

auto1 = Auto("Rojo",4,180)
bicicleta1 = Bicicleta("Azul",2,180)
print(auto1)
print(bicicleta1)
