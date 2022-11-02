class Color:
    """
    creacion de constructor color, que recibe un color 'puede ser un string indicando el nombre'
    o una tupla indicando el color rgb

    """
    def __init__(self,color) -> None:
        self._color = color
    '''
    sobreescritura del metodo str en la clase color con formateo de string
    '''
    def __str__(self) -> str:
        return f'{self._color}'
    
    '''
    definicion de setter y getters de atributo de la clase color
    '''
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color = value


'''
creacion de instancias de ejemplo de la clase color que solo se ejecutan en este archivo
'''

if __name__ == "__main__":
    color_rojo = Color((255,255,255))
    print(color_rojo)