#sumar los pares entre rangos dados

inicio = int(input('ingrese el primer numero'))
fin = int(input('fin'))
sumador =  0
for i in range(inicio, fin,1):
    print(i)
    if i % 2 == 0:
        sumador += i
print (sumador)