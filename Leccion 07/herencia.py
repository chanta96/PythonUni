class Persona:
    def __init__(self,nombre,apellido) -> None:
        self._nombre = nombre
        self._apellido = apellido
    
    def __str__(self) -> str:
        return f"""nombre : {self._nombre}
apellido : {self._apellido}"""
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,value):
        self._nombre = value
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,value):
        self._apellido = value
    

class Empleado(Persona):
    def __init__(self,nombre,apellido,sueldo):
        super().__init__(nombre,apellido)
        self._sueldo = sueldo

    def __str__(self) -> str:
        return f"""{super().__str__()} 
sueldo :{self._sueldo}
        """



empleado1 = Empleado('gonzalo', 'Gramajo',7500)
print(empleado1)