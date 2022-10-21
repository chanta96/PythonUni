# ejercicio 11 agenda telefonica
#hacer un programa que simule una agenda de contactos. crear un diccionario
# donde la clase sea el nombre del usuario y el valor 
# sea el telefono, el programa tendra el siguiente menu de opciones:
#     1-nuevo contacto
#     2-borrar Contacto
#     3- ver contactos existentes
#     4- salir

def menu():
    def agregar_contacto(diccionario,nombre,telefono):
        diccionario[f'{nombre}'] = f'{telefono}'
        print(end='*'*50)

    def eliminar_contacto(diccionario,nombre):
        if nombre != diccionario.keys():
            print('contacto inexistente')
            print(end='*'*50)
        else:    
            del diccionario[f'{nombre}']
            print(end='*'*50)

    def mostrar_diccionario(diccionario):
        for key,value in diccionario.items():
            print(key,':',value)
        print(end='*'*50)
        
    agenda = {}
    salir = 0
    while not salir:
        print('\n1-agregar contacto')
        print('2-borrar contacto')
        print('3-mostrar contactos')
        print('4-salir')
        option = int(input())
        if option == 1:
            agregar_contacto(agenda,input('ingrese el nombre'),input('ingrese el numero de telefono')) 
        if option ==2:
            eliminar_contacto(agenda,input('ingrese el nombre'))
        if option == 3:
            mostrar_diccionario(agenda) 
        if option == 4:
            print('hasta luego')
            salir = True
            break

menu()