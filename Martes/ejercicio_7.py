numeros = []
for i in range(5):
    numero=float(input("Escribe un número para guardarlo en la lista: "))
    numeros.append(numero)

suma = sum(numeros)
print("La suma de todos los números de la lista es: ", suma)
