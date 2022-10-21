#!crear una lista con numeros ingresados por usuario hasta ingresar un 0

lista = []

salir = False
i=0
while not salir:
    num=(float(input('ingrese un numero')))
    if num == 0:
        salir = True
        break
    else:
        lista.append(num)

print(sorted(lista))