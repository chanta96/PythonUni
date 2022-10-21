# ejercicio 2 :  operaciones de conjuntos con listas
#escriba un programa que tenga 2 listas y que a continuacion
#cree las siguientes listas (en las que no deben haber repeticiones)
#1 lista de palabras que aparecen en las listas
#2 lista de palabras que aparecen en la primera lista pero no en la segunda
#3 lista de palabras que aparecen en la segunda lista pero no en la primera
#4 lista de palabras que aparecen en ambas listas
from doctest import NORMALIZE_WHITESPACE


def normalize(lista):
    normalized = []
    for names in lista:
        normalized.append(names.lower())
    normalized = set(normalized)
    sorted(normalized)
    return list(normalized) 

lista_1 = normalize(['carlos','pepito','pedrito'])
lista_2 = normalize(['gonzalo','luciana', 'pedrito'])
punto1  = lista_1 + lista_2
print(punto1)
punto2 = list(set(lista_1) - set(lista_2))
print(punto2)
punto3 = list(set(lista_2) - set(lista_1))
print(punto3)
punto4 = set(lista_1 + lista_2)
print(sorted(punto4))