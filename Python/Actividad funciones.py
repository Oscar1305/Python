"""
Calcula el volumen y área de un cuadrado.
"""
lado = float(input("Lado del cuadrado: "))

def calcularVolumen(lado_):
    return lado_ * lado_

def calcularArea(lado_):
    return lado_ * 4

print("Volumen: " + str(calcularVolumen(lado)))
print("Área: " + str(calcularArea(lado)))
