print("Ingrese los siguientes datos del libro:")
nombre = input("Ingrese el nombre del libro:")
idBook = int(input("Ingresa el codigo del libro:"))
precio = float(input("Ingrese el precio del libro:"))
envioGratuito = input("Indica si el envio es gratuito(True/False):")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto debe ser True O False"
    
    
print("Nombre:", nombre)
print("Codigo:", idBook)
print("Precio:", precio)
print("Envio Gratuito?:", envioGratuito)


print(type(envioGratuito))