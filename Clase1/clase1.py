"""hola
xd
# Clase 1
print("Clase 1 :")  # Primeras lineas de codigo en python
print("Hello world")
print("Fin clase 1")
print(" ")

# Clase 2
print("Clase 2 :")  # Variables, dinamicas en python
variable = 3  # variante definida como int
print(variable)
variable = "cambio de valor de la variable"  # cambio a string
print(variable)
variable = 3.5  # cambio a float
print(variable)
x = 10
y = 2
z = x + y
print(z)  imprime resultado
print("Posicion de variable x en  ram :", id(x))  #funcion para mostrar la literal de X 
# caso (posicion de X guardada en la memoria RAM (donde se guardo el valor de X en la MEMORIA , la direccion
# de la memoria))
print(id(y)=  
print(id(z))
# x+ultimos digitos de la memoria (ejemplo z = x024)
print("Fin clase 2")
print(" ")

# Clase 3
print("Clase 3 :")  # Tipos de datos
variableTipoString = "hello there"
print(type(variableTipoString))  # Funcion type muestra el tipo de variable
variableTipoNumber: int = 2  # Se puede mostrar el tipo de variable a usar con :
print(type(variableTipoNumber))  # int
variableTipoFlotante = 10.78  #Flotante
print(type(variableTipoFlotante))
variableBoolean = True  # True o False clase bool usa mayus
print(type(variableBoolean))

# Repaso - muestra dinamismo variables
variableDinamica = 0
print(variableDinamica)
print(type(variableDinamica))
variableDinamica = 0.133
print(variableDinamica)
print(type(variableDinamica))
variableDinamica = "cambio de tipo la variable"
print(variableDinamica)
print(type(variableDinamica))
variableDinamica = False
print(variableDinamica)
print(type(variableDinamica))  # la variable va cambiando

# Tipo cadena - y concatenacion
variableGrupoFavorito = "Nirvana"+" "+"check"  
print("Mi grupo favorito es :"+variableGrupoFavorito)
//muestra de concatenacion
variableUno = "1"
variableDos = "2"
print(variableUno+variableDos)  # resultado 12 
print(int(variableUno)+int(variableDos))  #pasamos a int
varboolean = 1 > 2  # devuelve un bool
print(varboolean)

# Condicion if (si, sino)
if varboolean:  # if, como en pseint
    print("Resultado True")
else:  # Sintaxis if/else/elif + : else: elif: if:
    print("Resultado Falso")

# Entrada de datos
resultadoInput = input("Ingrese un valor para otorgarle a la variable.")  # La funcion input retorna un dato tipo string
# Ingreso de valor para que la variable obtenga ese valor y se guarde
print(resultadoInput)
# Cibvertir datos de u tipo a otro
inputCambioDeTipoDeDato = int(input("Ingreso de dato STR, pero se cambia a int, ingrese numero "))
input2 = int(input("Segundo numero "))  # se debe usar un int, con string daria error
result = inputCambioDeTipoDeDato+input2
print("El resultado es ", result)
print("Fin clase 3")
print(" ")
"""

"""
# Clase 4 :
# Primer video clase  4
# usar f para format o imprimir una variable en un print
# Operador aritmetico suma/adicion/addition
varUno = 10
varDos = 3
result = varUno + varDos
print(f"Result of addition = {result}")
# Fin del video clase 4

# Segundo video de la clase 4
# Operador aritmetico 
rest = varUno - varDos
print(f"Result of rest = {rest}")
# Operador aritmetico de multiplicacion:
multiplication = varUno * varDos
print(f"Result of multiplication = {multiplication}")
# Operador aritmetico de division
division = varUno / varDos
print(f"Result of division = {division}")
# Python transforma autimaticamente int a float si hace falta
# Operador integer division
division2 = varUno // varDos
# Operador
print(f"Result of division with integer = {division2}")
# Operador modulo
module = varUno % varDos
print(f"Result of modulo = {modulo}")  # Significa 10/3 = 9,queda un resto de 1
# Operador exponencial
exponencial = varUno ** varDos  # potenciacion 
print(f"Resultado de exponencial = {exponencial}")
# Fin del video dos de la clase 4
"""

"""
# Tercer video de la clase 4 (Consigna a realizar, en otro archivo (realizado))
"""

"""
# Cuarto video de la clase 4
# Operadores de asignacion y comparacion:
miVariable = 10
print(miVariable)
# Operadores de reasignacion
miVariable = miVariable+1
print(miVariable)  # Reasignacion de valor de la variable
# Otra forma de reasignacion acotada
miVariable += 1  # menos cantidad de codigo en mi caso prefiero la forma normal
print(miVariable)
# Esta forma de reasignacion se puede usar con otros operadores aritmeticos
miVariable -= 2
print(miVariable)
miVariable *= 30
print(miVariable)
miVariable /= 30
print(miVariable)
miVariable **= 2
print(miVariable)
miVariable %= 9
print(miVariable)
"""

"""
# Quinto video de la clase 4
# Operadores arimeticos sobre cadena de texto :
variableHola = "Hola "
print(variableHola)
variableHola *= 4
print(variableHola)
print(" ")
# Operadores de comparacion
x = 4
y = 3
# Operador de igualdad =, ==
resultado = x == y  # devuelve resultado booleano (true o false)
print(resultado)  # False
# Operador diferente !
resultadoCero = x != y  # distintos?
print(resultadoCero)  # True, son distintos? True
# Operadores mayores, menores, iguales < , > , =
resultadoUno = x >= y  # Comprobamos si x es mayor a y , devuelve el resultado booleano (true o false)
print(resultadoUno)  # x es mayor o igual a y? True
"""

"""
# Sexto video clase 4
# Consignas , ejercicio 1 y 2 video 6 clase 4 en otro archivo
"""

"""
# Video uno clase 5
# Operadores logicos :
# Operador and >>> Devuelve True si ambos operandos son True (a and b)
# Operador or >>> Devuelve True si alguno de los operandos es True (a or b)
# Operador not >>> Devuelve True si alguno de los operandos es False (not a)
# Operador and (operador binario, necesita dos valores almenos para un funcionamiento correcto)
a = True
b = True
c = False
d = False
resultado = a and b  # Operador and > a y b son true, por tanto sera true
resultado1 = a and c  # Operador and > a y c no son true, por tanto devuelve false
resultado2 = d and c  # Operador and > d y c no son true, por tanto devuelve false
print(resultado)
print(resultado1)
print(resultado2)
print(" ")
# Operador or (operador binario, necesita dos valores almenos para un funcionamiento correcto)
resultadoOr = a or b  # Operador or > a o b, alguno es true? si, por tanto devuelve true
resultadoOr1 = d or c  # Operador or > d o c, alguno es true? no, por tanto devuelve false
resultadoOr2 = a or c  # Operador or > a o c, alguno es true? si, por tanto devuelve true
print(resultadoOr)
print(resultadoOr1)
print(resultadoOr2)
print(" ")
# Operador not (operador univario, solo necesita un valor, para ejecutarse)
resultadoNot = not a  # Operador not, si este es true devuelve false, si es false devuelve true, invertido de valor
print(resultadoNot)
"""

"""
# Video dos clase 6
# Video del 2 al 6 son ejercicios de la clase 6, en otro archivo.
"""

"""
# Clase 6, video 1
# Sentencias if/else: direccionamiento por un camino u otro a partir de if/else y la intruccion que declaremos
# Intruccion booleana, se ejecuta solo un camino, verdadero o falso
# La sentencia if es obligatoria, no el elif y else, estas quedan a disposicion del programador si desea usarlas o no
# Condiciones: True,False, sin especificacion (un determinado valor, pero no determinamos si este es true o false)
# Las condiciones, y variables, programa, lo que querramos que funcione dentro de un if/else/elif, debe estar al mismo
# nivel de identacion (dabulador,espacio,espacios), para que funcione correctamente

# Clase 6, video 2
# Debug en if/else (paso a paso): punto de ruptura, entre especificacion de que linea de codigo es,y el codigo perse
# Seleccionamos el punto de ruptura (graficado como punto rojo), este para la ejecucion del codigo en la linea puntuada
# Uso de debug en pycharm+archivo que querramos y hayamos seleccionado el punto de ruptura,y muestra como trabaja el
# El punto de ruptura, y el paso a paso solo se correra si utilizamos DEBUG de pycharm, no con correr el programa normal
# codigo. F8, avanza un "paso">step over. Dependiendo el codigo especifico, las especificaciones que mostrara el debug
# Debug significado: Depuracion/depurar, limpieza, se muestra el codigo y si existe algun error para reparar/mejorar

# Clase 6, video 3
# Uso de git: Commit,log,add de los archivos python, mediante git
# En pycharm, muestra commit o si falta guardar algo(trabajo realizado sin guardar en git) en la seccion superior
# derecha (Git: Flecha azul (dibujo))
"""

"""
# Clase 6, video 4
# Conversion de int(numero) a str(string/texto):
num = int(input("Digite un numero entre 1-3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"  # De acuerdo a el valor (int) que ingrese el usuario, se asigna a un valor texto(str)
elif num == 2:               # a una variable
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Numero fuera del rango"
print(f"Numero ingresado: {num} - {numTexto}.")  # Tenemos guardado el valor tanto como int como texto(str), para su uso
"""

"""
# Clase 6, video 5
# Ejercicio en otro archivo.
"""

"""
# Clase 6, video 6 
# Ctrl + / (control y diagonal) = comentar/descomentar lineas de codigos seleccionadas
# # Sintaxys simplificada (Operador ternario) en if/else:
condicion = False  # Valor de la variable
print("Condicion verdadera") if condicion else print("Condicion false")
# Si condicion true ejecuta lo primero, else lo segundo
# Sintaxys simplificada se recomienda solo para codigo pequeño, comprobacion pequeña de if/else
# No se debe utilizar elif, solo if/else. Cuando el codigo tiene mas lineas, no se recomienda el operador ternario
# Si el codigo es amplio se recomienda el if/else "comun".
"""

# Clase 7, ejercios en otro archivo.
#