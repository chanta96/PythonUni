# ya se como funcionan las funciones xd


def show(name, last_name):
     print (name + ' ' + last_name)

person = ['ariel','betancud']
show(person[0], person[1])
person3 = {'last_name': 'natalia','name':'lucero'}
show(**person3)

for i in range(1, 4):
     print(i)
else:
     print('final de ciclos')

#list comprehesion
names = ['pablos','hernan','lucero','pedro']
alongP = [name_withp for name_withp in names if name_withp[0]== 'p' or name_withp[0]== 'P']
print(alongP)


def listarTerminos(**terminos): #realmente se utilizar **kwargs para recibir argumentos
     for key,value in terminos.items():
          print(key,':',value)

#funcionamiento correcto
listarTerminos(IDE='integrated development environment', PK = 'PRIMARY KEY') 
#falla 
# listarTerminos(10 = 'lionel messi', 20 = 'frezzi')

def desplegar_nombres(nombres):
     for nombre in nombres:
          print(nombre)

#funciona solamente enviando listas
desplegar_nombres(['pepe','carlos','hernan'])
#aca no funciona porque no es un objeto iterable
# desplegar_nombres(10)

# def factorial(numero):
#      if numero == 1:
#           return 1
#      else:
#           return numero * factorial(numero-1)
# print(factorial(5))
sumatoria = 1
numero_a_chequear = int(input('ingrese un numero mayor a 0'))
if numero_a_chequear >= 0 and numero_a_chequear < 2:
     if numero_a_chequear == 0:
          print('no hay factorial de 0')
     else:
          if numero_a_chequear ==1:
               print('el factorial de 1 es 1')
          else:
               print("el factorial de 2 es 2")
else:
     for i in range (2,numero_a_chequear+1):
          sumatoria *= i 
     print(sumatoria)

print('test python')
