class Persona:
    contador_persona = 0
    def __init__(self,nombre,edad) -> None:
        self._nombre = nombre
        self._edad = edad
        self.contador_persona+=1
        self.__id_persona = self.contador_persona

    def __str__(self) -> str:
        return f'''nombre = {self._nombre}
edad = {self._edad}
id = {self.__id_persona}'''

    


persona1 = Persona('gonzalo',25)
print(persona1)
persona2 = Persona('jaun',42)
print(persona2)


