class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self._nombre = nombre
        self._sueldo = sueldo
    
    def __str__(self) -> str:
        return f'''nombre = {self._nombre}
sueldo = {self._sueldo}'''

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,value):
        self._nombre = value
    
    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, value):
        self._sueldo = value
    

if __name__ == '__main__':
    empleado1 = Empleado('gonzalo', 25000)
    print(empleado1)
