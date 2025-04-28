hora = int(input("Ingresa la hora (0 - 23): "))

if hora < 12 or hora > 18:
    print("No es hora de tranajar")
else:
    print("Hora de trabajar")