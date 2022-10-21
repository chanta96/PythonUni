class Persona:
    def __init__(self,nombre = None , apellido = None, email = None,edad = None) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._edad = edad
    
    def __str__(self) -> str:
        return f'''
nombre: {self._nombre}
apellido: {self._apellido}
email: {self._email}
edad: {self._edad}
        '''
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,value):
        self._apellido = value
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        self._email = value
    
    @property
    def edad (self):
        return self._edad
    @edad.setter
    def edad(self,value):
        self._edad = value
    
    def mostrar_detalles(self):
        return f'''
nombre : {self.nombre}
apellido :s{self.apellido}
edad : {self.edad}
email : {self.email}
        '''

if __name__ == '__main__':
    # personas = []
    # persona1 = Persona(nombre = 'gonzalo',apellido = 'gramajo',email = 'gramajo@mail.com',edad = 31)
    # personas.append(persona1)
    # persona2 = Persona(nombre = 'ariel',apellido = 'betancud',email = 'betancud@mail.com',edad = 42)
    # personas.append(persona2)
    # for persona in personas:
    #     print (persona)
    
    #-------------------------------------------------------------------------------------------------
    
    #tarea crear tres objetos mas utilizando los metodos getter and setter
    #para modificar y mostrar los cambios
    persona3 = Persona('Carlos','defederico','cfederico@mail.com',27)
    print(f'\npre modificacion\nnombre : {persona3.nombre}\napellido: {persona3.apellido}\nedad : {persona3.edad}' )
    persona3.nombres = 'Oscar'
    persona3.apellido = 'Delia'
    persona3.edad = 28
    persona3.email = 'ODelia@mail.com'

    print (persona3.mostrar_detalles())

    persona4 = Persona(nombre = 'javi',apellido='garcia',edad = 32)
    print(f'\npre modificacion\nnombre : {persona4.nombre}\napellido: {persona4.apellido}\nedad : {persona4.edad}' )
    persona4.nombres = 'Pedrito'
    persona4.apellido = 'Mendez'
    persona4.edad = 21
    print(persona4.mostrar_detalles())

    persona5 = Persona(nombre = 'hernan',apellido = 'Martinez',edad = 22)
    print(f'\npre modificacion\nnombre : {persona5.nombre}\napellido: {persona5.apellido}\nedad : {persona5.edad}' )
    persona5.nombres = 'Federico'
    persona5.apellido = 'De La Rua'
    persona5.edad = 86
    print(persona5.mostrar_detalles())
    