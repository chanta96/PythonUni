# ejercicio 11 agenda telefonica
#hacer un programa que simule una agenda de contactos. crear un diccionario
# donde la clase sea el nombre del usuario y el valor 
# sea el telefono, el programa tendra el siguiente menu de opciones:
#     1-nuevo contacto
#     2-borrar Contacto
#     3- ver contactos existentes
#     4- salir
class Contacto:
    def __init__(self,nombre,telefono) -> None:
        self.nombre = nombre
        self.telefono = telefono
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} {self.telefono}'

class ListaContacto:
    
    def __init__(self) -> None:
        pass