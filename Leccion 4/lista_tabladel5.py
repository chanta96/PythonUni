#lista del 1 al 10
lista = list(range(1,11))
num = int(input("que tabla desea comprobar?"))
desde = int(input("desde que numero?"))
hasta = int(input("hasta que numero?"))
for item in range(desde,hasta+1):
    print(f'{item} X {num} = {item*num}')