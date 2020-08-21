a = 3
b = 2

resultado = a == b
print("a == b", resultado)

resultado = a != b
print("a != b", resultado)

resultado = a > b
print("a > b", resultado)

resultado = a >= b
print("a >= b", resultado)

resultado = a < b
print("a < b", resultado)

resultado = a <= b
print("a <= b", resultado)

resultado = a % 2 == 0
print("a % b == 0", resultado)

if a % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    
edadLimite = 18
edadPersona = 5

if edadPersona >= edadLimite:
    print("Es mayor de edad")
else:
    print("Es menor de edad")