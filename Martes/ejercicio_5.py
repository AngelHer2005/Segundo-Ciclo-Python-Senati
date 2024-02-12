# EJERCICIO 1
contador = 0
while contador < 100:
    contador += 1
    print(contador)

# EJERCICIO 2
cont = 0
while cont < 50:
    cont += 1
    if cont % 2 == 0:
        print(cont)

# EJERCICIO 3
numero = 0
while numero > 50:
    numero += 1
    if numero % 2 != 0:
        print(numero)
# EJERCICIO 4
numero = int(input("Ingresa un número entero positivo: "))
print(numero)
while numero < 1:
    if numero <= 0:
        numero = int(input("No ingresaste un número entero. Ingresa un número entero positivo: "))  
        print(numero)
    else:
        numero = int(input("Ingresaste un número entero."))
        break   