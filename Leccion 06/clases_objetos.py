class Persona:
    def __init__(self,nombre,apellido,edad,*args,**kwargs) -> None:
        self._nombre = nombre
        self._edad = edad
        self._apellido = apellido
        self._args = args
        self._kwargs = kwargs

    def __str__(self): #segun el profesor self es igual a this
        return (f'{self._nombre}:{self._edad}:{self._apellido}')
    
    def mostrar_detalles(self):
        print(f'{self._nombre} - {self._apellido} - {self._edad} - {self._args} - {self._kwargs}')

persona1 = Persona('Gonzalo',25,'Gramajo')

print(persona1)
persona2 = Persona('Ariel','Betancud',35)
print(f'nombre :{persona2._nombre} - edad :{persona2._edad} apellido :{persona2._apellido}')
print (persona2)
persona1.mostrar_detalles()

persona2.telefono = '1151234123'
print(f'{persona2.telefono}')
persona3 = Persona('Rogelio',25,'Romero' ,'calle lopez', 823 , 'manzana',77,'casa',18, Altura = 1.82, Peso = 105, CFavorito = 'azul',Auto = 'Citroen',Modelo = 2021)
print(persona3.mostrar_detalles())
persona3._nombre = 'Gonzalo'
print(persona3.mostrar_detalles())

# persona3._nombre = 'gonzalo'
# print(persona3._nombre()) esta parte del codigo no funciona porque se necesita un getter y setter
