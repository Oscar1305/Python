"""
2. Se disponen de tres variables A, B, y C. Escribir las instrucciones necesarias para intercambiar entre sí sus valores del modo siguiente:

B toma el valor de A
C toma el valor de B
A toma el valor de C

*Sólo se puede utilizar una variable auxiliar!!
"""

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

auxa = A
auxb = B
auxc = C
B = auxa
C = auxb
A = auxc

print("A: " + str(A))
print("B: " + str(B))
print("C: " + str(C))
