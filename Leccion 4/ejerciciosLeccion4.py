#ejercicio 1 for con numeros divisibles entre 3 

for i in range (11):
    if i % 3 == 0:
        print(i)
print('-'*50)
#ejercicio 2 numeros de 2 a 6
for i in range (2,7):
    print(i)
print('-'*50)

#ejercicio 3 crear un rango de 3 a 10 pero con incrementos de a 2

for i in range( 3, 11, 2):
    print(i)

print("-"*50)

# dada la siguiente tupla
tupla  = (13,1,8,3,2,5,8)
#crear una lista que solo muestre numeros menores a 5 

tuplas = list(tupla)
new_list = []
for num in tupla:
    if num < 5 :
        new_list.append(num)
print(new_list)