numsPar = []

for i in range (5):
    numero = int(input(f"Ingresa un numero {i+1}: "))
    if numero % 2 == 0:
        numsPar.append(numero)
    
print ("numeros pares ingresados: ", numsPar)