notaStr = input("Proporciona un valor entre 0 y 10:")
try:
    nota = float(notaStr)
    if nota >= 9 and nota <= 10:
        notaFinal = 'A'
    elif nota >= 8  and nota < 9:
        notaFinal = 'B'
    elif nota >= 7  and nota < 8:
        notaFinal = 'C'
    elif nota >= 6  and nota < 7:
        notaFinal = 'D'
    elif nota >= 0  and nota < 6:
        notaFinal = 'F'
    else:
        notaFinal = "Valor desconocido"
    
    print("La nota final es:", notaFinal)
except ValueError:
    print("Ocurrio un error")
