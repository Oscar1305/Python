"""
7. Leer un carácter y deducir si está situado antes de la letra "m" en orden alfabético
"""

m = ord("m")

#Opción 1
caracter = input("Dime una letra: ")
caracter = ord(caracter)

def comprobarPosiciones(eme, caract):
    if caract < eme:
        print("está antes")
    else:
        print("está después")

comprobarPosiciones(m, caracter)

#Opción 2

"""
caracter = input("Dime una letra: ")
caracter = ord(caracter)

def comprobarPosicion(eme, caract):
    if caract < eme:
        return True
    else:
        return False

if comprobarPosicion(m, caracter)== True:
    print("Está antes")
else:
    print("Está después")
"""
