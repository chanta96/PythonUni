#listas en python 
import os

my_list = ['ariel','gonzalo','pedro','pepe']
# print(my_list)
# my_list.append('pedrito')
# print(my_list)

#forma de empezar desde un indice del array,primer espacio indice inicial
#segundo espacio indice final, tercer espacio orden , delante hacia atras
#print(my_list[0:2])
#print(my_list[::-1])
#cambiamos un indice del array
my_list [2] = 'PEDRITO'
#print(my_list)

#tuplas python listas inmutables
cocina = ('Cuchara','Tenedor','Cuchillo')
#imprimir tupla en indice 1
#print(cocina[1])
#mostrar el largo de la tupla
#print(len(cocina))
#largo de la lista sin objetos repetidos
#print(len(set(cocina)))
#convertir la tupla a una lista
my_new_list = list(cocina)
#agregar objeto a la lista
my_new_list.append('Sarten')
cocina2 = tuple(my_new_list)
#mostrar nueva tupla
#print(cocina2)

cocina3 = ('papa')
#print(type(cocina3))

#recorrer elementos de una tupla
for cocinar in cocina:
    print(cocinar, end = 'cocina')

# *repaso de set
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('hola')
print(conjunto2)
conjunto1.add('hola')
conjunto3 = set()
conjunto3 = {'hola','chau',2,3}
conjunto4 = conjunto1 - conjunto2
print(conjunto4)

print('',end='-'*30)
print('')
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))
os.system('cls')

print('-'*70)
#repaso diccionarios


diccionario_nuevo = {'azul':'blue','rojo':'red','verde':'green','amarillo':'yellow'}
print(diccionario_nuevo)
print(sorted(diccionario_nuevo))

#los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'ariel':{'edad':40,'altura':1.83},
                'osvaldo':{'edad':35,'altura':1.63},
                'pepitos':{'edad':21,'altura':1.90}
                }
print(diccionario2)

print('*'*50)

#repaso set un set sirve para eliminar elementos repetidos de un array 
lsita = [1,4,1,2,3,5,6]
lista_nueva = set(lsita)
print (lista_nueva)

os.system('cls')
print('*'*50)

#colas con listas
#estructura de datos de tipo fifo (first input/first output)
cola = ['ariel','osvaldo','liliana','pilar']
cola.append('gonzalo')
cola.append('carlos')
cola.append('rebord')
print(cola)
for i in range(0,len(cola)):
    print('El siguiente paciente a atender es:',cola[-1])
    cola.pop()