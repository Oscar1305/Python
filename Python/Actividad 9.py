"""
9. Diseñar iun algoritmo que imprima y sume la serie de números 3, 6, 9, 12 ..., 99.
"""
contador = 3
suma = 0

#Sin utilizar una función

while contador < 99:
    print (contador)
    suma += contador
    contador += 3

#Utilizando una función

def SumarNumeros(contador_, suma_):
    while contador_ < 100:
        #Si es múltiplo de 3 incrementamos la suma
        if contador_ %3 == 0:
            suma_ += contador_
            print(contador_)
        contador_ += 1
    return suma_

print("Suma: " + str(SumarNumeros(contador, suma)))
