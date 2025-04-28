nota = float(input("Ingresa tu nota (o al 10): "))

if nota < 5:
    print("Perdiste")
elif nota >= 5 and nota < 7:
    print("Aprobaste")
elif nota >= 7 and nota <= 10:
    print("Eres sobresaliente")
else:
    print("nota no valida")