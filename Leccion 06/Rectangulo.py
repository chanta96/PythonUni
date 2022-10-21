class Rectangulo:
    def __init__(self,altura,base) -> None:
        self._altura = altura
        self._base = base
    
    @property
    def altura(self):
        return self._altura
    @property
    def base(self):
        return self._base
    @altura.setter
    def altura(self,value):
        self._altura = value
    
    @base.setter
    def base(self,value):
        self._base = value
    
    def __str__(self) -> str:
        return f'altura = {self.altura}\nbase = {self.base}'
    
    def calcular_area(self):
        return f'area del rectangulo : {self.altura*self.base}'

obj1 = Rectangulo(2,3)
print(obj1.calcular_area())