class FiguraGeometrica(object):
    ''''
    creacion de la clase FiguraGeometrica y constructor
    '''
    def __init__(self,ancho,alto) -> None:
        self._ancho = ancho
        self._alto = alto
    '''
    metodo str con f string
    '''
    def __str__(self) -> str:
        return f'''ancho : {self._ancho}
alto : {self._alto}'''

    '''
    metodos getter y setter
    '''
    @property
    def ancho (self):
        return self._ancho
    @ancho.setter
    def ancho(self,value):
        self._ancho = value
    
    @property
    def alto (self):
        return self._alto
    @alto.setter
    def alto(self,value):
        self._alto = value
    
'''
prueba de funcionamiento de la clase FiguraGeometrica solamente en este archivo
'''

if __name__ == '__main__':
    figura = FiguraGeometrica(25,4)
    print(figura)