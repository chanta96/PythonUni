year =  int(input("input the year to check for"))

if year <1582:
    print("leap numbers werent invented yet")
elif year %4 ==0 and year %100 ==0 and year % 400==0:
    print(f"{year} is leap year" )
else:
    print(f"{year} is not leap year" )
    
contador_positive = 0
contador_negative = 0
contador_cero = 0

for i in range(1,11):
    number = int(input("ingrese numero"))
    if number >0:
        contador_positive +=1
    elif number < 0:
        contador_negative +=1
    else: 
        contador_cero +=1

print(f"Contador positivo:   {contador_positive}")
print(f"Contador negativo:  {contador_negative}")
print(f"Contador cero:   {contador_cero}")

calif_promedio = 0
calif_baja = -1
for i in range(0,3):
    calificacion = int( input("ingrese la calificacion"))
    if calif_baja == -1:
        calif_baja = calificacion
    calif_promedio += calificacion
    if calificacion < calif_baja:
        calif_baja = calificacion

print (f"promedio = {calif_promedio/3}")
print (f"calificacion mas baja = {calif_baja}")
    