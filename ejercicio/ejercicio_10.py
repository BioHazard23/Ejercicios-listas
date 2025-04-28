edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print("Eres un niño")
elif edad >= 13 and edad < 18:
    print("Eres un adolecente")
elif edad >= 18 and edad < 60:
    print("Eres un adulto")
else:
    print("Eres un anciano")
