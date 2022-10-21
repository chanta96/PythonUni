import re


class Aritmetica:
    """
    docstring se utiliza para documentar clases
    """
    def __init__(self,operandoA,operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def __str__(self) -> str:
        return f'opA :{self.operandoA}\n opB :{self.operandoB}' 
    
    def sumar(self):
        return f'la suma es: {self.operandoA+self.operandoB}'

    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplication(self):
        return self.operandoA * self.operandoB
    
    def division(self):
        return self.operandoA / self.operandoB

test1 = Aritmetica(7.123123123,9.123123)
print(round(test1.sumar(),2))
