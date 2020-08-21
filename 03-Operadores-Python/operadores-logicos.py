a = int(input("Ingresa un valor:"))
valorMinimo = 0;
valorMaximo = 5;

dentroRango = a >= valorMinimo and a <= valorMaximo
print(dentroRango)
if dentroRango:
    print("Dentro de rango")
else:
    print("Fuera de rango")
    
vacaciones = False
diaDescanso = False

if not(vacaciones or diaDescanso):
    print("Tienes deberes para hacer")
else:
    print("Ir al parque")
    
print(not(vacaciones))