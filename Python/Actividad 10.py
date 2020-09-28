numero = int(input("Número: "))

def esPrimo(num):
    cont = 2
    primo = True
    while cont < num:
        if num % cont == 0:
            primo = False
            break
        cont += 1
    return primo

if esPrimo(numero) == True:
    print("Es primo")
else:
    print("No es primo")
    
