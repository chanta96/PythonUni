class MiClase:
    variable_clase = 'esta es una variable de clase'

    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia
    
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

print(MiClase.variable_clase)
miclase1 = MiClase('variable de instancia')
print(miclase1.variable_instancia)
print(miclase1.variable_clase)
miclase2 = MiClase('valor variable de instancia 2')
MiClase.variable_clase2 = 'valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miclase2.variable_clase2)
print('*'*50)
MiClase.metodo_estatico()