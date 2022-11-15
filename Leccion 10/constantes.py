# en python no existen las constantes, estas se declaran en mayuscula
# para que otros programadores sepan que estas variables no pueden modificarse
import math
MI_CONST = 1231
SEGUNDA_CONSTANTE = 12312


class Matematicas():
    PI = math.pi


if __name__ == '__main__':
    print(MI_CONST * SEGUNDA_CONSTANTE)