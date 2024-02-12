# EJERCICIO 5
for num in range(1,13):
    for num2 in range(1,13):
        print(f"{num}*{num2}={num*num2}")

# EJERCICIO 6
intentos = 3
while intentos > 0:
    contraseña = input("Ingresa tu contraseña: ")
    if contraseña != "Sistema2023":
        intentos -= 1
        print("Contraseña incorrecta, intentos faltantes: ", intentos)
    else:
        print("Contraseña correcta."); break
import random
# EJERCICIO 7
listaedades = [45, 18, 15, 20, 14, 35]
# EJERCICIO 8
cantMayorDeEdad = 0
for edad in listaedades:
    if edad >= 18:
        cantMayorDeEdad += 1
print(cantMayorDeEdad)

# EJERCICIO 9
lista_clientes = []
cantClientes = int(input("¿Cuántos clientes quieres agregar? "))
for i in range(cantClientes):
    clientes = input("Ingrese el nombre del cliente: ")
    lista_clientes.append()
print(lista_clientes)