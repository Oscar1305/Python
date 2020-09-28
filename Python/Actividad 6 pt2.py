"""
6. Escribir un algoritmo que calcule la superficie de un triángulo en función de la base y la altura: s = (b * h) / 2.
"""
base = int(input("Base: "))
altura = int(input("Altura: "))

#Defino una función
def calcularSuperficie(b, h):
    #Resultado que obtengo de la función:
    return (b * h) /2
#Ejecuto la función e imprimo el resultado:
superficie = calcularSuperficie(base, altura)
print(superficie)
