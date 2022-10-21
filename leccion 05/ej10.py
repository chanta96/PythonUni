#ej10
#hacer u programa que pida una cadena por teclado, 
#y luego meter los caracteres en una lista sin repetir
cadena = 'meriendadd'
# new_cadena = list(cadena)
# # print (set(new_cadena))
# new_cadena = ''.join(set(cadena))
# print (list(new_cadena))
cadena_sin_espacios = ''.join((cadena))
new_list = list()
for char in cadena_sin_espacios:
    if char not in new_list:
        new_list.append(char)

print (new_list)
        