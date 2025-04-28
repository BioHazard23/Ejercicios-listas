numeros = [1, 2, 3, 4, 5]
print (numeros)

agregar = int(input("Ingresa un numero para agregar a la lista:  "))
posicion = int(input("En que posicion lo vas a agregar (0 - 4): "))

numeros.insert(posicion, agregar)
print (numeros)