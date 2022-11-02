from cuadrado import Cuadrado

if __name__ == '__main__':
    cuadrado1 = Cuadrado(4,5,(255,255,255))
    print(cuadrado1)
    print(f'area de su {cuadrado1.check_cuadrado()} = {cuadrado1.calcular_area()}')
    # print(f'es un rectangulo o un cuadrado? {cuadrado1.check_cuadrado()}')