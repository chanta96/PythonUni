class Animal:
    def __init__(self,name,age,state):
        self.name = name
        self.age = age
        self.state = state
    
    def __str__(self) -> str:
        return (f'name :{self.name} \nedad:{self.age} \nestado:{self.state}')

class Mamifero(Animal):
    def __init__(self,name,age,state,species):
        self.name = name
        self.age = age
        self.state = state
        self.species = species
    
    def __str__(self) -> str:
        return (f'species : {self.species}\n')+super().__str__() 

class Agus:
    def init(self):
        self.__name = 0
    def __str__(self) -> str:
        return f'name : {self.__name}'

    @property
    def name(self):
        print('getter called')    
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    

apolo = Mamifero('apolo','1','live','mamifero')
animal1 = Animal('carlos', '15','VIVO')
print(apolo)
print(animal1)
agus1 = Agus()
agus1.name = 'agus'
print(agus1.name)
