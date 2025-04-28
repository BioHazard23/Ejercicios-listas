numeros = [1, 2, 3, 4, 5, 6]

encontrar = int(input("Ingresa un numero que desees buscar: "))

if encontrar in numeros:
    ubicacion = numeros.index(encontrar)
    print ("el numero que ingresaste esta en la posicion: ", ubicacion)
    print("\n", numeros)
else:
    print("El numero no esta en la lista")