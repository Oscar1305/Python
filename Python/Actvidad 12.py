"""
12. Visualizar los múltiples de 4 comprendidos entre t y N, donde N es un número introducido por teclado.
"""
numero = int(input("numero (a partir de 4): "))
multiplos = []
contador = 4
while contador <= numero:
    if contador % 4 == 0:
        multiplos.append(contador)
        #print(contador)
    contador += 1
#print(multiplos)
contador = 0
while contador < len(multiplos):
    print(multiplos[contador])
    contador += 1
