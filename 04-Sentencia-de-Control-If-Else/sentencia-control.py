condicion = False

print("True") if condicion else print("False")

if condicion == True:
    print("La condicion es True")
elif condicion == False:
    print("La condicion es False")
else:
    print("Condicion no reconocida")
    
numero = int(input("Ingresa un numero entre 1 y 3:"))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else: 
    numeroTexto = "Fuera de rango"
    
print("numero ingresado:", numeroTexto)
