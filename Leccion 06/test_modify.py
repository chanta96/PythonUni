class Atributo :
    def __init__(self,name) -> None:
        self._name = name
    
    def __str__(self) -> str:
        return self._name

persona1 = Atributo('gonzalo')
persona1._name = 'pepito'
print(persona1._name)