"""
8. Leer un carácter y deducir si está situado entre la "I" y "M" en orden alfabético.
"""

letra = input ("Letra mayúscula: ")
letra = ord (letra)

def obtenerPosicion(letra_):
    M = ord("M")
    I = ord("I")
    if letra_ < M and letra_ > I:
        print("Está dentro")
    else:
        print("Está antes o después")

obtenerPosicion(letra)
