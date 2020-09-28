"""
21.1 Dado un array de 25 números, encuentra el número par más alto.
"""
import random
longitud = 25
numeros = []

def insertarNumeros(longitud_):
    for i in range(longitud_):
        numeros.append(int(random.uniform(0, 101)))
        print(numeros[i])

def obtenerMayorPar(numeros_):
    mayor = 0
    for i in range(len(numeros_)):
        if mayor < numeros_[i] and numeros_[i] % 2 == 0:
            mayor = numeros_[i]
    return mayor

insertarNumeros(longitud)
print("***************")
print(obtenerMayorPar(numeros))
