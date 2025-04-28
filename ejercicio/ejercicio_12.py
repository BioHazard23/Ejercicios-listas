frutas = ["manzanza", "pera", "platano", "fresa"]
print (frutas)
eliminar = input("Que fruta quieres eliminar: ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print("fruta eliminada: ", eliminar)
else:
    print("La fruta no esta en la lista.")
print("Lista de frutas: ", frutas)
