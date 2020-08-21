numero1 = int(input("Proporciona el numero1:"))
numero2 = int(input("Proporciona el numero2:"))
numeroMayor = None

if numero1 > numero2:
    numeroMayor = numero1
elif numero2 > numero1:
    numeroMayor = numero2

if numeroMayor:
    print("El numero mayor es:", numeroMayor)
else:
    print("Los valores son iguales")
    