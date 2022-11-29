from gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())


gerente1 = Gerente('Gonzalo', 123123, 'Salubridad')
imprimir_detalles(gerente1)
