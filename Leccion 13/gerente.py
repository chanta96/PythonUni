from empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento) -> None:
        super().__init__(nombre, sueldo)
        self._departamento = departamento

    def __str__(self) -> str:
        return f'''{super().__str__()}
departamento = {self._departamento}'''

    def mostrar_detalles(self):
        return self.__str__()

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        self._departamento = value


if __name__ == '__main__':
    empleado1 = Gerente('Gonzalo', 280000, 'Gerente')
    print(empleado1)
