"""
21. Diseñar un algoritmo qwue calcule el mayor valor de una lista L de N elementos

1. Función para almacenar números de forma alaetoria en la lista

2. Función para comprobar el número mayor incluido en la lista 
"""
import random

longitud = 1000
numeros = [None] * longitud

def insertarNumeros():
    for i in range(len(numeros)):
        numeros[i] = int(random.uniform(0, 10000))
        print(numeros[i])

def obtenerNumMayor(numeros_):
    mayor = numeros_ [0]
    for i in range(len(numeros)):
        if mayor < numeros_ [i]:
            mayor = numeros_[i]
    return mayor

insertarNumeros()
print(obtenerNumMayor(numeros))
