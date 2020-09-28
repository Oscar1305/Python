x = 0

def calcularSuma(num1, num2, num3):
    suma = num1 + num2 + num3
    return suma

while x <= 10:
 
    if calcularSuma(x, x, x) > 20:
        break
    print(calcularSuma(x, x, x))
    x += 1
    
