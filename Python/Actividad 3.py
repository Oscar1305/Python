"""
3. Escribir un algoritmo que lea cuatro números y, a continuación, ecriba el mayor de los cuatro.
"""
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
num4 = int(input("num4: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print (str(num1))
elif num2 > num1 and num2 > num3 and num2 > num4:
    print (str(num2))
elif num3 > num1 and num3 > num2 and num3 > num4:
    print (str(num3))
else:
    print (str(num4))
