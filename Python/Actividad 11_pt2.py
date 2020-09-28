"""
11. Calcular la media de 10 números introducidos por teclado y visualizar su resultado.
"""

numeros = []
cont = 1

while cont < 10:
    numero = int(input("Dime tu número" + str(cont) + " : " ))
    numeros.append(numero)
    cont += 1
#print(numeros)
    
def calcularMedia(nums):
    suma = 0
    cont = 0
    while cont < len(nums):
        suma += nums[cont]
        cont += 1
    return suma / len(nums)

print(calcularMedia(numeros)
