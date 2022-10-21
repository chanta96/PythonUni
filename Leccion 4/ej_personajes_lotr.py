# agregar personajes del señor de los anillos con su raza y clase
# class PersonajesTolkien:
#     def __init__(self,nombre,clase,raza) -> None:
#         self._nombre = nombre
#         self._clase = clase
#         self._raza = raza
    
#     def __str__(self) -> str:
#         return f'Nombre: {self._nombre}\nclase: {self._clase}\nraza: {self._raza}'
    
#     def __repr__(self) -> str:
#         return str(self)

# personaje1 = PersonajesTolkien('Gandalf','Mago','istar')
# print(personaje1)
# personaje2 = PersonajesTolkien('Aragorn','Dunadain del norte','Guerrero')
# personaje3 = PersonajesTolkien('Legolas','Arquero','Elfo')
# lista = [personaje1,personaje2,personaje3]
# print(lista)

lista = [{'nombre':'Gandalf El Gris', 'Clase':'Mago', 'Raza':'istar'},
         {'nombre':'Aragorn Rey de Gondor', 'Clase':'Guerrero', 'Raza':'Dunadain del norte'},
         {'nombre':'Legolas Hoja Verde', 'Clase':'Arquero', 'Raza':'Elfo'},
         {'nombre':'Gimli Hijo De Gloin', 'Clase':'Herrero/Guerrero', 'Raza':'enano'},
         {'nombre':'Frodo Bolson', 'Clase':'Portador Del Anillo','Raza':'Hobbit'},
         {'nombre':'Bilbo Bolson', 'Clase':'Ladron Montador Del barril','raza':'Hobbit'}]
lista.append({'nombre':'Theoden Rey de Rohan', 'Clase':'Guerrero','raza':'Hombre'})

for i in range(len(lista)):
    print (lista[i])